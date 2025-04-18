from bot.bot import *
from bot.models import Bot_user, Review
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardRemove
from bot.utils.keyboards import build_keyboard


async def setup_menu_commands(context: CustomContext):
    commands = [
        ("start", context.words.reload_bot),
    ]
    await bot.set_my_commands(commands)


async def ask_phone(update: Update, context: CustomContext):
    if await is_message_back(update):
        keyboard = await build_keyboard(context, Strings.uz_ru, n_cols=2, main_menu_button=False, back_button=False)
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
    await update.message.reply_text(context.words.ask_review, reply_markup=keyboard)
    return REVIEW


async def save_review(update: Update, context: CustomContext):
    if await is_message_back(update):
        keyboard = await build_keyboard(context, [], n_cols=1, main_menu_button=False)
        await update.message.reply_text(context.words.ask_phone, reply_markup=keyboard)
        return PHONE

    user = await Bot_user.objects.aget(user_id=update.message.from_user.id)
    review = Review(user=user, text=update.message.text)
    await review.asave()
    await setup_menu_commands(context)
    await update.message.reply_text(context.words.review_thank_you, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def cancel(update: Update, context: CustomContext):
    await setup_menu_commands(context)
    await update.message.reply_text(context.words.operation_canceled, reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
