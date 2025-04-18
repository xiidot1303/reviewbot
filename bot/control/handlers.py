from bot import *
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    InlineQueryHandler,
    TypeHandler,
    ConversationHandler
)

from bot.resources.conversationList import *

from bot.bot import (
    main,
)

from bot.bot.review import ask_phone, ask_review, save_review, cancel
from bot.bot.main import set_language


review_conversation = ConversationHandler(
    entry_points=[CommandHandler('start', main.start)],
    states={
        LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, callback=set_language)],
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, callback=ask_phone)],
        PHONE: [MessageHandler(filters.CONTACT | (filters.TEXT & ~filters.COMMAND), callback=ask_review)],
        REVIEW: [MessageHandler(filters.TEXT & ~filters.COMMAND, callback=save_review)],
    },
    fallbacks=[CommandHandler('start', cancel)],
    name='review_conversation',
    persistent=True,
)

handlers = [
    review_conversation,
    TypeHandler(type=NewsletterUpdate, callback=main.newsletter_update),
]
