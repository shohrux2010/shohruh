from telegram.ext import Application, CommandHandler, ContextTypes

# Bu yerga o'zingizning yangi tokeningizni qo'ying!
TOKEN = "YOUR_BOT_TOKEN_HERE"

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! 👋 Men sizning yangi botingizman.")

# Asosiy funksiya
def main():
    app = Application.builder().token(TOKEN).build()

    # /start komandasi qo‘shiladi
    app.add_handler(CommandHandler("start", start))

    # Botni ishga tushirish
    app.run_polling()

if __name__ == "__main__":
    main()