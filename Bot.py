
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Вітаємо! Це бот контролю електроенергії "
        "на вулиці Леся Курбаса, 4.\n\n"
        "Я допоможу відстежувати відключення світла!\n\n"
        "Доступні команди:\n"
        "/status — стан електроенергії\n"
        "/stats — статистика відключень\n"
        "/schedule — графік відключень"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Поки немає підключення до датчика електроенергії.\n"
        "Незабаром я зможу визначати наявність світла!"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Статистика відключень поки збирається."
    )

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Графік відключень незабаром з'явиться!"
    )

def main():
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("schedule", schedule))

    app.run_polling()

if __name__ == "__main__":
    main()
