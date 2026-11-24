
import os
import logging
from telegram import Update, LabeledPrice
from telegram.ext import (
    Application,
    CommandHandler,
    PreCheckoutQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

# Создаём магазин
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = [
        [LabeledPrice("Тестовый товар", 10)]
    ]

    await update.message.reply_text(
        "🔥 Добро пожаловать в Robux Shop!\n\n"
        "Нажми кнопку ниже, чтобы посмотреть тестовую оплату."
    )

    await context.bot.send_invoice(
        chat_id=update.effective_chat.id,
        title="Тестовый заказ",
        description="Проверка оплаты Telegram Stars",
        payload="test_order",
        provider_token="",
        currency="XTR",
        prices=prices,
    )

async def precheckout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.pre_checkout_query.answer(ok=True)

async def successful_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ Оплата получена! Спасибо за заказ."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(PreCheckoutQueryHandler(precheckout))
    app.add_handler(
        MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
