import os
import fitz  # PyMuPDF
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

RESULTS_DIR = "results"
user_data = {}

# /start command – show semester list
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(sem.replace(".pdf", ""), callback_data=sem)]
        for sem in sorted(os.listdir(RESULTS_DIR))
        if sem.endswith(".pdf")
    ]
    await update.message.reply_text(
        "📚 Please choose a semester:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

# Handle semester selection
async def semester_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_data[query.from_user.id] = {"semester": query.data}
    await query.message.reply_text("🆔 Please enter your Hall Ticket Number:")

# Handle hall ticket input
async def handle_hallticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    htno = update.message.text.strip().upper()

    if user_id not in user_data:
        await update.message.reply_text("❗ Please select a semester first using /start.")
        return

    semester_file = user_data[user_id]["semester"]
    pdf_path = os.path.join(RESULTS_DIR, semester_file)
    results = extract_results_from_pdf(pdf_path, htno)

    if results:
        reply = f"📄 *Results for `{htno}` - {semester_file.replace('.pdf', '')}*\n\n"
        for res in results:
            reply += (
                f"📘 *{res['Subcode']} - {res['Subname']}*\n"
                f"📎 Internals: `{res['Internals']}` | Grade: `{res['Grade']}` | Credits: `{res['Credits']}`\n\n"
            )
    else:
        reply = f"⚠️ No result found for Hall Ticket Number: `{htno}`"

    await update.message.reply_markdown(reply)

# 🧠 New parser for vertical line-based data
def extract_results_from_pdf(pdf_path, htno):
    results = []
    doc = fitz.open(pdf_path)

    for page in doc:
        lines = [line.strip() for line in page.get_text().split("\n") if line.strip()]
        i = 0
        while i < len(lines) - 5:
            current_htno = lines[i]
            if current_htno == htno:
                result = {
                    "Subcode": lines[i + 1],
                    "Subname": lines[i + 2],
                    "Internals": lines[i + 3],
                    "Grade": lines[i + 4],
                    "Credits": lines[i + 5]
                }
                results.append(result)
            i += 6  # Go to the next block
    return results

# 🚀 Run the bot
def main():
    token = "BOT TOKEN"  # Replace with your bot token
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(semester_selected))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_hallticket))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
