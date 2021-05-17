import pdfkit
import telegram
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
from telegram import MessageEntity
import os

TOKEN = os.getenv("TOKEN")
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Start
def start(update, context):
    username = update.message.chat.username
    print(username)
    keyboard = [
        [
            telegram.InlineKeyboardButton("Support Channel 🌱",
                                          url="t.me/theostrich"),
            telegram.InlineKeyboardButton("Support Group 🦸‍♂", url="t.me/ostrichdiscussion"),
        ],
        [
            telegram.InlineKeyboardButton("Developer 🧑‍💻",
                                          url="https://www.github.com/nooneluvme"),
        ],
    ]

    reply_markup = telegram.InlineKeyboardMarkup(keyboard)

    message = f'''
<b>Hey @{username} 👋
 
🌀 I can convert a WebPage To Pdf 
💀 /help to for help 
</b>
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='html',
                             reply_markup=reply_markup, disable_web_page_preview=True)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# Help
def help(update, context):
    username = update.message.chat.username
    print("Help :", username)
    message = '''<b>Just Send Me A Link Dude🥱</b> '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='html'
                             , disable_web_page_preview=True)


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


# web2pdf

def web2pdf(update, context):
        print("web2pdf : ", update.message.chat.username)
        url=update.message.text
        print("url = ", url)
        if "http" in url:
            keyboard = [
                [
                    telegram.InlineKeyboardButton("Url 🔗",
                                                  url=url),
                ]
            ]
            reply_markup = telegram.InlineKeyboardMarkup(keyboard)
            config = pdfkit.configuration(wkhtmltopdf='./bin/wkhtmltopdf')
            pdfkit.from_url(url, output_path="@theweb2pdfbot.pdf", configuration=config)

            context.bot.send_document(chat_id=update.effective_chat.id,
                                      document=open('@theweb2pdfbot.pdf', 'rb'), parse_mode="html", reply_markup=reply_markup,timeout=200)

web2pdf_handler = MessageHandler(Filters.text & Filters.entity(MessageEntity.URL), web2pdf)
dispatcher.add_handler(web2pdf_handler)

updater.start_polling()
