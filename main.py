import pdfkit
import telegram
from telegram.ext import Updater, CommandHandler
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
 
I can convert a WebPage To Pdf 📄
/help to for help 
</b>
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='html',
                             reply_markup=reply_markup, disable_web_page_preview=True)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# help
def help(update, context):
    username = update.message.chat.username
    print("Help :", username)
    message = '''
<b>
Usage:
/web2pdf {url}
example </b> : /web2pdf https://theostrich.eu.org/
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode='html'
                             , disable_web_page_preview=True)


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


# web2pdf

def web2pdf(update, context):
    print("web2pdf : ", update.message.chat.username)
    url = context.args[0]
    print("url = ", url)
    cap=f"🔗 Url : {url}"
    if "http" in url:
            pdfkit.from_url(url, "@theweb2pdfbot.pdf")
            context.bot.send_document(chat_id=update.effective_chat.id,
                                      document=open('@theweb2pdfbot.pdf', 'rb'),
                                      caption=cap, parse_mode="html",timeout=150)
    else:
        update.message.reply_text(reply_to_message_id=update.message.message_id, text="Send A valid 🔗 url")


web2pdf_handler = CommandHandler('web2pdf', web2pdf)
dispatcher.add_handler(web2pdf_handler)

updater.start_polling()
