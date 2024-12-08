from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

start_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Тесты'
        ),
        KeyboardButton(
            text='Теория'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


def generate_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        # [InlineKeyboardButton(text=questions[0], callback_data=f"q_{questions[0]}")],
        # [InlineKeyboardButton(text=questions[1], callback_data=f"q_{questions[1]}")],
        # [InlineKeyboardButton(text=questions[2], callback_data=f"q_{questions[2]}")],
        [InlineKeyboardButton(text="Заменить вопрос", callback_data="choose_question")],
        [InlineKeyboardButton(text="В главное меню", callback_data="main_menu")]
    ])
    return keyboard


def theory_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1. Налоги", callback_data="tax")],
        [InlineKeyboardButton(text="2. Страхование", callback_data="ensurance")],
        [InlineKeyboardButton(text="3. Бюджет", callback_data="budget")],
        [InlineKeyboardButton(text="4. Криптовалюта", callback_data="crypto")],
        [InlineKeyboardButton(text="5. Банковская карта", callback_data="card")],
        [InlineKeyboardButton(text="6. Виды денег", callback_data="money")],
        [InlineKeyboardButton(text="7. Кредит", callback_data="credit")]

    ])
    return keyboard


def test_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1. Налоги", callback_data="tax_test")],
        [InlineKeyboardButton(text="2. Страхование", callback_data="ensurance_test")],
        [InlineKeyboardButton(text="3. Бюджет", callback_data="budget_test")],
        [InlineKeyboardButton(text="4. Криптовалюта", callback_data="crypto_test")],
        [InlineKeyboardButton(text="5. Банковская карта", callback_data="card_test")],
        [InlineKeyboardButton(text="6. Виды денег", callback_data="money_test")],
        [InlineKeyboardButton(text="7. Кредит", callback_data="credit_test")]

    ])
    return keyboard


def back_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data="back")]
    ])
    return keyboard

def update_kb():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Обновить СП', callback_data="update_page")]
    ])
    return keyboard


tax1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Возвратности денежных средств налогоплательщикам'
        )
    ],
    [
        KeyboardButton(
            text='Всеобщности и равенства налогообложения'
        )
    ],
    [
        KeyboardButton(
            text='Дифференцированности ставки налогов в зависимости от форм собственности'
        )
    ],
    [
        KeyboardButton(
            text='Дифференцированности ставки налогов в зависимости от гражданства физических лиц'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


tax2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Налоги с физических и юридических лиц'
        )
    ],
    [
        KeyboardButton(
            text='Федеральные, региональные, местные'
        )
    ],
    [
        KeyboardButton(
            text='Внутренние и внешние'
        )
    ],
    [
        KeyboardButton(
            text='Прямые и косвенные'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


tax3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Прибыль'
        )
    ],
    [
        KeyboardButton(
            text='Государственная пенсия'
        )
    ],
    [
        KeyboardButton(
            text='Доход'
        )
    ],
    [
        KeyboardButton(
            text='Собственность'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


tax4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Является добровольной'
        )
    ],
    [
        KeyboardButton(
            text='Осуществляется по усмотрению налоговой инспекции'
        )
    ],
    [
        KeyboardButton(
            text='Является конституционной обязанностью граждан'
        )
    ],
    [
        KeyboardButton(
            text='Зависит от имущественного положения гражданина'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


tax5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Акцизы'
        )
    ],
    [
        KeyboardButton(
            text='Налог на прибыль'
        )
    ],
    [
        KeyboardButton(
            text='Государственная пошлина'
        )
    ],
    [
        KeyboardButton(
            text='Курортный сбор'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# ENSURANCE

ensurance1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Механизм, предназначенный для сокращения рисков физического или юридического лица путем их передачи страховщику на основе договора.'
        )
    ],
    [
        KeyboardButton(
            text='Механизм, предназначенный для сокращения рисков физического или юридического лица путем их передачи страховщику на основе переговоров.'
        )
    ],
    [
        KeyboardButton(
            text='Денежная выплата, которую получают выгодоприобретатель или страхователь при наступлении страхового случая.'
        )
    ],
    [
        KeyboardButton(
            text='Обязательные или добровольные платежи.'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


ensurance2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Обязательное и добровольное'
        )
    ],
    [
        KeyboardButton(
            text='Частное и государственное'
        )
    ],
    [
        KeyboardButton(
            text='Индивидуальное и взаимное'
        )
    ],
    [
        KeyboardButton(
            text='Личное и коллективное'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


ensurance3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Страхование ГПО работодателя'
        )
    ],
    [
        KeyboardButton(
            text='Страхование ГПО туроператора или турагента'
        )
    ],
    [
        KeyboardButton(
            text='Страхование от несчастных случае'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


ensurance4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Жизнью, здоровьем, трудоспособностью и пенсионным обеспечением страхователя или застрахованного лица'
        )
    ],
    [
        KeyboardButton(
            text='Возмещением страхователем причиненного им вреда личности или имуществу физического или юридического лица'
        )
    ],
    [
        KeyboardButton(
            text='Перестрахованием'
        )
    ],
    [
        KeyboardButton(
            text='Владением, пользованием, распоряжением имуществом'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


ensurance5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# BUDGET

budget1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Обязательные'
        )
    ],
    [
        KeyboardButton(
            text='Произвольные'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


budget2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Расходы'
        )
    ],
    [
        KeyboardButton(
            text='Доходы'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


budget3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='То, куда семья отдаёт деньги'
        )
    ],
    [
        KeyboardButton(
            text='То, откуда семья получает деньги'
        )
    ],
    [
        KeyboardButton(
            text='Часть дохода семьи, не используемая на текущее потребление'
        )
    ],
    [
        KeyboardButton(
            text='Финансовый план семьи на определённый период времени'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


budget4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Плохое здоровье родителей, пьянство и другие вредные привычки, наличие долгов и кредитов'
        )
    ],
    [
        KeyboardButton(
            text='Развитие своих способностей, престижное образование, старательность на работе'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


budget5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Доходы меньше расходов'
        )
    ],
    [
        KeyboardButton(
            text='Доходы равны расходам'
        )
    ],
    [
        KeyboardButton(
            text='Доходы больше расходов'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# CRYPTO

crypto1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Дивиденды'
        )
    ],
    [
        KeyboardButton(
            text='Токены'
        )
    ],
    [
        KeyboardButton(
            text='Проценты'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


crypto2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Способ продажи криптовалюты'
        )
    ],
    [
        KeyboardButton(
            text='Средство обмена криптовалюты'
        )
    ],
    [
        KeyboardButton(
            text='Средство получения процентов с криптовалюты'
        )
    ],
    [
        KeyboardButton(
            text='Способ получения криптовалюты'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


crypto3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Да'
        )
    ],
    [
        KeyboardButton(
            text='Нет'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


crypto4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Покупка продуктов в магазине'
        )
    ],
    [
        KeyboardButton(
            text='Инвестиции'
        )
    ],
    [
        KeyboardButton(
            text='Оплата авиабилетов'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


crypto5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Нет бумажного выражения'
        )
    ],
    [
        KeyboardButton(
            text='Не существует в Интернете'
        )
    ],
    [
        KeyboardButton(
            text='Её ценность зависит от государства'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# CARD

card1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='5'
        )
    ],
    [
        KeyboardButton(
            text='16'
        )
    ],
    [
        KeyboardButton(
            text='3'
        )
    ],
    [
        KeyboardButton(
            text='9'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


card2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='На лицевой'
        )
    ],
    [
        KeyboardButton(
            text='На оборотной'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


card3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Да'
        )
    ],
    [
        KeyboardButton(
            text='Нет'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


card4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Штрих-код'
        )
    ],
    [
        KeyboardButton(
            text='Наименование банка'
        )
    ],
    [
        KeyboardButton(
            text='Фото владельца карты'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


card5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Полоса для имени держателя карты'
        )
    ],
    [
        KeyboardButton(
            text='Полоса для подписи'
        )
    ],
    [
        KeyboardButton(
            text='Магнитная полоса'
        )
    ],
    [
        KeyboardButton(
            text='Данные банка'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# MONEY

money1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Полные'
        )
    ],
    [
        KeyboardButton(
            text='Неполноценные'
        )
    ],
    [
        KeyboardButton(
            text='Неполные'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


money2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Товарные'
        )
    ],
    [
        KeyboardButton(
            text='Сложные'
        )
    ],
    [
        KeyboardButton(
            text='Бумажные'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


money3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Металлические'
        )
    ],
    [
        KeyboardButton(
            text='Бумажные'
        )
    ],
    [
        KeyboardButton(
            text='Медицинские'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


money4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


money5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ],
    [
        KeyboardButton(
            text='-'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")

# CREDIT

credit1_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Возможность взять технику или оборудование в аренду с правом последующего выкупа.'
        )
    ],
    [
        KeyboardButton(
            text='Предоставление денежных средств в долг на условиях возвратности под проценты'
        )
    ],
    [
        KeyboardButton(
            text='Поиск спонсоров, инвесторов и прочих лиц для финансирования мероприятия, проекта, идеи или организации.'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


credit2_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Чтобы приобрести необходимые товары или услуги быстре'
        )
    ],
    [
        KeyboardButton(
            text='Чтобы быстро продать имущество'
        )
    ],
    [
        KeyboardButton(
            text='Чтобы получить более низкую ставку по первой ипотеке'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


credit3_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ипотечному'
        )
    ],
    [
        KeyboardButton(
            text='Потребительскому'
        )
    ],
    [
        KeyboardButton(
            text='Банковскому'
        )
    ],
    [
        KeyboardButton(
            text='Ломбардному'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


credit4_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Международный'
        )
    ],
    [
        KeyboardButton(
            text='Ростовщический'
        )
    ],
    [
        KeyboardButton(
            text='Государственный'
        )
    ],
    [
        KeyboardButton(
            text='Коммерческий'
        )
    ],
    [
        KeyboardButton(
            text='Потребительский'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")


credit5_kb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Да'
        )
    ],
    [
        KeyboardButton(
            text='Нет'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите действие")
