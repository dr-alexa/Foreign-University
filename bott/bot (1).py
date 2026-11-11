"""
Телеграм-бот «Куда поехать учиться».
Запуск:
    pip install -r requirements.txt
    cp .env.example .env  # впишите токен
    python bot.py
"""
import asyncio
import logging
import os
import sqlite3
from datetime import datetime

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    LabeledPrice,
    Message,
    PreCheckoutQuery,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bott.data import (CAMPUS_LABEL, CAREER, CLIMATE_LABEL, COUNTRIES, FIELDS, MENTALITY_LABEL,
                       REGION_GROUP, REGIONS)

# ----------------------------------------------------------------------------
# Настройки
# ----------------------------------------------------------------------------
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

BOT_TOKEN = os.getenv("BOT_TOKEN", "9208515878:AAGee5Nc4SKpe8Pz9s8InyipfzaUTdCc8bE")
ADMIN_ID = int(os.getenv("ADMIN_ID", "1693248265"))  # ваш Telegram ID — сюда приходят заказы
DB_PATH = os.getenv("DB_PATH", "bot.db")

# Платные услуги. Цена — в Telegram Stars (⭐).
SERVICES = {
    "report": {
        "title": "📄 Персональный отчёт по стране",
        "desc": "Полный рейтинг всех стран под ваш профиль, детальная смета, сроки подачи, "
                "чек-лист документов и план действий. Приходит сразу.",
        "price": 150,
        "needs_country": True,
    },
    "letter": {
        "title": "✉️ Проверка мотивационного письма",
        "desc": "Разбор и правки вашего письма/эссе. Пришлите текст после оплаты — ответ в течение 48 часов.",
        "price": 300,
        "needs_country": False,
    },
    "consult": {
        "title": "🎓 Консультация 30 минут",
        "desc": "Личный созвон: выбор вуза, программы, стипендий и план поступления.",
        "price": 1000,
        "needs_country": False,
    },
}

QUESTIONS = [
    ("region", "🌍 <b>Какой регион рассматриваете?</b>",
     [("eu", "🇪🇺 Европа (ЕС)"), ("asia", "🌏 Азия"), ("any", "🤷 Везде")]),
    ("level", "🎓 <b>Какой уровень обучения вас интересует?</b>",
     [("bachelor", "Бакалавриат"), ("master", "Магистратура")]),
    ("field", "📚 <b>Какое направление?</b>\nОт него зависят сильные рынки труда и список вузов.",
     [(k, v) for k, v in FIELDS.items()] + [("any", "🤷 Пока не знаю")]),
    ("climate", "🌡 <b>Какой климат вам ближе?</b>",
     [("warm", "☀️ Тёплый"), ("moderate", "🌤 Умеренный"), ("cold", "❄️ Холодный"), ("any", "🤷 Не важно")]),
    ("budget", "💰 <b>Какой у вас бюджет в год</b> (обучение + проживание)?",
     [("low", "до 12 000 €"), ("mid", "12–20 000 €"), ("high", "20–35 000 €"), ("any", "Без ограничений")]),
    ("campus", "🏫 <b>Какой формат студенческой жизни предпочитаете?</b>",
     [("campus", "🌳 Кампус"), ("city", "🏙 Большой город"), ("any", "🤷 Не важно")]),
    ("lang", "🗣 <b>На каком языке готовы учиться?</b>",
     [("en", "🇬🇧 Только английский"), ("local", "📖 Готов учить местный язык")]),
    ("mentality", "🤝 <b>Какой менталитет местных вам комфортнее?</b>\n"
                  "<i>Это обобщение (опросы экспатов и модель Хофстеде), у каждого человека всё по-своему.</i>",
     [("warm", "😊 Открытые и общительные"), ("reserved", "🧊 Сдержанные, личное пространство"),
      ("formal", "📏 Формальные: правила и иерархия"), ("any", "🤷 Не важно")]),
    ("degree", "🎓🎓 <b>Нужен двойной (совместный) диплом?</b>",
     [("need", "Да, это важно"), ("nice", "Желательно"), ("no", "Не нужен")]),
    ("jobs", "💼 <b>Насколько важно быстро найти работу по специальности после выпуска?</b>",
     [("high", "Критично"), ("mid", "Важно, но могу искать до года"), ("any", "Не приоритет")]),
]
# Участники конвенций о признании квалификаций (ЮНЕСКО/Совет Европы) из нашей базы
LISBON = {"de", "nl", "cz", "pl", "fi", "it", "hu", "es", "at", "be", "bg", "hr", "cy", "dk", "ee", "fr", "gr",
          "ie", "lv", "lt", "lu", "mt", "pt", "ro", "sk", "si", "se", "ca", "tr", "kz", "ge"}
TOKYO = {"cn", "jp", "kr", "tr"}
BUDGET_LIMIT = {"low": 12_000, "mid": 20_000, "high": 35_000, "any": 10**9}

logging.basicConfig(level=logging.INFO)
router = Router()


class Letter(StatesGroup):
    waiting_text = State()


# ----------------------------------------------------------------------------
# База данных (SQLite): заказы
# ----------------------------------------------------------------------------
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER, username TEXT, service TEXT, country TEXT,
            stars INTEGER, charge_id TEXT, created_at TEXT
        )"""
    )
    return conn


def save_order(user_id, username, service, country, stars, charge_id):
    with db() as conn:
        conn.execute(
            "INSERT INTO orders (user_id, username, service, country, stars, charge_id, created_at) "
            "VALUES (?,?,?,?,?,?,?)",
            (user_id, username, service, country, stars, charge_id, datetime.utcnow().isoformat()),
        )


# ----------------------------------------------------------------------------
# Подбор стран
# ----------------------------------------------------------------------------
def annual_cost(c: dict) -> int:
    return int(sum(c["tuition"]) / 2 + c["living"] * 12)


def score_country(code: str, p: dict) -> tuple[float, list[str]]:
    c, cr = COUNTRIES[code], CAREER[code]
    s, why = 0.0, []

    # Регион (макс. 3)
    if p.get("region", "any") == "any":
        s += 2
    elif REGION_GROUP.get(code) == p["region"]:
        s += 3
        why.append("нужный регион")

    # Климат (макс. 4)
    pc = p.get("climate", "any")
    if pc == "any":
        s += 2
    elif c["climate"] == pc:
        s += 4
        why.append("климат как вы хотели")
    elif "moderate" in (c["climate"], pc):
        s += 2

    # Бюджет (макс. 4)
    cost, limit = annual_cost(c), BUDGET_LIMIT[p.get("budget", "any")]
    if cost <= limit:
        s += 4
        why.append("укладывается в бюджет")
    elif cost <= limit * 1.25:
        s += 2
        why.append("чуть выше бюджета, но реалистично со стипендией")

    # Кампус (макс. 2)
    pcam = p.get("campus", "any")
    if pcam == "any":
        s += 1
    elif c["campus"] in (pcam, "both"):
        s += 2
        why.append("подходящий формат вузов")

    # Язык (макс. 3)
    if p.get("lang", "en") == "en":
        s += c["english"]
        if c["english"] == 3:
            why.append("много программ на английском")
    else:
        s += 2

    # Менталитет (макс. 3)
    pm = p.get("mentality", "any")
    main, also, _ = cr["ment"]
    if pm == "any":
        s += 1.5
    elif main == pm:
        s += 3
        why.append("менталитет по вашему вкусу")
    elif pm in also:
        s += 1.5

    # Двойной диплом (макс. 3). Совместные магистратуры (EMJM) — только магистратура.
    dd = cr["dd"][0]
    if p.get("level") == "bachelor":
        dd = min(dd, 2)
    pd = p.get("degree", "no")
    if pd == "need":
        s += dd
        if dd >= 3:
            why.append("много двойных/совместных программ")
    elif pd == "nice":
        s += dd * 0.7
    else:
        s += 1.5

    # Трудоустройство (макс. 4): занятость выпускников + право остаться после диплома
    tier, months = cr["jobs"][0], cr["stay_months"] or 0
    base = tier + (1 if months >= 18 else 0.5 if months >= 9 else 0)
    pj = p.get("jobs", "any")
    if pj == "high":
        s += base
        if tier == 3:
            why.append("высокая занятость выпускников")
        if months >= 18:
            why.append("долгий срок на поиск работы")
    elif pj == "mid":
        s += base * 0.75
    else:
        s += 2

    # Направление (макс. 2)
    pf = p.get("field", "any")
    if pf == "any":
        s += 1
    elif pf in cr["strong"]:
        s += 2
        why.append("сильный рынок по вашему направлению")

    return s / 28, why


def rank(p: dict) -> list[tuple[str, float, list[str]]]:
    res = [(code, *score_country(code, p)) for code in COUNTRIES]
    # при равных баллах: больше англоязычных программ, затем дешевле
    return sorted(res, key=lambda x: (-x[1], -COUNTRIES[x[0]]["english"], annual_cost(COUNTRIES[x[0]])))


# ----------------------------------------------------------------------------
# Вспомогательные функции
# ----------------------------------------------------------------------------
async def send_long(target: Message, text: str):
    """Telegram ограничивает сообщение 4096 символами — режем по строкам."""
    chunk = ""
    for line in text.split("\n"):
        if len(chunk) + len(line) + 1 > 3900:
            await target.answer(chunk)
            chunk = ""
        chunk += line + "\n"
    if chunk.strip():
        await target.answer(chunk)


def kb_question(idx: int):
    key, _, options = QUESTIONS[idx]
    kb = InlineKeyboardBuilder()
    for val, label in options:
        kb.button(text=label, callback_data=f"q:{idx}:{val}")
    kb.adjust(2)
    return kb.as_markup()


def kb_country(code: str):
    kb = InlineKeyboardBuilder()
    kb.button(text="🎁 Стипендии", callback_data=f"sch:{code}")
    kb.button(text="🏛 Университеты", callback_data=f"uni:{code}")
    kb.button(text="💼 Работа после учёбы", callback_data=f"job:{code}")
    kb.button(text="🎓 Двойной диплом", callback_data=f"dd:{code}")
    kb.button(text="🤝 Менталитет и язык", callback_data=f"cult:{code}")
    kb.button(text="⭐ Платные услуги", callback_data=f"shop:{code}")
    kb.button(text="⬅️ К подбору", callback_data="results")
    kb.adjust(2)
    return kb.as_markup()


def country_card(code: str) -> str:
    c = COUNTRIES[code]
    t_min, t_max = c["tuition"]
    tuition = "бесплатно (публичные вузы)" if t_max == 0 else (
        f"{t_min:,}–{t_max:,} € / год".replace(",", " ") if t_min else f"до {t_max:,} € / год".replace(",", " ")
    )
    return (
        f"<b>{c['name']}</b>\n\n{c['about']}\n\n"
        f"🌡 Климат: {CLIMATE_LABEL[c['climate']]}\n"
        f"🏫 Вузы: {CAMPUS_LABEL[c['campus']]}\n"
        f"💶 Обучение: {tuition}\n"
        f"🏠 Проживание: ~{c['living']} € / мес\n"
        f"📊 Итого в среднем: ~{annual_cost(c):,} € / год".replace(",", " ")
    )


# ----------------------------------------------------------------------------
# Старт и опрос
# ----------------------------------------------------------------------------
@router.message(CommandStart())
async def start(m: Message, state: FSMContext):
    await state.clear()
    kb = InlineKeyboardBuilder()
    kb.button(text="🚀 Начать подбор", callback_data="begin")
    kb.button(text="🌍 Все страны", callback_data="all")
    kb.adjust(1)
    await m.answer(
        "👋 Привет! Я помогу выбрать страну для учёбы за рубежом.\n\n"
        "Задам 10 коротких вопросов (регион, уровень, направление, климат, бюджет, формат вуза, язык, менталитет, двойной диплом, работа), подберу страны, а потом покажу <b>стипендии</b> "
        "и <b>университеты по всем направлениям</b>.",
        reply_markup=kb.as_markup(),
    )


@router.callback_query(F.data == "begin")
async def begin(c: CallbackQuery, state: FSMContext):
    await state.update_data(profile={})
    await c.message.answer(QUESTIONS[0][1], reply_markup=kb_question(0))
    await c.answer()


@router.callback_query(F.data.startswith("q:"))
async def answer_question(c: CallbackQuery, state: FSMContext):
    _, idx, val = c.data.split(":")
    idx = int(idx)
    data = await state.get_data()
    profile = data.get("profile", {})
    profile[QUESTIONS[idx][0]] = val
    await state.update_data(profile=profile)

    if idx + 1 < len(QUESTIONS):
        await c.message.answer(QUESTIONS[idx + 1][1], reply_markup=kb_question(idx + 1))
    else:
        await show_results(c.message, profile)
    await c.answer()


async def show_results(message: Message, profile: dict):
    top = rank(profile)[:3]
    kb = InlineKeyboardBuilder()
    text = "🎯 <b>Лучшие варианты для вас:</b>\n\n"
    for i, (code, sc, why) in enumerate(top, 1):
        c = COUNTRIES[code]
        text += f"{i}. {c['name']} — <b>{int(sc * 100)}%</b>\n   <i>{', '.join(why) or 'универсальный вариант'}</i>\n"
        kb.button(text=c["name"], callback_data=f"c:{code}")
    kb.button(text="🌍 Все страны", callback_data="all")
    kb.button(text="🔁 Пройти заново", callback_data="begin")
    kb.adjust(1)
    await message.answer(text + "\nВыберите страну, чтобы узнать подробности 👇", reply_markup=kb.as_markup())


@router.callback_query(F.data == "results")
async def back_results(c: CallbackQuery, state: FSMContext):
    profile = (await state.get_data()).get("profile")
    if profile and len(profile) == len(QUESTIONS):
        await show_results(c.message, profile)
    else:
        await begin(c, state)
        return
    await c.answer()


@router.callback_query(F.data == "all")
@router.message(Command("countries"))
async def all_countries(event):
    kb = InlineKeyboardBuilder()
    for key, (title, codes) in REGIONS.items():
        kb.button(text=f"{title} ({len(codes)})", callback_data=f"reg:{key}")
    kb.adjust(1)
    msg = event.message if isinstance(event, CallbackQuery) else event
    await msg.answer(f"🌍 <b>Выберите регион</b> (всего стран: {len(COUNTRIES)}):", reply_markup=kb.as_markup())
    if isinstance(event, CallbackQuery):
        await event.answer()


@router.callback_query(F.data.startswith("reg:"))
async def region_countries(c: CallbackQuery):
    key = c.data.split(":")[1]
    title, codes = REGIONS[key]
    kb = InlineKeyboardBuilder()
    for code in codes:
        kb.button(text=COUNTRIES[code]["name"], callback_data=f"c:{code}")
    kb.adjust(2)
    kb.row(InlineKeyboardButton(text="⬅️ Все регионы", callback_data="all"))
    await c.message.answer(f"<b>{title}</b>\nВыберите страну:", reply_markup=kb.as_markup())
    await c.answer()


# ----------------------------------------------------------------------------
# Карточка страны, стипендии, университеты
# ----------------------------------------------------------------------------
@router.callback_query(F.data.startswith("c:"))
async def country(c: CallbackQuery, state: FSMContext):
    code = c.data.split(":")[1]
    await state.update_data(country=code)
    await c.message.answer(country_card(code), reply_markup=kb_country(code))
    await c.answer()


@router.callback_query(F.data.startswith("sch:"))
async def scholarships(c: CallbackQuery):
    code = c.data.split(":")[1]
    info = COUNTRIES[code]
    text = f"🎁 <b>Стипендии — {info['name']}</b>\n\n" + "\n".join(f"• {s}" for s in info["scholarships"])
    text += f"\n\n📅 <b>Сроки подачи:</b> {info['deadlines']}"
    text += "\n\n⚠️ Условия и страны-участницы меняются — сверяйтесь с официальными сайтами."
    kb = InlineKeyboardBuilder()
    kb.button(text="🏛 Университеты", callback_data=f"uni:{code}")
    kb.button(text="⬅️ Назад", callback_data=f"c:{code}")
    kb.adjust(1)
    await c.message.answer(text, reply_markup=kb.as_markup())
    await c.answer()


@router.callback_query(F.data.startswith("uni:"))
async def universities_menu(c: CallbackQuery):
    code = c.data.split(":")[1]
    kb = InlineKeyboardBuilder()
    for key, name in FIELDS.items():
        kb.button(text=name, callback_data=f"uf:{code}:{key}")
    kb.button(text="📋 Все направления сразу", callback_data=f"uall:{code}")
    kb.button(text="⬅️ Назад", callback_data=f"c:{code}")
    kb.adjust(1)
    await c.message.answer(
        f"🏛 <b>Университеты — {COUNTRIES[code]['name']}</b>\nВыберите направление:",
        reply_markup=kb.as_markup(),
    )
    await c.answer()


@router.callback_query(F.data.startswith("uf:"))
async def universities_field(c: CallbackQuery):
    _, code, field = c.data.split(":")
    unis = COUNTRIES[code]["universities"].get(field, [])
    text = f"<b>{FIELDS[field]} — {COUNTRIES[code]['name']}</b>\n\n" + "\n".join(f"• {u}" for u in unis)
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Другие направления", callback_data=f"uni:{code}")
    await c.message.answer(text, reply_markup=kb.as_markup())
    await c.answer()


@router.callback_query(F.data.startswith("uall:"))
async def universities_all(c: CallbackQuery):
    code = c.data.split(":")[1]
    text = f"📋 <b>Университеты по всем направлениям — {COUNTRIES[code]['name']}</b>\n"
    for key, name in FIELDS.items():
        text += f"\n<b>{name}</b>\n" + "\n".join(f"• {u}" for u in COUNTRIES[code]["universities"].get(key, [])) + "\n"
    await send_long(c.message, text)
    await c.answer()


# ----------------------------------------------------------------------------
# Работа, двойной диплом, менталитет и язык
# ----------------------------------------------------------------------------
SRC_LABEL = {"eurostat": "Eurostat", "estimate": "оценка, официальных сопоставимых данных нет"}
LISBON_TEXT = "все 27 стран ЕС, Канада, Турция, Казахстан, Грузия и другие (57 государств)"
TOKYO_TEXT = "Китай, Япония, Южная Корея, Турция, Австралия, Новая Зеландия и др. (12 государств)"


def recognition_text(code: str) -> str:
    cr_name = COUNTRIES[code]["name"]
    in_lisbon = code in LISBON
    in_tokyo = code in TOKYO
    parts = []
    if in_lisbon:
        parts.append(f"✅ <b>Лиссабонская конвенция</b> (ЮНЕСКО/Совет Европы): диплом из страны {cr_name} признаётся по общему правилу "
                     f"— если нет «существенных различий» — в странах-участницах: {LISBON_TEXT}.")
    if in_tokyo:
        parts.append(f"✅ <b>Токийская конвенция</b> (ЮНЕСКО, Азия и Океания): аналогичные правила действуют между участниками: {TOKYO_TEXT}.")
    if not parts:
        parts.append("⚠️ Страна не входит ни в Лиссабонскую, ни в Токийскую конвенцию (по проверенным данным): "
                     "признание диплома в других странах решается индивидуально национальным центром (ENIC-NARIC / APNNIC), "
                     "часто нужны апостиль и оценка диплома.")
    if in_lisbon and not in_tokyo:
        parts.append("🔀 С Китаем, Японией и Кореей прямого договора нет (кроме Турции): признание через национальные центры "
                     "или Глобальную конвенцию ЮНЕСКО (38 государств-участников на 30.09.2025).")
    if in_tokyo and not in_lisbon:
        parts.append("🔀 С Европой и Канадой прямого договора нет (кроме Турции): признание через национальные центры "
                     "или Глобальную конвенцию ЮНЕСКО (38 государств-участников на 30.09.2025).")
    return "\n\n".join(parts)


@router.callback_query(F.data.startswith("job:"))
async def job_view(c: CallbackQuery, state: FSMContext):
    code = c.data.split(":")[1]
    info, cr = COUNTRIES[code], CAREER[code]
    profile = (await state.get_data()).get("profile", {})
    tier, src, stat = cr["jobs"]
    stars = "🟢" * tier + "⚪" * (3 - tier)
    text = (
        f"💼 <b>Работа после учёбы — {info['name']}</b>\n\n"
        f"📊 <b>Занятость выпускников</b> {stars}\n{stat}\n<i>Источник: {SRC_LABEL[src]}</i>\n\n"
        f"🛂 <b>Можно ли остаться после диплома:</b>\n{cr['stay']}\n\n"
        f"📍 <b>Где искать работу:</b> {cr['hubs']}\n"
    )
    f = profile.get("field", "any")
    if f != "any":
        mark = "✅ входит в сильные направления рынка" if f in cr["strong"] else "⚠️ не входит в число самых сильных направлений"
        text += f"\n🎯 Ваше направление ({FIELDS[f]}): {mark}\n"
    if profile.get("level") == "bachelor" and code == "fr":
        text += "\n⚠️ Во Франции пост-учебное разрешение выдаётся при дипломе уровня master — бакалавриата недостаточно.\n"
    text += (
        "\nℹ️ <i>Как быстро найти работу — зависит от направления, языка и города. Официальной статистики «сколько дней "
        "ищут работу» нет: ближайший показатель — доля работающих недавних выпускников (Eurostat, возраст 20–34).</i>"
    )
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Назад", callback_data=f"c:{code}")
    await c.message.answer(text, reply_markup=kb.as_markup())
    await c.answer()


@router.callback_query(F.data.startswith("dd:"))
async def dd_view(c: CallbackQuery):
    code = c.data.split(":")[1]
    info, cr = COUNTRIES[code], CAREER[code]
    level, note = cr["dd"]
    stars = "⭐" * level + "☆" * (3 - level)
    text = (
        f"🎓 <b>Двойной диплом — {info['name']}</b> {stars}\n"
        "<i>Оценка доступности: 3 — много программ, 1 — выбор небольшой.</i>\n\n"
        f"{note}\n\n"
        "<b>Чем отличаются типы дипломов (по определениям Erasmus+):</b>\n"
        "• <b>Совместный (joint)</b> — один диплом от нескольких вузов;\n"
        "• <b>Двойной (double)</b> — два диплома от двух вузов; <b>множественный</b> — два и более.\n"
        "Совместные магистерские Erasmus Mundus (EMJM) — только магистратура.\n\n"
        f"🌐 <b>Где диплом из этой страны котируется:</b>\n{recognition_text(code)}\n\n"
        "⚠️ Чтобы двойной диплом «работал» везде, все страны-участницы программы должны его официально признать. "
        "Перед выбором программы проверьте признание в центре ENIC-NARIC нужной страны."
    )
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Назад", callback_data=f"c:{code}")
    await c.message.answer(text, reply_markup=kb.as_markup())
    await c.answer()


@router.callback_query(F.data.startswith("cult:"))
async def culture_view(c: CallbackQuery):
    code = c.data.split(":")[1]
    info, cr = COUNTRIES[code], CAREER[code]
    main, also, note = cr["ment"]
    eng = {3: "очень много программ на английском", 2: "достаточно программ на английском (чаще магистратура)",
           1: "программ на английском мало"}[info["english"]]
    text = (
        f"🤝 <b>Менталитет и язык — {info['name']}</b>\n\n"
        f"<b>Менталитет:</b> {MENTALITY_LABEL[main]}\n{note}\n\n"
        f"🗣 <b>Язык обучения:</b> {eng}.\n{cr['lang']}\n\n"
        "ℹ️ <i>Менталитет — обобщение на основе опросов экспатов (Expat Insider 2025, InterNations) и модели Хофстеде; "
        "опросы отражают опыт экспатов, а не студентов, и у каждого человека он свой.</i>"
    )
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅️ Назад", callback_data=f"c:{code}")
    await c.message.answer(text, reply_markup=kb.as_markup())
    await c.answer()


# ----------------------------------------------------------------------------
# Платные услуги (Telegram Stars)
# ----------------------------------------------------------------------------
@router.callback_query(F.data.startswith("shop"))
@router.message(Command("services"))
async def shop(event, state: FSMContext):
    code = None
    if isinstance(event, CallbackQuery):
        parts = event.data.split(":")
        code = parts[1] if len(parts) > 1 else None
    else:
        code = (await state.get_data()).get("country")
    msg = event.message if isinstance(event, CallbackQuery) else event

    kb = InlineKeyboardBuilder()
    text = "⭐ <b>Платные услуги</b>\n\n"
    for sid, s in SERVICES.items():
        text += f"<b>{s['title']}</b> — {s['price']} ⭐\n{s['desc']}\n\n"
        kb.button(text=f"{s['title']} · {s['price']}⭐", callback_data=f"buy:{sid}:{code or '-'}")
    kb.adjust(1)
    await msg.answer(text + "Оплата через Telegram Stars.", reply_markup=kb.as_markup())
    if isinstance(event, CallbackQuery):
        await event.answer()


@router.callback_query(F.data.startswith("buy:"))
async def buy(c: CallbackQuery, state: FSMContext):
    _, sid, code = c.data.split(":")
    s = SERVICES[sid]
    if s["needs_country"] and code == "-":
        await c.message.answer("Сначала выберите страну: /countries")
        await c.answer()
        return
    await c.message.answer_invoice(
        title=s["title"].split(" ", 1)[1],
        description=s["desc"][:255],
        payload=f"{sid}:{code}",
        currency="XTR",  # Telegram Stars
        prices=[LabeledPrice(label=s["title"][:30], amount=s["price"])],
        provider_token="",  # для Stars токен провайдера не нужен
    )
    await c.answer()


@router.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery):
    await q.answer(ok=True)


def build_report(profile: dict, code: str) -> str:
    c = COUNTRIES[code]
    text = f"📄 <b>Персональный отчёт: {c['name']}</b>\n\n{country_card(code)}\n"
    if profile and len(profile) == len(QUESTIONS):
        text += "\n<b>📊 Топ-10 стран под ваш профиль:</b>\n"
        for i, (cc, sc, _) in enumerate(rank(profile)[:10], 1):
            text += f"{i}. {COUNTRIES[cc]['name']} — {int(sc * 100)}% (~{annual_cost(COUNTRIES[cc]):,} €/год)\n".replace(",", " ")
    text += (
        f"\n<b>📅 Сроки:</b> {c['deadlines']}\n"
        f"\n<b>🛂 Виза и финансы:</b> {c['visa']}\n"
        f"\n<b>🎁 Стипендии:</b>\n" + "\n".join(f"• {s}" for s in c["scholarships"]) + "\n"
        f"\n<b>💼 Работа после учёбы:</b> {CAREER[code]['stay']}\n"
        f"📊 {CAREER[code]['jobs'][2]}\n📍 {CAREER[code]['hubs']}\n"
        f"\n<b>🎓 Двойные дипломы:</b> {CAREER[code]['dd'][1]}\n"
        f"\n<b>🤝 Менталитет:</b> {CAREER[code]['ment'][2]}\n"
        "\n<b>✅ План действий:</b>\n"
        "1. За 12 мес.: выбрать 3–5 программ, проверить требования и язык (IELTS/TOEFL/DSH/TestDaF).\n"
        "2. За 9–10 мес.: подготовить мотивационное письмо, резюме, рекомендации.\n"
        "3. За 8 мес.: подать документы в вузы и на стипендии.\n"
        "4. За 4–6 мес.: получить приглашение, оформить визу, найти жильё.\n"
        "5. За 1–2 мес.: страховка, билеты, перевод средств.\n\n"
        "<b>📎 Базовый пакет документов:</b> паспорт, аттестат/диплом с приложением (с переводом и апостилем/нострификацией), "
        "языковой сертификат, мотивационное письмо, резюме, фото, подтверждение финансов."
    )
    return text


@router.message(F.successful_payment)
async def paid(m: Message, state: FSMContext):
    pay = m.successful_payment
    sid, code = pay.invoice_payload.split(":")
    user = m.from_user
    save_order(user.id, user.username, sid, code, pay.total_amount, pay.telegram_payment_charge_id)
    logging.info("Paid: %s %s %s", user.id, sid, pay.total_amount)

    if sid == "report":
        profile = (await state.get_data()).get("profile", {})
        await send_long(m, build_report(profile, code))
    elif sid == "letter":
        await state.set_state(Letter.waiting_text)
        await m.answer("✅ Оплата получена! Пришлите одним сообщением текст вашего мотивационного письма.")
    elif sid == "consult":
        await m.answer("✅ Оплата получена! Я свяжусь с вами в ближайшее время, чтобы согласовать время созвона.")

    if ADMIN_ID and sid != "report":
        await m.bot.send_message(
            ADMIN_ID,
            f"💰 Новый заказ: {SERVICES[sid]['title']}\n"
            f"От: {user.full_name} (@{user.username}) id={user.id}\n"
            f"Страна: {code}\nСумма: {pay.total_amount} ⭐",
        )


@router.message(Letter.waiting_text, F.text)
async def letter_text(m: Message, state: FSMContext):
    await state.set_state(None)
    if ADMIN_ID:
        await m.bot.send_message(
            ADMIN_ID, f"✉️ Мотивационное письмо от @{m.from_user.username} (id={m.from_user.id}):\n\n{m.text}"
        )
    await m.answer("Получил! Ответ пришлю в течение 48 часов 🙌")


@router.message(Command("paysupport"))
async def pay_support(m: Message):
    # Telegram требует обработчик этой команды для платных ботов
    await m.answer("По вопросам оплаты и возвратов напишите администратору — укажите ID платежа из чека.")


@router.message(Command("help"))
async def help_cmd(m: Message):
    await m.answer(
        "/start — начать подбор\n/countries — все страны\n/services — платные услуги\n/paysupport — вопросы по оплате"
    )


# ----------------------------------------------------------------------------
async def main():
    if not BOT_TOKEN:
        raise SystemExit("Укажите BOT_TOKEN в .env")
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
