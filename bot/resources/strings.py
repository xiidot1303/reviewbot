class Strings:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def __getattribute__(self, key: str):
        if result := object.__getattribute__(self, key):
            if isinstance(result, list):
                from bot.services.redis_service import get_user_lang
                user_id = object.__getattribute__(self, "user_id")
                user_lang_code = get_user_lang(user_id)
                return result[user_lang_code]
            else:
                return result
        else:
            return key

    hello = """🤖 Xush kelibsiz!\n Bot tilini tanlang  🌎 \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n
    👋 Добро пожаловать \n \U0001F1FA\U0001F1FF Выберите язык бота \U0001F1F7\U0001F1FA"""
    added_group = "Чат успешно добавлена ✅"
    uz_ru = ["UZ 🇺🇿", "RU 🇷🇺"]
    main_menu = ["Asosiy menyu 🏠", "Главное меню 🏠"]
    change_lang = [
        "\U0001F1FA\U0001F1FF Tilni o'zgartirish \U0001F1F7\U0001F1FA",
        "\U0001F1FA\U0001F1FF Сменить язык \U0001F1F7\U0001F1FA",
    ]
    select_lang = [
        "Iltimos, bot tilini tanlang:", 
        "Пожалуйста, выберите язык бота:"
    ]
    type_name = ["""Ismingizni kiriting """, """Введите ваше имя """]
    send_number = [
        """Telefon raqamingizni yuboring """,
        """Оставьте свой номер телефона """,
    ]
    leave_number = ["Telefon raqamni yuborish", "Оставить номер телефона"]
    back = ["🔙 Ortga", "🔙 Назад"]
    next_step = ["""Davom etish ➡️""", """Далее ➡️"""]
    seller = ["""Sotuvchi 🛍""", """Продавцам 🛍"""]
    buyer = ["""Xaridor 💵""", """Покупателям 💵"""]
    settings = ["""Sozlamalar ⚙️""", """Настройки ⚙️"""]
    language_change = ["""Tilni o\'zgartirish 🇺🇿🇷🇺""", """Смена языка 🇺🇿🇷🇺"""]
    change_phone_number = [
        """Telefon raqamni o\'zgartirish 📞""",
        """Смена номера телефона 📞""",
    ]
    change_name = ["""Ismni o\'zgartirish 👤""", """Смени имени 👤"""]
    settings_desc = ["""Sozlamalar ⚙️""", """Настройки ⚙️"""]
    your_phone_number = [
        """📌 Sizning telefon raqamingiz: [] 📌""",
        """📌 Ваш номер телефона: [] 📌""",
    ]
    send_new_phone_number = [
        """Yangi telefon raqamingizni yuboring!\n<i>Jarayonni bekor qilish uchun "🔙 Ortga" tugmasini bosing.</i>""",
        """Отправьте свой новый номер телефона!\n<i>Нажмите кнопку "🔙 Назад", чтобы отменить процесс.</i>""",
    ]
    number_is_logged = [
        "Bunday raqam bilan ro'yxatdan o'tilgan, boshqa telefon raqam kiriting",
        "Этот номер уже зарегистрирован. Введите другой номер",
    ]
    changed_your_phone_number = [
        """Sizning telefon raqamingiz muvaffaqiyatli o\'zgartirildi! ♻️""",
        """Ваш номер телефона успешно изменен! ♻️""",
    ]
    your_name = ["""Sizning ismingiz: """, """Ваше имя: """]
    send_new_name = [
        """Ismingizni o'zgartirish uchun, yangi ism kiriting:\n<i>Jarayonni bekor qilish uchun "🔙 Ortga" tugmasini bosing.</i>""",
        """Чтобы изменить свое имя, введите новое:\n<i>Нажмите кнопку "🔙 Назад", чтобы отменить процесс.</i>""",
    ]
    changed_your_name = [
        """Sizning ismingiz muvaffaqiyatli o'zgartirildi!""",
        """Ваше имя успешно изменено!""",
    ]

    ask_name = [
        "Iltimos, ismingizni kiriting:", 
        "Пожалуйста, введите ваше имя:"
    ]
    ask_phone = [
        "Iltimos, telefon raqamingizni yuboring yoki yozing:", 
        "Пожалуйста, отправьте или введите ваш номер телефона:"
    ]
    ask_review = [
        "Iltimos, fikringizni yozing:", 
        "Пожалуйста, напишите ваш отзыв:"
    ]
    review_thank_you = [
        "Fikringiz uchun rahmat!", 
        "Спасибо за ваш отзыв!"
    ]
    operation_canceled = [
        "Amal bekor qilindi.", 
        "Операция отменена."
    ]

    reload_bot = [
        "Botni qayta ishga tushirish",
        "Перезапустить бота"
    ]

    cancel_opeation = [
        "Amalni bekor qilish",
        "Отменить операцию"
    ]

    _ = [
        "",
        ""
    ]

    _ = [
        "",
        ""
    ]

    _ = [
        "",
        ""
    ]

    _ = [
        "",
        ""
    ]

    _ = [
        "",
        ""
    ]
