from bot.bot import *
import json
import logging
import traceback
import html
from django.db import close_old_connections
from bot.models import Bot_user
from bot.utils.keyboards import build_keyboard

LANGUAGE, NAME = range(2)

async def setup_menu_commands(context: CustomContext):
    commands = [
        ("start", context.words.cancel_opeation),
    ]
    await bot.set_my_commands(commands)

async def start(update: Update, context: CustomContext):
    keyboard = [
        Strings.uz_ru_en,  # Update to include three languages
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(Strings.hello, reply_markup=reply_markup)
    return LANGUAGE

async def set_language(update: Update, context: CustomContext):
    if await is_message_back(update):
        keyboard = await build_keyboard(context, Strings.uz_ru_en, n_cols=3, main_menu_button=False)
        await update.message.reply_text(Strings.hello, reply_markup=keyboard)
        return LANGUAGE

    selected_language = update.message.text
    if selected_language == Strings.uz_ru_en[0]:  # Uzbek
        lang_code = 0
    elif selected_language == Strings.uz_ru_en[1]:  # Russian
        lang_code = 1
    elif selected_language == Strings.uz_ru_en[2]:  # English
        lang_code = 2
    else:
        keyboard = await build_keyboard(context, Strings.uz_ru_en, n_cols=3, main_menu_button=False)
        await update.message.reply_text(context.words.select_lang, reply_markup=keyboard)
        return LANGUAGE

    user, _ = await Bot_user.objects.aget_or_create(user_id=update.message.from_user.id)
    user.lang = lang_code
    await user.asave()
    await setup_menu_commands(context)

    keyboard = await build_keyboard(context, [], n_cols=1, main_menu_button=False)
    await update.message.reply_text(context.words.ask_name, reply_markup=keyboard)
    return NAME

async def newsletter_update(update: NewsletterUpdate, context: CustomContext):
    bot = context.bot
    if not (update.photo or update.video or update.document):
        # send text message
        message = await bot.send_message(
            chat_id=update.user_id,
            text=update.text,
            reply_markup=update.reply_markup,
            parse_mode=ParseMode.HTML
        )

    if update.photo:
        # send photo
        message = await bot.send_photo(
            update.user_id,
            update.photo,
            caption=update.text,
            reply_markup=update.reply_markup,
            parse_mode=ParseMode.HTML,
        )
    if update.video:
        # send video
        message = await bot.send_video(
            update.user_id,
            update.video,
            caption=update.text,
            reply_markup=update.reply_markup,
            parse_mode=ParseMode.HTML,
        )
    if update.document:
        # send document
        message = await bot.send_document(
            update.user_id,
            update.document,
            caption=update.text,
            reply_markup=update.reply_markup,
            parse_mode=ParseMode.HTML,
        )
    if update.pin_message:
        await bot.pin_chat_message(chat_id=update.user_id, message_id=message.message_id)


###############################################################################################
###############################################################################################
###############################################################################################
logger = logging.getLogger(__name__)


async def error_handler(update: Update, context: CustomContext):
    # restart db connection if error is "connection already closed"
    if "connection already closed" in str(context.error):
        await sync_to_async(close_old_connections)()
        return


    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error("Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)
    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        "An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
    )
    error_message = f"{html.escape(tb_string)}"

    # Finally, send the message
    try:
        await context.bot.send_message(
            chat_id=206261493, text=message, parse_mode=ParseMode.HTML
        )
        for i in range(0, len(error_message), 4000):
            await context.bot.send_message(
                chat_id=206261493, text=f"<pre>{error_message[i:i+4000]}</pre>", parse_mode=ParseMode.HTML
            )
    except Exception as ex:
        print(ex)
