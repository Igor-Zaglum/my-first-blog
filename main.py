from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext


# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его.")


# Функция для обработки входящих текстовых сообщений
async def echo(update: Update, context: CallbackContext):
    user_message = update.message.text
    await update.message.reply_text(user_message)


def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    token = "7994074439:AAFydcUD9bV-uK42oQEJiLBRWELij9MjUTE"

    # Создаем объект Application
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()