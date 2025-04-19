from bot.bot import *
from bot.models import Bot_user, Complaint  # Updated import
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardRemove
from bot.utils.keyboards import build_keyboard
from config import TELEGRAM_GROUP_ID


async def setup_menu_commands(context: CustomContext):
    commands = [
        ("start", context.words.reload_bot),
    ]
    await bot.set_my_commands(commands)


async def ask_phone(update: Update, context: CustomContext):
    if await is_message_back(update):
        keyboard = await build_keyboard(context, Strings.uz_ru_en, n_cols=1, main_menu_button=False, back_button=False)
        await update.message.reply_text(Strings.hello, reply_markup=keyboard)
        return LANGUAGE

    user, _ = await Bot_user.objects.aget_or_create(user_id=update.message.from_user.id)
    user.name = update.message.text
    await user.asave()
    keyboard = await build_keyboard(context, [KeyboardButton(text=context.words.leave_number, request_contact=True)], n_cols=1, main_menu_button=False)
    await update.message.reply_text(context.words.ask_phone, reply_markup=keyboard)
    return PHONE


async def ask_review(update: Update, context: CustomContext):
    if await is_message_back(update):
        keyboard = await build_keyboard(context, [], n_cols=1, main_menu_button=False)
        await update.message.reply_text(context.words.ask_name, reply_markup=keyboard)
        return NAME

    user = await Bot_user.objects.aget(user_id=update.message.from_user.id)
    if update.message.contact:
        user.phone = update.message.contact.phone_number
    else:
        user.phone = update.message.text
    await user.asave()
    keyboard = await build_keyboard(context, [], n_cols=1, main_menu_button=False)
    await update.message.reply_text(context.words.ask_complaint, reply_markup=keyboard)
    return REVIEW


async def save_review(update: Update, context: CustomContext):  # Kept function name for consistency
    if await is_message_back(update):
        keyboard = await build_keyboard(context, [], n_cols=1, main_menu_button=False)
        await update.message.reply_text(context.words.ask_phone, reply_markup=keyboard)
        return PHONE

    user = await Bot_user.objects.aget(user_id=update.message.from_user.id)
    complaint = Complaint(user=user, text=update.message.text)  # Updated to Complaint
    await complaint.asave()

    # Prepare the message in Russian
    message = (
        f"📢 Новая жалоба:\n\n"
        f"👤 Пользователь: {user.name or 'Не указано'}\n"
        f"📱 Телефон: {user.phone or 'Не указан'}\n"
        f"🌐 Язык: {'Русский' if user.lang == 1 else 'Узбекский' if user.lang == 0 else 'Английский'}\n"
        f"📝 Жалоба: {complaint.text}\n"
        f"📅 Дата: {complaint.date.strftime('%Y-%m-%d %H:%M:%S')}"
    )

    # Send the message to the Telegram group
    await context.bot.send_message(chat_id=TELEGRAM_GROUP_ID, text=message)

    await setup_menu_commands(context)
    await update.message.reply_text(context.words.complaint_thank_you, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def cancel(update: Update, context: CustomContext):
    await setup_menu_commands(context)
    await update.message.reply_text(context.words.operation_canceled, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
