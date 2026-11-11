"""
База данных стран, стипендий и университетов.

ВАЖНО: цифры приблизительные (для студентов не из ЕС, в евро в год/месяц).
Перед публикацией бота проверьте и обновите данные по официальным сайтам.
Чтобы добавить страну или университет — просто дополните словарь COUNTRIES.
"""

FIELDS = {
    "it": "💻 IT и инженерия",
    "business": "📈 Бизнес и экономика",
    "med": "⚕️ Медицина",
    "hum": "📚 Гуманитарные и социальные науки",
    "nat": "🔬 Естественные науки",
    "arts": "🎨 Дизайн и искусство",
}

# climate: warm / moderate / cold
# campus: campus / city / both
# english: 1-3 — насколько широко доступны программы на английском
COUNTRIES = {
    "de": {
        "name": "🇩🇪 Германия",
        "climate": "moderate",
        "campus": "city",
        "english": 2,
        "tuition": (0, 1500),  # публичные вузы; в земле Баден-Вюртемберг ~1500 €/год
        "living": 950,
        "about": "Бесплатное или почти бесплатное обучение в публичных вузах, сильная инженерия и наука. "
                 "Многие магистерские программы на английском, бакалавриат чаще на немецком (нужен B2–C1).",
        "deadlines": "Зимний семестр: подача до 15 июля (через uni-assist — часто до 15 июля, "
                     "некоторые вузы до 31 мая). Летний семестр: до 15 января.",
        "visa": "Студенческая виза; блокированный счёт (~11 900 €/год), страховка, подтверждение языка.",
        "scholarships": [
            "DAAD — стипендии для магистров и аспирантов (покрывают проживание и страховку).",
            "Deutschlandstipendium — 300 €/мес от вуза и спонсоров (доступно и иностранным студентам).",
            "Erasmus Mundus Joint Masters — полные гранты на совместные магистерские программы.",
            "Фонды: Konrad-Adenauer, Friedrich-Ebert, Heinrich-Böll (чаще для магистров и PhD).",
        ],
        "universities": {
            "it": ["TU Munich (TUM)", "RWTH Aachen", "KIT Karlsruhe", "TU Berlin", "TU Dresden"],
            "business": ["University of Mannheim", "LMU Munich", "Frankfurt School of Finance", "WHU Vallendar"],
            "med": ["Charité Berlin", "Heidelberg University", "LMU Munich", "University of Freiburg"],
            "hum": ["Humboldt University Berlin", "FU Berlin", "Heidelberg University", "University of Tübingen"],
            "nat": ["Heidelberg University", "University of Göttingen", "University of Bonn", "University of Freiburg"],
            "arts": ["UdK Berlin", "Bauhaus-Universität Weimar", "HfG Karlsruhe", "Kunsthochschule Berlin-Weißensee"],
        },
    },
    "nl": {
        "name": "🇳🇱 Нидерланды",
        "climate": "moderate",
        "campus": "both",
        "english": 3,
        "tuition": (10000, 16000),
        "living": 1200,
        "about": "Самая «английская» страна континентальной Европы: тысячи программ на английском, "
                 "практикоориентированное обучение, высокие позиции в рейтингах.",
        "deadlines": "Большинство программ для non-EU: 1 апреля – 1 мая (медицина и программы с numerus fixus — "
                     "ещё раньше, до 15 января). Магистратура — часто до 1 марта – 1 апреля.",
        "visa": "Разрешение на проживание оформляет вуз; нужно подтверждение финансов (~1 000–1 300 €/мес).",
        "scholarships": [
            "Holland Scholarship — 5 000 € на первый год (для non-EEA бакалавриата и магистратуры).",
            "Amsterdam Excellence Scholarship (UvA), Utrecht Excellence Scholarship, Leiden Excellence и др.",
            "Erasmus Mundus Joint Masters.",
            "Wageningen Fellowship, University of Twente Scholarship (UTS), TU Delft Excellence Scholarship.",
        ],
        "universities": {
            "it": ["TU Delft", "TU Eindhoven", "University of Twente", "VU Amsterdam"],
            "business": ["Erasmus University Rotterdam (RSM)", "Tilburg University", "University of Amsterdam", "Maastricht University"],
            "med": ["Leiden University", "Utrecht University", "Amsterdam UMC", "Maastricht University"],
            "hum": ["University of Amsterdam", "Leiden University", "Utrecht University", "Radboud University"],
            "nat": ["Wageningen University", "Utrecht University", "University of Groningen", "Leiden University"],
            "arts": ["Design Academy Eindhoven", "Gerrit Rietveld Academie", "ArtEZ", "Willem de Kooning Academy"],
        },
    },
    "cz": {
        "name": "🇨🇿 Чехия",
        "climate": "moderate",
        "campus": "city",
        "english": 2,
        "tuition": (3000, 9000),  # английские программы; на чешском бесплатно
        "living": 700,
        "about": "Недорогая жизнь в центре Европы. Обучение на чешском бесплатное, на английском — платное. "
                 "Сильные технические вузы и медицина на английском.",
        "deadlines": "Обычно с февраля по 30 апреля – 31 мая; медицина — часто до 28 февраля – 31 марта. "
                     "Многие вузы требуют вступительный экзамен.",
        "visa": "Долгосрочная студенческая виза; нострификация аттестата; подтверждение финансов.",
        "scholarships": [
            "Czech Government Scholarship — для граждан отдельных стран (список уточняйте на msmt.cz).",
            "Стипендии вузов (Charles University, CTU, Masaryk University).",
            "Erasmus Mundus Joint Masters.",
            "Стипендии MŠMT для талантливых студентов магистратуры/PhD.",
        ],
        "universities": {
            "it": ["Czech Technical University (CTU) Prague", "Brno University of Technology", "VŠB-TU Ostrava"],
            "business": ["Prague University of Economics and Business (VŠE)", "Masaryk University", "Charles University"],
            "med": ["Charles University (1st–3rd Faculty of Medicine)", "Masaryk University", "Palacký University Olomouc"],
            "hum": ["Charles University", "Masaryk University", "Palacký University Olomouc"],
            "nat": ["Charles University", "Masaryk University", "University of Chemistry and Technology Prague"],
            "arts": ["UMPRUM Prague", "Academy of Fine Arts Prague (AVU)", "FAMU", "Brno University of Technology (FaVU)"],
        },
    },
    "pl": {
        "name": "🇵🇱 Польша",
        "climate": "moderate",
        "campus": "city",
        "english": 2,
        "tuition": (2000, 4500),
        "living": 650,
        "about": "Самая доступная страна в списке: невысокая оплата и недорогая жизнь, "
                 "много программ на английском, активные стипендиальные программы.",
        "deadlines": "Основной приём — до 31 мая – 30 июня (зимний семестр); некоторые вузы продлевают до сентября.",
        "visa": "Национальная виза D (студенческая), затем карта побыту; страховка и подтверждение средств.",
        "scholarships": [
            "NAWA — Polish Government Scholarships (программы Ignacy Łukasiewicz, Banach и др.).",
            "Стипендии вузов за достижения (до 100% оплаты в отдельных программах).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Warsaw University of Technology", "AGH Kraków", "Wrocław University of Science and Technology", "Gdańsk Tech"],
            "business": ["SGH Warsaw School of Economics", "Kozminski University", "Warsaw University"],
            "med": ["Medical University of Warsaw", "Jagiellonian University Medical College", "Medical University of Gdańsk", "Poznań University of Medical Sciences"],
            "hum": ["University of Warsaw", "Jagiellonian University", "Adam Mickiewicz University Poznań"],
            "nat": ["University of Warsaw", "Jagiellonian University", "Wrocław University"],
            "arts": ["Academy of Fine Arts Warsaw", "Jan Matejko Academy Kraków", "Academy of Fine Arts Gdańsk"],
        },
    },
    "ca": {
        "name": "🇨🇦 Канада",
        "climate": "cold",
        "campus": "campus",
        "english": 3,
        "tuition": (15000, 25000),
        "living": 1200,
        "about": "Классические кампусы, возможность работать во время учёбы и получить рабочую визу после выпуска. "
                 "Дорого, но много вузовских грантов; требуется английский (IELTS/TOEFL).",
        "deadlines": "Осенний набор: подача с октября по январь–март. Магистратура — декабрь–февраль.",
        "visa": "Study Permit; подтверждение финансов (≈ 20 600 CAD/год на жизнь + оплата за первый год), PAL/TAL от провинции.",
        "scholarships": [
            "Lester B. Pearson International Scholarship (University of Toronto) — полное покрытие.",
            "UBC International Major Entrance Scholarship, Karen McKellin Scholarship.",
            "Vanier Canada Graduate Scholarships — для PhD.",
            "Mitacs Globalink — исследовательские стажировки; entrance awards от McGill, Waterloo, McMaster и др.",
        ],
        "universities": {
            "it": ["University of Waterloo", "University of Toronto", "UBC", "McGill University"],
            "business": ["Rotman (UofT)", "Sauder (UBC)", "Schulich (York)", "Smith (Queen's)", "Ivey (Western)"],
            "med": ["University of Toronto", "McGill University", "UBC", "McMaster University"],
            "hum": ["University of Toronto", "McGill University", "UBC", "Queen's University"],
            "nat": ["University of Toronto", "UBC", "University of Alberta", "McMaster University"],
            "arts": ["OCAD University", "Emily Carr University", "NSCAD University", "Concordia University"],
        },
    },
    "fi": {
        "name": "🇫🇮 Финляндия",
        "climate": "cold",
        "campus": "campus",
        "english": 3,
        "tuition": (10000, 15000),
        "living": 900,
        "about": "Современные кампусы, высокий уровень образования и безопасности. "
                 "Для non-EU платное обучение, но есть много грантов; все магистратуры на английском.",
        "deadlines": "Совместный приём: бакалавриат — январь; магистратура — с декабря по январь. "
                     "Некоторые вузы — до 15 января.",
        "visa": "Residence permit for studies; подтверждение финансов (800 €/мес).",
        "scholarships": [
            "Aalto University Scholarship — частичное/полное покрытие оплаты.",
            "University of Helsinki Scholarship, Tampere University Scholarship, LUT Scholarship.",
            "Finland Scholarship — гранты для non-EU студентов.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Aalto University", "University of Helsinki", "Tampere University", "LUT University"],
            "business": ["Aalto University School of Business", "Hanken School of Economics", "University of Turku"],
            "med": ["University of Helsinki", "University of Turku", "University of Eastern Finland (для отдельных программ)"],
            "hum": ["University of Helsinki", "University of Turku", "University of Jyväskylä"],
            "nat": ["University of Helsinki", "University of Oulu", "University of Turku"],
            "arts": ["Aalto University (дизайн, архитектура, кино)", "Academy of Fine Arts, University of the Arts Helsinki"],
        },
    },
    "it": {
        "name": "🇮🇹 Италия",
        "climate": "warm",
        "campus": "city",
        "english": 2,
        "tuition": (1000, 4000),  # публичные вузы; зависит от дохода (ISEE)
        "living": 900,
        "about": "Тёплый климат, богатая культура, низкая оплата в публичных вузах. "
                 "Особенно сильны архитектура, дизайн, искусство, инженерия.",
        "deadlines": "Через Universitaly: предварительная регистрация с января – февраля до апреля – мая; "
                     "для non-EU — ранний срок (до апреля). Магистратура — февраль – март.",
        "visa": "Виза типа D (study), затем permesso di soggiorno; нужна Dichiarazione di Valore / CIMEA.",
        "scholarships": [
            "Invest Your Talent in Italy (MAECI) — для граждан отдельных стран.",
            "Региональные стипендии DSU (Lombardia, Lazio, Emilia-Romagna и др.) — жильё, питание, деньги.",
            "Университетские: Bocconi Merit Awards, Politecnico di Milano, University of Bologna Unibo Action 2.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Politecnico di Milano", "Politecnico di Torino", "University of Pisa", "Sapienza University of Rome"],
            "business": ["Bocconi University", "University of Bologna", "LUISS Rome", "Politecnico di Milano (MIP)"],
            "med": ["Sapienza University of Rome", "University of Bologna", "University of Padova", "Humanitas University"],
            "hum": ["University of Bologna", "Sapienza", "University of Florence", "Scuola Normale Superiore"],
            "nat": ["University of Padova", "Scuola Normale Superiore", "University of Pisa", "University of Milan"],
            "arts": ["Accademia di Belle Arti di Brera", "Politecnico di Milano (Design)", "NABA Milan", "Domus Academy"],
        },
    },
    "hu": {
        "name": "🇭🇺 Венгрия",
        "climate": "moderate",
        "campus": "both",
        "english": 2,
        "tuition": (3000, 8000),  # медицина ~ 12–16 тыс.
        "living": 600,
        "about": "Недорогая жизнь, сильная медицина на английском, одна из самых известных стипендиальных "
                 "программ для иностранцев (Stipendium Hungaricum).",
        "deadlines": "Stipendium Hungaricum: подача, как правило, до 15 января; обычный приём — "
                     "до 31 июля (иногда до сентября).",
        "visa": "Резидентский пермит для студентов; страховка, подтверждение жилья.",
        "scholarships": [
            "Stipendium Hungaricum — полное покрытие обучения + стипендия + жильё (для стран-партнёров).",
            "Tempus Public Foundation — Hungarian Government Scholarships.",
            "Университетские стипендии (BME, Semmelweis, Debrecen, Corvinus).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Budapest University of Technology (BME)", "Óbuda University", "University of Debrecen", "University of Szeged"],
            "business": ["Corvinus University of Budapest", "BME (Economics)", "University of Pécs"],
            "med": ["Semmelweis University", "University of Debrecen", "University of Szeged", "University of Pécs"],
            "hum": ["ELTE Budapest", "University of Szeged", "University of Debrecen"],
            "nat": ["ELTE Budapest", "University of Szeged", "University of Debrecen"],
            "arts": ["Moholy-Nagy University of Art and Design (MOME)", "Hungarian University of Fine Arts"],
        },
    },
    "es": {
        "name": "🇪🇸 Испания",
        "climate": "warm",
        "campus": "both",
        "english": 2,
        "tuition": (2000, 6000),  # публичные; частные (IE, ESADE) заметно дороже
        "living": 950,
        "about": "Тёплый климат, доступная оплата в публичных вузах и очень сильные бизнес-школы. "
                 "Много английских магистерских программ; бакалавриат чаще на испанском.",
        "deadlines": "Магистратура: подача с января по июнь (раунды). Бакалавриат: июнь – июль; "
                     "частные школы принимают круглогодично.",
        "visa": "Студенческая виза; гомологация аттестата; подтверждение финансов (~ 600 €/мес минимум).",
        "scholarships": [
            "Erasmus Mundus Joint Masters.",
            "Университетские: UPC Barcelona, Pompeu Fabra, University of Navarra и др.",
            "Fundación Carolina — главным образом для Латинской Америки.",
            "Гранты частных бизнес-школ (IE, ESADE, IESE) — merit-based.",
        ],
        "universities": {
            "it": ["UPC Barcelona (BarcelonaTech)", "UPM Madrid", "University of Navarra", "Universitat Pompeu Fabra"],
            "business": ["IE Business School", "ESADE", "IESE", "UPF Barcelona School of Management"],
            "med": ["University of Barcelona", "Complutense University Madrid", "University of Navarra", "University of Valencia"],
            "hum": ["University of Barcelona", "Complutense Madrid", "Autonomous University of Madrid"],
            "nat": ["University of Barcelona", "Autonomous University of Barcelona (UAB)", "University of Valencia"],
            "arts": ["Elisava Barcelona", "IED Madrid", "Complutense (Fine Arts)", "Universidad Politécnica de Valencia"],
        },
    },
}

CLIMATE_LABEL = {"warm": "☀️ тёплый", "moderate": "🌤 умеренный", "cold": "❄️ холодный"}
CAMPUS_LABEL = {"campus": "кампусный", "city": "городской", "both": "кампусный и городской"}


# ----------------------------------------------------------------------------
# Подключаем остальные страны ЕС и Азии
# ----------------------------------------------------------------------------
from bott.data_more import MORE_COUNTRIES  # noqa: E402

COUNTRIES.update(MORE_COUNTRIES)

# Регионы для навигации по списку (название, коды стран)
REGIONS = {
    "west": ("🇪🇺 Западная Европа", ["de", "nl", "be", "lu", "fr", "at", "ie"]),
    "north": ("🇪🇺 Северная Европа", ["se", "dk", "fi", "ee", "lv", "lt"]),
    "south": ("🇪🇺 Южная Европа", ["it", "es", "pt", "gr", "mt", "cy", "hr", "si"]),
    "east": ("🇪🇺 Центральная и Восточная Европа", ["cz", "pl", "hu", "sk", "ro", "bg"]),
    "asia": ("🌏 Азия", ["jp", "kr", "cn", "tw", "hk", "sg", "my", "th", "in", "tr", "ae", "kz", "ge"]),
    "na": ("🌎 Северная Америка", ["ca"]),
}

# Крупная группа для вопроса «какой регион рассматриваете»: eu / asia / na
REGION_GROUP = {}
for _key, (_title, _codes) in REGIONS.items():
    for _code in _codes:
        REGION_GROUP[_code] = "asia" if _key == "asia" else ("na" if _key == "na" else "eu")


from data_career import CAREER, MENTALITY_LABEL  # noqa: E402,F401
