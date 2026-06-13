import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ParseMode

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ Produkte entdecken", callback_data="shop")],
        [InlineKeyboardButton("📖 Unsere Geschichte", callback_data="story")],
        [InlineKeyboardButton("🎨 Brand Farben", callback_data="colors")],
        [InlineKeyboardButton("📁 Brand Assets", callback_data="assets")]
    ]
    
    await update.message.reply_text(
        "🤍 *Willkommen bei Elian & Co.*\n\n"
        "Nachhaltige Premium-Produkte für dein kleines Wunder.\n"
        "Made with Love, for little ones. 🌿",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "colors":
        await query.edit_message_text(
            "🌈 *Elian & Co. Farbpalette*\n\n"
            "• Zartrosa `#EECCC9` (Herz, CTA)\n"
            "• Himmelblau `#B4C5D0` (Elian)\n"
            "• Salbeigrün `#C0C8B9` (Natürliches)\n\n"
            "Liebevoll • Nachhaltig • Premium",
            parse_mode=ParseMode.MARKDOWN
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤍 Elian & Co. Bot gestartet...")
    app.run_polling()

if __name__ == "__main__":
    main()
