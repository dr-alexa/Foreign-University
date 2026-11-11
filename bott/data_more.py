"""
Дополнительные страны: оставшиеся члены ЕС (19) и страны Азии (13).
Формат такой же, как в data.py. Цены — ориентировочные, в евро, для студентов не из ЕС.
Перед публикацией бота сверьте всё с официальными сайтами вузов и программ.
"""

EU_MORE = {
    "at": {
        "name": "🇦🇹 Австрия", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (1450, 1500), "living": 1000,
        "about": "Низкая оплата в государственных вузах (около 726 € за семестр для non-EU), высокое качество жизни, "
                 "сильные технические и медицинские факультеты. Бакалавриат в основном на немецком, магистратура часто на английском.",
        "deadlines": "Non-EU: зимний семестр — до 1 сентября (часто до 5 сентября), летний — до 1 февраля; "
                     "медицина — раньше (регистрация на MedAT в феврале–марте).",
        "visa": "Студенческий вид на жительство; подтверждение финансов (~ 1 100 €/мес), страховка, знание немецкого B2 для немецких программ.",
        "scholarships": [
            "OeAD — Ernst Mach Grant (магистры, PhD, исследователи).",
            "Erasmus Mundus Joint Masters.",
            "Стипендии вузов (TU Wien, University of Vienna, MCI) — частичное покрытие.",
        ],
        "universities": {
            "it": ["TU Wien", "TU Graz", "JKU Linz", "University of Innsbruck"],
            "business": ["WU Vienna", "University of Vienna", "MCI Innsbruck", "JKU Linz"],
            "med": ["MedUni Wien", "MedUni Graz", "MedUni Innsbruck", "Paracelsus Medical University Salzburg"],
            "hum": ["University of Vienna", "University of Graz", "University of Innsbruck", "University of Salzburg"],
            "nat": ["University of Vienna", "University of Innsbruck", "University of Graz", "BOKU Vienna"],
            "arts": ["University of Applied Arts Vienna", "Academy of Fine Arts Vienna", "University of Music and Performing Arts Vienna", "Mozarteum Salzburg"],
        },
    },
    "be": {
        "name": "🇧🇪 Бельгия", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (1000, 7000), "living": 1000,
        "about": "Высокий уровень вузов (KU Leuven — один из сильнейших в Европе), мультиязычная среда, "
                 "оплата зависит от региона (Фландрия / Валлония) и программы.",
        "deadlines": "Non-EU: чаще всего 1 февраля – 1 марта (KU Leuven, Ghent); Валлония — до 30 апреля – 31 мая.",
        "visa": "Студенческая виза D; подтверждение финансов (~ 800–900 €/мес), страховка, апостиль.",
        "scholarships": [
            "VLIR-UOS (Фландрия) — для студентов из развивающихся стран.",
            "ARES (Валлония) — гранты на магистратуру и PhD.",
            "KU Leuven Science@Leuven, Ghent University Special Research Fund.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["KU Leuven", "Ghent University", "UCLouvain", "Vrije Universiteit Brussel (VUB)"],
            "business": ["KU Leuven", "Vlerick Business School", "Solvay Brussels School (ULB)", "University of Antwerp"],
            "med": ["KU Leuven", "Ghent University", "UCLouvain", "ULB"],
            "hum": ["KU Leuven", "Ghent University", "ULB", "University of Antwerp"],
            "nat": ["KU Leuven", "Ghent University", "VUB", "University of Liège"],
            "arts": ["LUCA School of Arts", "KASK & Conservatorium Ghent", "Royal Academy of Fine Arts Antwerp", "La Cambre Brussels"],
        },
    },
    "bg": {
        "name": "🇧🇬 Болгария", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (3000, 8000), "living": 500,
        "about": "Очень недорогая жизнь, обучение на английском в медицинских вузах и несколько сильных университетов. "
                 "Хороший вариант для бюджетного старта в ЕС.",
        "deadlines": "Приём документов обычно с апреля по сентябрь; медицина — до июля–августа.",
        "visa": "Виза типа D; нострификация аттестата; подтверждение финансов; медицинские документы.",
        "scholarships": [
            "Стипендии правительства Болгарии (в основном для болгар по происхождению и отдельных стран).",
            "Erasmus Mundus Joint Masters.",
            "Университетские скидки для отличников (Sofia University, Medical University of Sofia).",
        ],
        "universities": {
            "it": ["Sofia University", "Technical University of Sofia", "American University in Bulgaria"],
            "business": ["UNWE Sofia", "Sofia University", "American University in Bulgaria"],
            "med": ["Medical University of Sofia", "Medical University of Plovdiv", "Medical University of Varna", "Medical University of Pleven"],
            "hum": ["Sofia University", "American University in Bulgaria", "Veliko Tarnovo University"],
            "nat": ["Sofia University", "University of Chemical Technology and Metallurgy"],
            "arts": ["National Academy of Art Sofia", "New Bulgarian University", "NATFA Sofia"],
        },
    },
    "hr": {
        "name": "🇭🇷 Хорватия", "climate": "warm", "campus": "city", "english": 1,
        "tuition": (1000, 5000), "living": 650,
        "about": "Адриатическое побережье, недорогая жизнь, постепенно растущий выбор программ на английском. "
                 "Лучше всего подходит тем, кто готов учить хорватский или выбирает магистратуру.",
        "deadlines": "Приём обычно с июня по сентябрь; магистратура — до 30 июня – 15 сентября.",
        "visa": "Временное проживание для студентов; страховка и подтверждение жилья и средств.",
        "scholarships": [
            "Стипендии Министерства науки и образования Хорватии для иностранцев (отдельные программы).",
            "Erasmus Mundus Joint Masters.",
            "Стипендии вузов (University of Zagreb, Rijeka, Split).",
        ],
        "universities": {
            "it": ["University of Zagreb (FER)", "University of Split", "University of Rijeka", "University of Osijek"],
            "business": ["University of Zagreb (FEB)", "Zagreb School of Economics and Management", "University of Rijeka"],
            "med": ["University of Zagreb School of Medicine", "University of Split School of Medicine", "University of Rijeka"],
            "hum": ["University of Zagreb", "University of Zadar", "University of Rijeka"],
            "nat": ["University of Zagreb (PMF)", "University of Split", "University of Osijek"],
            "arts": ["Academy of Fine Arts Zagreb", "Academy of Dramatic Art Zagreb", "Arts Academy Split"],
        },
    },
    "cy": {
        "name": "🇨🇾 Кипр", "climate": "warm", "campus": "both", "english": 3,
        "tuition": (4000, 12000), "living": 800,
        "about": "Тёплый климат, обучение на английском и дружелюбная среда. Много частных вузов, "
                 "приём гибкий, нередко без сложных вступительных испытаний.",
        "deadlines": "Приём rolling (в течение года); на осенний семестр — обычно до июля–августа.",
        "visa": "Студенческая виза/permit; страховка, подтверждение финансов, часто нужен медосмотр.",
        "scholarships": [
            "Merit scholarships от университетов (University of Nicosia, European University Cyprus).",
            "University of Cyprus — стипендии магистрам и PhD.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["University of Cyprus", "Cyprus University of Technology", "University of Nicosia", "Frederick University"],
            "business": ["University of Cyprus", "University of Nicosia", "European University Cyprus", "Neapolis University Pafos"],
            "med": ["University of Nicosia Medical School", "European University Cyprus", "University of Cyprus (Medical School)"],
            "hum": ["University of Cyprus", "Open University of Cyprus", "University of Nicosia"],
            "nat": ["University of Cyprus", "Cyprus University of Technology"],
            "arts": ["University of Nicosia (Art & Design)", "Frederick University", "Cyprus University of Technology (Multimedia & Graphic Arts)"],
        },
    },
    "dk": {
        "name": "🇩🇰 Дания", "climate": "cold", "campus": "city", "english": 3,
        "tuition": (6000, 16000), "living": 1200,
        "about": "Практикоориентированное обучение, дизайн, инженерия, высокий уровень жизни. "
                 "Для non-EU обучение платное, но программы полностью на английском.",
        "deadlines": "Non-EU: магистратура — до 15 января; бакалавриат — до 15 марта.",
        "visa": "Residence permit for studies; подтверждение финансов (~ 900–1 000 €/мес).",
        "scholarships": [
            "Danish Government Scholarships — для отдельных стран.",
            "DTU Scholarship, Copenhagen Master's Scholarship (University of Copenhagen), Aarhus Excellence.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["DTU", "University of Copenhagen", "Aalborg University", "IT University of Copenhagen"],
            "business": ["Copenhagen Business School", "Aarhus University (BSS)", "University of Southern Denmark"],
            "med": ["University of Copenhagen", "Aarhus University", "University of Southern Denmark", "Aalborg University"],
            "hum": ["University of Copenhagen", "Aarhus University", "Roskilde University"],
            "nat": ["University of Copenhagen", "Aarhus University", "DTU", "University of Southern Denmark"],
            "arts": ["KADK (Royal Danish Academy)", "Design School Kolding", "Danish Film School", "Aarhus School of Architecture"],
        },
    },
    "ee": {
        "name": "🇪🇪 Эстония", "climate": "cold", "campus": "both", "english": 3,
        "tuition": (2000, 6000), "living": 700,
        "about": "Цифровая страна: сильные IT-программы, простое взаимодействие с госорганами, английский повсеместен. "
                 "Тарту — классический студенческий город, Таллин — технологический хаб.",
        "deadlines": "Обычно 15 января – 15 апреля (зависит от вуза и программы); магистратура — до 1 февраля – 15 апреля.",
        "visa": "Temporary residence permit for study; страховка, подтверждение финансов (~ 650–700 €/мес).",
        "scholarships": [
            "Dora Plus — гранты для международных студентов.",
            "Estonian Government Scholarships (для отдельных стран).",
            "University of Tartu и TalTech — merit-based стипендии.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["TalTech", "University of Tartu", "Tallinn University", "Estonian Entrepreneurship University of Applied Sciences"],
            "business": ["TalTech (School of Business)", "University of Tartu", "Estonian Business School"],
            "med": ["University of Tartu (Faculty of Medicine)", "Tallinn Health Care College", "TalTech (Biomedical Engineering)"],
            "hum": ["University of Tartu", "Tallinn University", "Estonian Academy of Security Sciences"],
            "nat": ["University of Tartu", "TalTech", "Estonian University of Life Sciences"],
            "arts": ["Estonian Academy of Arts", "Tallinn University (Baltic Film and Media School)", "University of Tartu Viljandi Culture Academy"],
        },
    },
    "fr": {
        "name": "🇫🇷 Франция", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (2800, 3800), "living": 1100,
        "about": "Низкая оплата в государственных вузах для non-EU (около 2 770 € на бакалавриате и 3 770 € в магистратуре), "
                 "много стипендий, престижные «гранд-эколь». Для бакалавриата нужен французский (B2–C1).",
        "deadlines": "Études en France: с октября по январь–март; Parcoursup (для проживающих во Франции) — январь–март; "
                     "Eiffel Scholarship — в январе.",
        "visa": "Long-stay student visa (VLS-TS); подтверждение финансов (615 €/мес), страховка, CAMPUSFRANCE.",
        "scholarships": [
            "Eiffel Excellence Scholarship — для магистров и PhD (покрывает проживание + 1 181 €/мес).",
            "Campus France / Régions — региональные стипендии.",
            "Emile Boutmy (Sciences Po), IDEX scholarships (Paris-Saclay, PSL).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["École Polytechnique", "CentraleSupélec", "Sorbonne University", "Paris-Saclay University", "INSA Lyon"],
            "business": ["HEC Paris", "ESSEC", "ESCP Business School", "PSL – Dauphine", "Sciences Po"],
            "med": ["Sorbonne University", "Université Paris Cité", "Aix-Marseille University", "Université Claude Bernard Lyon 1"],
            "hum": ["Sorbonne University", "PSL – ENS", "Sciences Po", "Paris 1 Panthéon-Sorbonne"],
            "nat": ["Paris-Saclay University", "Sorbonne University", "PSL (ENS, ESPCI)", "Université Grenoble Alpes"],
            "arts": ["ENSAD", "ENSBA Paris", "Strate School of Design", "École Duperré", "Gobelins"],
        },
    },
    "gr": {
        "name": "🇬🇷 Греция", "climate": "warm", "campus": "city", "english": 2,
        "tuition": (0, 4000), "living": 700,
        "about": "Тёплый климат, дешёвая жизнь, бесплатный бакалавриат в государственных вузах (на греческом), "
                 "магистратуры на английском чаще платные. Сильные архитектура, археология, морские науки.",
        "deadlines": "Магистратура: обычно с марта по июнь; бакалавриат (для иностранцев): июль–сентябрь.",
        "visa": "Национальная виза D для студентов; страховка; подтверждение жилья и средств.",
        "scholarships": [
            "IKY — Greek State Scholarships Foundation (программы для иностранцев).",
            "Erasmus Mundus Joint Masters.",
            "Стипендии вузов и фондов (например, Onassis Foundation — в основном для греков и исследователей).",
        ],
        "universities": {
            "it": ["NTUA (National Technical University of Athens)", "Aristotle University of Thessaloniki", "University of Patras", "Technical University of Crete"],
            "business": ["Athens University of Economics and Business", "University of Macedonia", "Panteion University"],
            "med": ["University of Athens (NKUA)", "Aristotle University of Thessaloniki", "University of Crete", "University of Patras"],
            "hum": ["University of Athens", "Aristotle University", "University of Crete", "Panteion University"],
            "nat": ["University of Athens", "Aristotle University", "University of Crete"],
            "arts": ["Athens School of Fine Arts", "Aristotle University (Fine Arts)", "University of the Aegean (Design)"],
        },
    },
    "ie": {
        "name": "🇮🇪 Ирландия", "climate": "moderate", "campus": "both", "english": 3,
        "tuition": (12000, 25000), "living": 1300,
        "about": "Английский как родной, сильные IT и биотех-компании (Google, Meta, Pfizer), "
                 "возможность остаться работать после выпуска (Stamp 1G).",
        "deadlines": "Бакалавриат: CAO — до 1 февраля; магистратура: подача через PAC/вуз до июля; "
                     "GOI-IES — обычно февраль–март.",
        "visa": "Student visa/IRP; подтверждение финансов (10 000 €), оплата курса, страховка.",
        "scholarships": [
            "Government of Ireland International Education Scholarship (GOI-IES) — 10 000 € + оплата обучения.",
            "Trinity Global Excellence, UCD Global Excellence Scholarships.",
            "Walsh Scholarships (Teagasc) — агро и науки о питании.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Trinity College Dublin", "University College Dublin", "Dublin City University", "University of Limerick"],
            "business": ["Trinity Business School", "UCD Smurfit School", "University of Galway", "Dublin City University"],
            "med": ["Trinity College Dublin", "RCSI", "University College Dublin", "University College Cork"],
            "hum": ["Trinity College Dublin", "UCD", "University College Cork", "University of Galway"],
            "nat": ["Trinity College Dublin", "UCD", "University College Cork", "Maynooth University"],
            "arts": ["NCAD Dublin", "Dún Laoghaire Institute (IADT)", "TU Dublin (Design)", "Crawford College of Art and Design"],
        },
    },
    "lv": {
        "name": "🇱🇻 Латвия", "climate": "cold", "campus": "city", "english": 2,
        "tuition": (2500, 7000), "living": 650,
        "about": "Недорогая учёба и жизнь в Прибалтике, медицина на английском (Рижский университет Страдиня), "
                 "хорошие IT и международные бизнес-программы.",
        "deadlines": "Обычно с января по июнь–июль; медицина — до июля.",
        "visa": "Student residence permit; подтверждение средств (~ 600–700 €/мес) и страховка.",
        "scholarships": [
            "Латвийские государственные стипендии для иностранцев (по межправсоглашениям).",
            "Стипендии вузов (RTU, RSU, University of Latvia).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Riga Technical University (RTU)", "University of Latvia", "Riga Business School (RTU)"],
            "business": ["RISEBA", "Stockholm School of Economics in Riga", "University of Latvia", "Riga Business School"],
            "med": ["Riga Stradiņš University (RSU)", "University of Latvia (Faculty of Medicine)"],
            "hum": ["University of Latvia", "Riga Graduate School of Law", "Vidzeme University"],
            "nat": ["University of Latvia", "Riga Technical University", "Latvia University of Life Sciences"],
            "arts": ["Art Academy of Latvia", "Latvian Academy of Culture", "Riga Technical University (Design)"],
        },
    },
    "lt": {
        "name": "🇱🇹 Литва", "climate": "cold", "campus": "city", "english": 2,
        "tuition": (3000, 6000), "living": 600,
        "about": "Недорогая и безопасная страна; английские программы по IT, бизнесу и медицине. "
                 "Вильнюс — столица стартапов и финтеха.",
        "deadlines": "Обычно до 1 июня – 15 июля (осенний набор); некоторые вузы — до сентября.",
        "visa": "National visa/Temporary residence permit; страховка и подтверждение средств.",
        "scholarships": [
            "Lithuanian State Scholarship для иностранцев (по межправсоглашениям).",
            "Стипендии вузов (Vilnius University, KTU, ISM).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Vilnius University", "Kaunas University of Technology (KTU)", "Vilnius Tech", "Vytautas Magnus University"],
            "business": ["ISM University of Management and Economics", "Vilnius University (VU BS)", "KTU School of Economics and Business"],
            "med": ["Lithuanian University of Health Sciences", "Vilnius University (Faculty of Medicine)"],
            "hum": ["Vilnius University", "Vytautas Magnus University", "LCC International University"],
            "nat": ["Vilnius University", "Kaunas University of Technology", "Lithuanian University of Health Sciences"],
            "arts": ["Vilnius Academy of Arts", "Lithuanian Academy of Music and Theatre", "Vilnius Tech (Architecture)"],
        },
    },
    "lu": {
        "name": "🇱🇺 Люксембург", "climate": "moderate", "campus": "campus", "english": 3,
        "tuition": (400, 900), "living": 1500,
        "about": "Единственный государственный университет с многоязычными программами (EN/FR/DE), "
                 "один из самых высоких уровней жизни в Европе, сильные финансы и IT. Самая дорогая жизнь в списке.",
        "deadlines": "Бакалавриат: до 31 мая; магистратура: до 15 мая – 1 июня; PhD — по вакансиям.",
        "visa": "Student visa/authorisation of stay; подтверждение финансов (~ 1 000–1 300 €/мес).",
        "scholarships": [
            "Erasmus Mundus Joint Masters.",
            "FNR AFR — PhD-гранты в университете.",
            "Стипендии University of Luxembourg (merit/needs-based) — ограничены.",
        ],
        "universities": {
            "it": ["University of Luxembourg (Computer Science, SnT)"],
            "business": ["University of Luxembourg (Finance, Economics, Law)", "Luxembourg School of Business (частная)"],
            "med": ["University of Luxembourg (первый год Bachelor in Medicine; дальше — за рубежом)"],
            "hum": ["University of Luxembourg (Cultural Sciences, Politics)"],
            "nat": ["University of Luxembourg (Physics, Life Sciences)"],
            "arts": ["Профильных вузов нет — смотрите Бельгию, Францию, Германию"],
        },
    },
    "mt": {
        "name": "🇲🇹 Мальта", "climate": "warm", "campus": "campus", "english": 3,
        "tuition": (5000, 12000), "living": 1000,
        "about": "Средиземноморский климат, английский — официальный язык, компактный кампус University of Malta. "
                 "Подходит для курсов по гейм-индустрии, финансам, туризму.",
        "deadlines": "Приём на октябрь: подача до марта–мая; MCAST — до июля.",
        "visa": "Student visa/residence permit; подтверждение финансов (~ 800–1 000 €/мес), страховка.",
        "scholarships": [
            "Erasmus Mundus Joint Masters.",
            "Commonwealth Shared Scholarship (для отдельных стран).",
            "Стипендии вуза и MCAST — ограничены.",
        ],
        "universities": {
            "it": ["University of Malta (ICT)", "MCAST (ICT)", "Malta College of Arts, Science and Technology"],
            "business": ["University of Malta (EMA)", "MCAST", "Institute of Tourism Studies"],
            "med": ["University of Malta (Medicine & Surgery)"],
            "hum": ["University of Malta (Arts)", "University of Malta (Education)"],
            "nat": ["University of Malta (Science)"],
            "arts": ["MCAST (Institute of Creative Arts)", "University of Malta (Built Environment & Design)"],
        },
    },
    "pt": {
        "name": "🇵🇹 Португалия", "climate": "warm", "campus": "city", "english": 2,
        "tuition": (3000, 7000), "living": 850,
        "about": "Тёплая и безопасная страна, недорогая жизнь, популярна среди иностранных студентов. "
                 "Сильные инженерные вузы, бизнес-школа Nova SBE, гибкий вид на жительство.",
        "deadlines": "Международный конкурс: несколько этапов с февраля по июль; магистратура — до июля.",
        "visa": "Student visa; подтверждение финансов (~ 760 €/мес), страховка, жильё.",
        "scholarships": [
            "Erasmus Mundus Joint Masters.",
            "Camões Institute — для студентов из португалоязычных стран.",
            "Стипендии University of Porto, University of Lisbon, Nova SBE.",
            "Calouste Gulbenkian Foundation (отдельные программы).",
        ],
        "universities": {
            "it": ["Instituto Superior Técnico (Lisbon)", "University of Porto", "University of Minho", "University of Coimbra"],
            "business": ["Nova SBE", "Católica Lisbon", "ISEG (University of Lisbon)", "University of Porto (FEP)"],
            "med": ["University of Lisbon (FMUL)", "University of Porto (ICBAS/FMUP)", "University of Coimbra", "Nova Medical School"],
            "hum": ["University of Lisbon", "University of Coimbra", "Nova FCSH", "University of Porto"],
            "nat": ["University of Lisbon", "University of Porto", "University of Aveiro", "Nova FCT"],
            "arts": ["FBAUP Porto", "ESAD Caldas da Rainha", "IADE Lisbon", "ESAD.CR"],
        },
    },
    "ro": {
        "name": "🇷🇴 Румыния", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (2500, 8000), "living": 550,
        "about": "Одна из самых недорогих стран ЕС, сильная медицина на английском (Carol Davila, Cluj), "
                 "хорошие технические вузы.",
        "deadlines": "Non-EU: приём на подготовительный год/бакалавриат — до июля–сентября; медицина — до июля.",
        "visa": "Letter of acceptance от Министерства образования, затем student visa; нострификация аттестата.",
        "scholarships": [
            "Румынские правительственные стипендии для non-EU студентов (через Министерство образования).",
            "Erasmus Mundus Joint Masters.",
            "Университетские стипендии (Babeș-Bolyai, UPB).",
        ],
        "universities": {
            "it": ["Politehnica University of Bucharest", "Babeș-Bolyai University", "Technical University of Cluj-Napoca"],
            "business": ["Bucharest University of Economic Studies (ASE)", "Babeș-Bolyai University", "Alexandru Ioan Cuza University"],
            "med": ["Carol Davila University of Medicine and Pharmacy", "Iuliu Hațieganu (Cluj-Napoca)", "UMF Timișoara", "UMF Iași"],
            "hum": ["University of Bucharest", "Babeș-Bolyai University", "Alexandru Ioan Cuza University"],
            "nat": ["University of Bucharest", "Babeș-Bolyai University", "University of Timișoara"],
            "arts": ["National University of Arts Bucharest (UNArte)", "UAUIM Bucharest (Architecture)", "George Enescu University of Arts Iași"],
        },
    },
    "sk": {
        "name": "🇸🇰 Словакия", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (2000, 9000), "living": 600,
        "about": "На словацком обучение бесплатное, на английском — платное. Недорогая жизнь, медицина на английском, "
                 "удобное расположение рядом с Веной и Будапештом.",
        "deadlines": "Обычно до 30 апреля – 30 июня; медицина — до 30 апреля (часто вступительные экзамены).",
        "visa": "Временное проживание для студентов; страховка, подтверждение средств, нострификация.",
        "scholarships": [
            "SAIA — Национальная стипендиальная программа для иностранцев.",
            "Slovak Government Scholarships (для отдельных стран).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["Slovak University of Technology (STU)", "Technical University of Košice", "Comenius University (Informatics)"],
            "business": ["University of Economics in Bratislava", "Comenius University (Management)", "Matej Bel University"],
            "med": ["Comenius University (Bratislava)", "Jessenius Faculty of Medicine", "UPJŠ Košice"],
            "hum": ["Comenius University", "Constantine the Philosopher University", "Matej Bel University"],
            "nat": ["Comenius University", "UPJŠ Košice", "STU (Chemical and Food Technology)"],
            "arts": ["Academy of Fine Arts and Design (VŠVU)", "VŠMU Bratislava (Performing Arts)", "Academy of Arts Banská Bystrica"],
        },
    },
    "si": {
        "name": "🇸🇮 Словения", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (2000, 8000), "living": 800,
        "about": "Небольшая и безопасная страна, природа Альп и Адриатики, недорогое образование на словенском. "
                 "Магистерские программы на английском доступнее бакалаврских.",
        "deadlines": "Non-EU: подача до 1 марта – 30 апреля; на английском — иногда до июля.",
        "visa": "Residence permit for studies; страховка, подтверждение средств (~ 500–600 €/мес).",
        "scholarships": [
            "Стипендии Республики Словения для иностранцев (Ad Futura).",
            "CEEPUS — обменные программы (для отдельных стран).",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["University of Ljubljana (FRI/FE)", "University of Maribor", "University of Primorska", "University of Nova Gorica"],
            "business": ["University of Ljubljana (EF)", "University of Maribor (EPF)", "IEDC-Bled School of Management"],
            "med": ["University of Ljubljana (Medicine)", "University of Maribor (Medicine)"],
            "hum": ["University of Ljubljana", "University of Maribor", "University of Primorska"],
            "nat": ["University of Ljubljana", "University of Nova Gorica", "University of Maribor"],
            "arts": ["Academy of Fine Arts and Design (ALUO) Ljubljana", "Academy of Music Ljubljana", "AGRFT Ljubljana"],
        },
    },
    "se": {
        "name": "🇸🇪 Швеция", "climate": "cold", "campus": "both", "english": 3,
        "tuition": (8000, 18000), "living": 1000,
        "about": "Свободное общение на английском, инновационная среда, сильные инженерные и медицинские вузы "
                 "(KTH, Karolinska, Chalmers). Для non-EU платно, но много стипендий.",
        "deadlines": "universityadmissions.se: подача на осень — с 15 октября по 15 января; "
                     "стипендия Swedish Institute — как правило, до февраля.",
        "visa": "Residence permit for studies; подтверждение финансов (~ 1 000 €/мес), страховка.",
        "scholarships": [
            "Swedish Institute Scholarships (SISGP, SISS) — для магистров из отдельных стран.",
            "Lund University Global Scholarship, KTH Scholarship, Chalmers IPOET.",
            "Erasmus Mundus Joint Masters.",
        ],
        "universities": {
            "it": ["KTH Royal Institute of Technology", "Chalmers University of Technology", "Linköping University", "Lund University"],
            "business": ["Stockholm School of Economics", "Lund University School of Economics", "Gothenburg School of Business"],
            "med": ["Karolinska Institutet", "Uppsala University", "Lund University", "University of Gothenburg"],
            "hum": ["Uppsala University", "Lund University", "Stockholm University", "University of Gothenburg"],
            "nat": ["Uppsala University", "Stockholm University", "Lund University", "KTH"],
            "arts": ["Konstfack", "KTH (Architecture)", "Umeå Institute of Design", "Beckmans College of Design"],
        },
    },
}

ASIA = {
    "jp": {
        "name": "🇯🇵 Япония", "climate": "moderate", "campus": "both", "english": 2,
        "tuition": (3500, 8000), "living": 900,
        "about": "Технологичная и безопасная страна, сильные инженерные вузы и научные центры. "
                 "Много английских программ в рамках «Global 30» и магистратуры, бакалавриат часто на японском (JLPT N1–N2).",
        "deadlines": "MEXT: апрель–июнь (через посольство); вузы: весенний набор — осенью, осенний — до весны.",
        "visa": "Student visa; Certificate of Eligibility (COE) от вуза; подтверждение финансов.",
        "scholarships": [
            "MEXT (Monbukagakusho) — полное покрытие + ежемесячная стипендия.",
            "JASSO — стипендии для иностранных студентов.",
            "University scholarships: UTokyo Fellowships, Waseda, Keio, Kyoto University.",
        ],
        "universities": {
            "it": ["University of Tokyo", "Kyoto University", "Institute of Science Tokyo", "Osaka University"],
            "business": ["Hitotsubashi University", "Waseda University", "Keio University", "GRIPS (Policy Studies)"],
            "med": ["University of Tokyo", "Kyoto University", "Osaka University", "Keio University"],
            "hum": ["University of Tokyo", "Kyoto University", "Waseda University", "Sophia University"],
            "nat": ["University of Tokyo", "Kyoto University", "Tohoku University", "Nagoya University"],
            "arts": ["Tokyo University of the Arts (Geidai)", "Musashino Art University", "Tama Art University", "Kyoto Seika University"],
        },
    },
    "kr": {
        "name": "🇰🇷 Южная Корея", "climate": "moderate", "campus": "campus", "english": 2,
        "tuition": (3000, 7500), "living": 950,
        "about": "Лидер в электронике, ИИ и креативных индустриях. Мощные кампусные университеты, "
                 "много стипендий (GKS), английские программы чаще в магистратуре.",
        "deadlines": "GKS: февраль–март (embassy track) / сентябрь–октябрь; вузы: весенний набор — осенью, осенний — апрель–июнь.",
        "visa": "D-2 (student visa); подтверждение средств; TOPIK для корейских программ.",
        "scholarships": [
            "GKS (Global Korea Scholarship) — полное обучение, жильё, стипендия, язык.",
            "SNU, KAIST, Yonsei, Korea University — merit/need-based гранты.",
            "KOICA — для студентов из отдельных стран.",
        ],
        "universities": {
            "it": ["KAIST", "Seoul National University", "POSTECH", "Hanyang University"],
            "business": ["Seoul National University (Business)", "Yonsei University", "Korea University", "SKKU"],
            "med": ["Seoul National University", "Yonsei University (Severance)", "Korea University"],
            "hum": ["Seoul National University", "Yonsei", "Korea University", "Ewha Womans University"],
            "nat": ["KAIST", "SNU", "POSTECH", "UNIST"],
            "arts": ["Korea National University of Arts", "Hongik University (Design)", "Kookmin University", "SNU (Fine Arts)"],
        },
    },
    "cn": {
        "name": "🇨🇳 Китай", "climate": "moderate", "campus": "campus", "english": 2,
        "tuition": (2500, 7000), "living": 600,
        "about": "Огромные кампусы, доступная стоимость жизни, мощная наука и инженерия. "
                 "Английские программы чаще на магистратуре и в медицине, для бакалавров — китайский HSK 4–5.",
        "deadlines": "CSC: январь–апрель; прямая подача в вузы: март–июнь на сентябрьский набор.",
        "visa": "X1 (long-term study); подтверждение финансов; медосмотр; JW201/JW202 от вуза.",
        "scholarships": [
            "CSC (Chinese Government Scholarship) — полное покрытие + стипендия.",
            "Confucius Institute Scholarship; Silk Road Scholarship.",
            "Schwarzman Scholars (Tsinghua), Yenching Academy (Peking University).",
            "Beijing/Shanghai Government Scholarships; университетские гранты.",
        ],
        "universities": {
            "it": ["Tsinghua University", "Peking University", "Shanghai Jiao Tong University", "Zhejiang University", "USTC"],
            "business": ["Tsinghua SEM", "Peking University (Guanghua)", "Fudan University", "CEIBS"],
            "med": ["Peking University Health Science Center", "Fudan (Shanghai Medical College)", "Zhejiang University", "Sun Yat-sen University"],
            "hum": ["Peking University", "Fudan University", "Renmin University", "Beijing Normal University"],
            "nat": ["USTC", "Tsinghua University", "Peking University", "Zhejiang University"],
            "arts": ["China Academy of Art", "Central Academy of Fine Arts (CAFA)", "Tsinghua Academy of Arts & Design"],
        },
    },
    "tw": {
        "name": "🇹🇼 Тайвань", "climate": "warm", "campus": "both", "english": 2,
        "tuition": (2500, 4500), "living": 650,
        "about": "Недорогая учёба, мощные технологии (полупроводники), безопасные города и хорошие стипендии. "
                 "Английские программы — в основном в магистратуре и PhD.",
        "deadlines": "Taiwan Scholarship: февраль–март; прямая подача в вузы: январь–апрель.",
        "visa": "Resident visa for study; подтверждение финансов; нотариальные копии документов.",
        "scholarships": [
            "Taiwan Scholarship (MOFA) — для студентов и PhD.",
            "MOE Taiwan Scholarship Program, ICDF Scholarship.",
            "University scholarships (NTU, NTHU, NCKU) — merit-based.",
        ],
        "universities": {
            "it": ["National Taiwan University", "National Tsing Hua University", "National Yang Ming Chiao Tung University", "NCKU"],
            "business": ["National Taiwan University (College of Management)", "National Chengchi University", "NTUST"],
            "med": ["National Taiwan University", "National Yang Ming Chiao Tung University", "Taipei Medical University"],
            "hum": ["National Taiwan University", "National Chengchi University", "National Tsing Hua University"],
            "nat": ["NTU", "NTHU", "NCKU", "Academia Sinica (Graduate Institutes)"],
            "arts": ["Taipei National University of the Arts", "National Taiwan University of Arts", "Shih Chien University"],
        },
    },
    "hk": {
        "name": "🇭🇰 Гонконг", "climate": "warm", "campus": "campus", "english": 3,
        "tuition": (12000, 18000), "living": 1300,
        "about": "Международный финансовый хаб, английский — язык обучения, несколько вузов из топ-100 мира. "
                 "Дорого, но много стипендий и PhD-фелловшипов.",
        "deadlines": "Бакалавриат: ноябрь–март; магистратура: ноябрь–март; HKPFS (PhD): 1 декабря.",
        "visa": "Student visa/permit; подтверждение финансов; письмо о зачислении.",
        "scholarships": [
            "Hong Kong PhD Fellowship Scheme (HKPFS).",
            "Hong Kong Scholarship for Excellence Scheme; Belt and Road Scholarship.",
            "Entrance scholarships HKU, HKUST, CUHK, CityU, PolyU.",
        ],
        "universities": {
            "it": ["HKUST", "University of Hong Kong (HKU)", "CUHK", "CityU Hong Kong"],
            "business": ["HKUST Business School", "HKU Business School", "CUHK Business School", "PolyU (Business)"],
            "med": ["HKU (LKS Faculty of Medicine)", "CUHK Faculty of Medicine"],
            "hum": ["HKU", "CUHK", "HKBU", "Lingnan University"],
            "nat": ["HKU", "HKUST", "CUHK", "CityU"],
            "arts": ["PolyU School of Design", "Hong Kong Academy for Performing Arts", "HKBU Academy of Visual Arts", "CUHK Fine Arts"],
        },
    },
    "sg": {
        "name": "🇸🇬 Сингапур", "climate": "warm", "campus": "campus", "english": 3,
        "tuition": (12000, 25000), "living": 1500,
        "about": "Один из лучших вузов Азии (NUS, NTU), английский язык, безопасность и доступ к международным компаниям. "
                 "Tuition Grant снижает стоимость, но обязывает работать в Сингапуре после выпуска (3 года).",
        "deadlines": "NUS/NTU: бакалавриат — октябрь–март; магистратура — декабрь–март; ASEAN Scholarship — декабрь–февраль.",
        "visa": "Student's Pass (ICA); подтверждение финансов; медосмотр.",
        "scholarships": [
            "ASEAN Scholarship, NUS Global Merit Scholarship, NTU Global Merit.",
            "SINGA (Singapore International Graduate Award) — PhD.",
            "SM1/SM2 (Singapore Government scholarships для стран ASEAN и др.).",
        ],
        "universities": {
            "it": ["National University of Singapore (NUS)", "Nanyang Technological University (NTU)", "SUTD", "SIT"],
            "business": ["NUS Business School", "NTU Nanyang Business School", "SMU Lee Kong Chian School of Business"],
            "med": ["NUS Yong Loo Lin School of Medicine", "NTU Lee Kong Chian School of Medicine", "Duke-NUS Medical School"],
            "hum": ["NUS (Arts and Social Sciences)", "NTU (College of Humanities)", "SMU (Social Sciences)"],
            "nat": ["NUS (Science)", "NTU (College of Science)", "A*STAR Graduate Academy"],
            "arts": ["LASALLE College of the Arts", "NAFA", "NTU (ADM — Art, Design & Media)", "SUTD (Architecture & Design)"],
        },
    },
    "my": {
        "name": "🇲🇾 Малайзия", "climate": "warm", "campus": "both", "english": 3,
        "tuition": (3000, 8000), "living": 600,
        "about": "Доступное образование на английском, филиалы британских и австралийских университетов "
                 "(Monash, Nottingham, Heriot-Watt) и комфортная жизнь в тропиках.",
        "deadlines": "Несколько наборов в год: февраль–март, июль, сентябрь–октябрь; подача — за 2–4 месяца.",
        "visa": "Student Pass (EMGS); подтверждение финансов; медосмотр; страховка.",
        "scholarships": [
            "Malaysia International Scholarship (MIS) — магистратура и PhD.",
            "MTCP (Malaysian Technical Cooperation Programme).",
            "University of Malaya, USM, UTM, UKM — гранты; merit-based скидки в частных вузах.",
        ],
        "universities": {
            "it": ["University of Malaya (UM)", "Universiti Teknologi Malaysia (UTM)", "Monash University Malaysia", "Taylor's University"],
            "business": ["University of Malaya", "Monash Malaysia", "Sunway University", "UPM Business School"],
            "med": ["University of Malaya", "UKM", "International Medical University (IMU)", "Monash Malaysia"],
            "hum": ["University of Malaya", "UKM", "USM", "Taylor's University"],
            "nat": ["UM", "USM", "UPM", "UKM"],
            "arts": ["Limkokwing University", "Raffles University", "UiTM (Art & Design)", "Taylor's (Design)"],
        },
    },
    "th": {
        "name": "🇹🇭 Таиланд", "climate": "warm", "campus": "both", "english": 3,
        "tuition": (3000, 8000), "living": 550,
        "about": "Недорогая жизнь, много международных программ на английском, особенно в Бангкоке и Чиангмае. "
                 "Подходит для бизнеса, медицины, дизайна и туризма.",
        "deadlines": "Rolling; два набора: июль–август и ноябрь–январь; Chulalongkorn — по раундам.",
        "visa": "Non-ED visa; подтверждение финансов; страховка; медсправки.",
        "scholarships": [
            "TICA — Thailand International Cooperation Agency (отдельные программы).",
            "Chulalongkorn University и Mahidol — merit-based гранты.",
            "AIT (Asian Institute of Technology) scholarships.",
        ],
        "universities": {
            "it": ["Chulalongkorn University", "KMUTT", "Asian Institute of Technology (AIT)", "Chiang Mai University"],
            "business": ["Thammasat University", "Chulalongkorn (CBS)", "Mahidol (CMMU)", "Kasetsart University"],
            "med": ["Mahidol University (Siriraj)", "Chulalongkorn University", "Chiang Mai University"],
            "hum": ["Chulalongkorn University", "Thammasat University", "Chiang Mai University"],
            "nat": ["Mahidol University", "Chulalongkorn University", "Kasetsart University"],
            "arts": ["Silpakorn University", "Chulalongkorn (Fine and Applied Arts)", "KMITL (Architecture & Design)"],
        },
    },
    "in": {
        "name": "🇮🇳 Индия", "climate": "warm", "campus": "both", "english": 3,
        "tuition": (1500, 4000), "living": 350,
        "about": "Самая низкая стоимость в списке, английский язык преподавания, сильная инженерия, IT и медицина. "
                 "Поступление в топ-вузы для иностранцев — через специальные квоты (SII, DASA, ICCR).",
        "deadlines": "Study in India: январь–март; ICCR: февраль–апрель; прочие вузы — май–июль.",
        "visa": "Student visa (X-1); подтверждение финансов; письмо о зачислении.",
        "scholarships": [
            "ICCR Scholarships — полное обучение + стипендия.",
            "Study in India (SII) — скидки и гранты для иностранцев.",
            "IIT, IISc — фелловшипы для магистров и PhD.",
        ],
        "universities": {
            "it": ["IIT Bombay", "IIT Delhi", "IIT Madras", "IISc Bangalore"],
            "business": ["IIM Ahmedabad", "IIM Bangalore", "ISB Hyderabad", "XLRI Jamshedpur"],
            "med": ["AIIMS Delhi", "CMC Vellore", "JIPMER", "Manipal"],
            "hum": ["Jawaharlal Nehru University (JNU)", "University of Delhi", "Ashoka University", "TISS Mumbai"],
            "nat": ["IISc Bangalore", "IISER Pune", "TIFR", "IIT Madras"],
            "arts": ["National Institute of Design (NID)", "IDC IIT Bombay", "Srishti Manipal Institute", "Jamia Millia Islamia"],
        },
    },
    "tr": {
        "name": "🇹🇷 Турция", "climate": "moderate", "campus": "both", "english": 2,
        "tuition": (1000, 6000), "living": 550,
        "about": "Недорогое образование в государственных вузах и сильные частные (Koç, Sabancı, Bilkent). "
                 "Турция — одна из самых удобных стран для старта: близость к Европе и Азии, много стипендий.",
        "deadlines": "Türkiye Scholarships: обычно 20 января – 20 февраля; YÖS — по расписанию вузов (весна); прямая подача: май–август.",
        "visa": "Student residence permit (ikamet); подтверждение финансов и жилья.",
        "scholarships": [
            "Türkiye Scholarships (Türkiye Burslari) — полное обучение, жильё, стипендия, перелёт, язык.",
            "Koç University, Sabancı University, Bilkent — merit-based гранты.",
            "YTB — для студентов из отдельных стран.",
        ],
        "universities": {
            "it": ["METU (ODTÜ)", "Istanbul Technical University", "Boğaziçi University", "Bilkent University"],
            "business": ["Koç University", "Sabancı University", "Boğaziçi University", "Bilkent University"],
            "med": ["Hacettepe University", "Istanbul University (Cerrahpaşa)", "Koç University", "Ankara University"],
            "hum": ["Boğaziçi University", "METU", "Istanbul University", "Bilkent University"],
            "nat": ["METU", "Boğaziçi University", "Istanbul Technical University", "Bilkent University"],
            "arts": ["Mimar Sinan Fine Arts University", "Bilkent (Art, Design & Architecture)", "Istanbul Technical University (Architecture)"],
        },
    },
    "ae": {
        "name": "🇦🇪 ОАЭ", "climate": "warm", "campus": "both", "english": 3,
        "tuition": (8000, 20000), "living": 1300,
        "about": "Футуристичная международная среда, английский повсеместен, филиалы известных вузов (NYUAD, Heriot-Watt, Middlesex). "
                 "Налогов нет, но жизнь и обучение недёшевы; жара летом.",
        "deadlines": "Rolling; осенний набор — до весны; гранты (MBZUAI, Khalifa) — чаще декабрь–март.",
        "visa": "Student visa (спонсирует вуз); медосмотр; страховка; подтверждение жилья.",
        "scholarships": [
            "MBZUAI — полностью финансируемые магистры и PhD по ИИ.",
            "Khalifa University — полные стипендии для магистров и PhD.",
            "NYU Abu Dhabi — need-blind financial aid (очень конкурентно).",
            "American University of Sharjah — merit-based гранты.",
        ],
        "universities": {
            "it": ["MBZUAI", "Khalifa University", "UAE University", "American University of Sharjah"],
            "business": ["American University of Sharjah", "University of Dubai", "Zayed University", "Heriot-Watt Dubai"],
            "med": ["Khalifa University (Medicine)", "Mohammed Bin Rashid University of Medicine", "UAE University", "RAK Medical & Health Sciences University"],
            "hum": ["NYU Abu Dhabi", "American University of Sharjah", "Zayed University", "Sorbonne Abu Dhabi"],
            "nat": ["Khalifa University", "UAE University", "NYU Abu Dhabi", "American University of Sharjah"],
            "arts": ["NYU Abu Dhabi (Arts & Design)", "Zayed University (Arts & Creative Enterprises)", "American University of Sharjah (Architecture & Design)"],
        },
    },
    "kz": {
        "name": "🇰🇿 Казахстан", "climate": "cold", "campus": "both", "english": 2,
        "tuition": (2000, 6000), "living": 450,
        "about": "Доступная жизнь и обучение, русскоязычная среда, английские программы в Nazarbayev University и KBTU. "
                 "Подходит тем, кто ищет простой переезд и близость к дому.",
        "deadlines": "Обычно июнь–август; Nazarbayev University — январь–март.",
        "visa": "Student visa/регистрация; подтверждение финансов; медсправки.",
        "scholarships": [
            "Государственные гранты для иностранцев (квоты Министерства науки и высшего образования РК).",
            "Nazarbayev University — полные гранты на магистратуру и PhD.",
            "KBTU, KIMEP — merit-based скидки.",
        ],
        "universities": {
            "it": ["Nazarbayev University", "KBTU", "Satbayev University", "Astana IT University"],
            "business": ["KIMEP University", "Nazarbayev University (GSB)", "Al-Farabi Kazakh National University"],
            "med": ["Nazarbayev University School of Medicine", "Astana Medical University", "Kazakh National Medical University"],
            "hum": ["Al-Farabi KazNU", "L.N. Gumilyov Eurasian National University", "KIMEP University"],
            "nat": ["Nazarbayev University", "Al-Farabi KazNU", "Satbayev University"],
            "arts": ["Zhurgenov Kazakh National Academy of Arts", "Kurmangazy Kazakh National Conservatory"],
        },
    },
    "ge": {
        "name": "🇬🇪 Грузия", "climate": "moderate", "campus": "city", "english": 2,
        "tuition": (2000, 6000), "living": 450,
        "about": "Дешёвая жизнь, лояльная визовая политика, много программ на английском (особенно медицина). "
                 "Тбилиси — активный и дружелюбный студенческий город.",
        "deadlines": "Обычно июнь–сентябрь; для международных студентов — до начала семестра.",
        "visa": "Student residence permit; нострификация аттестата; медстраховка.",
        "scholarships": [
            "Правительственные стипендии Грузии (отдельные программы для иностранцев).",
            "Ilia State University, Free University of Tbilisi — merit-based гранты.",
            "Erasmus+ (обмены).",
        ],
        "universities": {
            "it": ["Tbilisi State University", "Georgian Technical University", "Free University of Tbilisi", "Caucasus University"],
            "business": ["Tbilisi State University", "Caucasus University", "Free University of Tbilisi", "ISET (Economics)"],
            "med": ["Tbilisi State Medical University", "David Tvildiani Medical University", "Ilia State University", "European University"],
            "hum": ["Tbilisi State University", "Ilia State University", "Free University of Tbilisi"],
            "nat": ["Tbilisi State University", "Ilia State University", "Georgian Technical University"],
            "arts": ["Tbilisi State Academy of Arts", "Shota Rustaveli Theatre and Film University", "Tbilisi State Conservatoire"],
        },
    },
}

MORE_COUNTRIES = {**EU_MORE, **ASIA}
