from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = '7249517311:AAFKEqGOkugTiEmeXQ6Q3LrC1ValfilLgv8'

def start(update, context):
    message = ('Ман Баҳромов Саидҷон. Хуш омадед ба боти ман!')

    keyboard = [
        [InlineKeyboardButton('Контакты', callback_data='contact')],
        [InlineKeyboardButton('Суҳбат', callback_data='talk')],
        [InlineKeyboardButton('Messenger', callback_data='messed')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    with open('photo.jpg', 'rb') as file:
        update.message.reply_photo(file, message, reply_markup = reply_markup)

def main_page(update, context):
    message = ('Ман Баҳромов Саидҷон. Хуш омадед ба боти ман!')
    keyboard = [
        [InlineKeyboardButton('Контакты', callback_data='contact')],
        [InlineKeyboardButton('Суҳбат', callback_data='talk')],
        [InlineKeyboardButton('Messenger', callback_data='messed')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    quety = update.callback_query
    quety.edit_message_caption(message, reply_markup)

def contact(update, context):
    message = '+992 988851282 \n+992 100300658'
    quety = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Назад', callback_data='main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    quety.edit_message_caption(message, reply_markup = reply_markup)

def talk(update, context):
    message = 'Ман ҳоло ҷавоб дода наметавонам!'
    quety = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Назад', callback_data='main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    quety.edit_message_caption(message, reply_markup = reply_markup)

def messed(update, context):
    
    message = 'Ман дар месенджерҳо'
    quety = update.callback_query
    keyboard = [
        [InlineKeyboardButton('Telegram', url='https://t.me/saidjonbahromov'),
         InlineKeyboardButton('Whathapp', url='https://whatsapp.com/dl/code=gb1JTMJy2Y')],
         [InlineKeyboardButton('Назад', callback_data='main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    quety.edit_message_caption(message, reply_markup = reply_markup)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('contact', contact))
    dispatcher.add_handler(CommandHandler('talk', talk))
    dispatcher.add_handler(CallbackQueryHandler(contact, pattern='contact'))
    dispatcher.add_handler(CallbackQueryHandler(main_page, pattern='main'))
    dispatcher.add_handler(CallbackQueryHandler(talk, pattern='talk'))
    dispatcher.add_handler(CallbackQueryHandler(messed, pattern='messed'))  
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()