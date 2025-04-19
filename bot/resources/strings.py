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

    hello = "🤖 Xush kelibsiz!\n Bot tilini tanlang  \U0001F1FA\U0001F1FF \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n" \
        "👋 Добро пожаловать \n Выберите язык бота \U0001F1F7\U0001F1FA\n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n" \
            "😊 Welcome \n Select the bot language \U0001F1EC\U0001F1E7"

    uz_ru_en = ["UZ 🇺🇿", "RU 🇷🇺", "EN 🇬🇧"]
    main_menu = ["Asosiy menyu 🏠", "Главное меню 🏠", "Main menu 🏠"]
    change_lang = [
        "\U0001F1FA\U0001F1FF Tilni o'zgartirish \U0001F1F7\U0001F1FA",
        "\U0001F1FA\U0001F1FF Сменить язык \U0001F1F7\U0001F1FA",
        "\U0001F1FA\U0001F1FF Change language \U0001F1EC\U0001F1E7",
    ]
    select_lang = [
        "Iltimos, bot tilini tanlang:",
        "Пожалуйста, выберите язык бота:",
        "Please select the bot language:"
    ]
    type_name = [
        "Ismingizni kiriting:",
        "Введите ваше имя:",
        "Please enter your name:"
    ]
    send_number = [
        "Telefon raqamingizni yuboring:",
        "Оставьте свой номер телефона:",
        "Please send your phone number:"
    ]
    leave_number = [
        "Telefon raqamni yuborish",
        "Оставить номер телефона",
        "Send phone number"
    ]
    back = ["🔙 Ortga", "🔙 Назад", "🔙 Back"]
    next_step = ["Davom etish ➡️", "Далее ➡️", "Next ➡️"]
    seller = ["Sotuvchi 🛍", "Продавцам 🛍", "Seller 🛍"]
    buyer = ["Xaridor 💵", "Покупателям 💵", "Buyer 💵"]
    settings = ["Sozlamalar ⚙️", "Настройки ⚙️", "Settings ⚙️"]
    language_change = ["Tilni o\'zgartirish 🇺🇿🇷🇺", "Смена языка 🇺🇿🇷🇺", "Change language 🇺🇿🇷🇺"]
    change_phone_number = [
        "Telefon raqamni o\'zgartirish 📞",
        "Смена номера телефона 📞",
        "Change phone number 📞",
    ]
    change_name = ["Ismni o\'zgartirish 👤", "Смени имени 👤", "Change name 👤"]
    settings_desc = ["Sozlamalar ⚙️", "Настройки ⚙️", "Settings ⚙️"]
    your_phone_number = [
        "📌 Sizning telefon raqamingiz: [] 📌",
        "📌 Ваш номер телефона: [] 📌",
        "📌 Your phone number: [] 📌",
    ]
    send_new_phone_number = [
        "Yangi telefon raqamingizni yuboring!\n<i>Jarayonni bekor qilish uchun \"🔙 Ortga\" tugmasini bosing.</i>",
        "Отправьте свой новый номер телефона!\n<i>Нажмите кнопку \"🔙 Назад\", чтобы отменить процесс.</i>",
        "Send your new phone number!\n<i>Press \"🔙 Back\" to cancel the process.</i>",
    ]
    number_is_logged = [
        "Bunday raqam bilan ro'yxatdan o'tilgan, boshqa telefon raqam kiriting",
        "Этот номер уже зарегистрирован. Введите другой номер",
        "This number is already registered. Enter another number",
    ]
    changed_your_phone_number = [
        "Sizning telefon raqamingiz muvaffaqiyatli o\'zgartirildi! ♻️",
        "Ваш номер телефона успешно изменен! ♻️",
        "Your phone number has been successfully changed! ♻️",
    ]
    your_name = ["Sizning ismingiz: ", "Ваше имя: ", "Your name: "]
    send_new_name = [
        "Ismingizni o'zgartirish uchun, yangi ism kiriting:\n<i>Jarayonni bekor qilish uchun \"🔙 Ortga\" tugmasini bosing.</i>",
        "Чтобы изменить свое имя, введите новое:\n<i>Нажмите кнопку \"🔙 Назад\", чтобы отменить процесс.</i>",
        "To change your name, enter a new name:\n<i>Press \"🔙 Back\" to cancel the process.</i>",
    ]
    changed_your_name = [
        "Sizning ismingiz muvaffaqiyatli o'zgartirildi!",
        "Ваше имя успешно изменено!",
        "Your name has been successfully changed!",
    ]

    ask_name = [
        "Iltimos, ismingizni kiriting:",
        "Пожалуйста, введите ваше имя:",
        "Please enter your name:"
    ]
    ask_phone = [
        "Iltimos, telefon raqamingizni yuboring yoki yozing:",
        "Пожалуйста, отправьте или введите ваш номер телефона:",
        "Please send or enter your phone number:"
    ]
    ask_complaint = [
        "Iltimos, fikr mulohaza yoki shikoyatingizni yozib qoldiring:",
        "Пожалуйста, оставьте свой отзыв или жалобу:",
        "Please leave your feedback or complaint:"
    ]
    complaint_thank_you = [
        "Fikringiz uchun rahmat",
        "Спасибо за ваш отзыв",
        "Thank you for your feedback"
    ]
    operation_canceled = [
        "Amal bekor qilindi.",
        "Операция отменена.",
        "Operation canceled."
    ]

    reload_bot = [
        "Botni qayta ishga tushirish",
        "Перезапустить бота",
        "Restart bot"
    ]

    cancel_opeation = [
        "Amalni bekor qilish",
        "Отменить операцию",
        "Cancel operation"
    ]

    _ = [
        "",
        "",
        ""
    ]

    _ = [
        "",
        "",
        ""
    ]

    _ = [
        "",
        "",
        ""
    ]

    _ = [
        "",
        "",
        ""
    ]

    _ = [
        "",
        "",
        ""
    ]
