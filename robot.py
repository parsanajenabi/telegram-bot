import json
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
usernames = []
try:
    with open("usernames.json", "rt", encoding="utf-8") as f:
        usernames_data = json.load(f)
        usernames.extend(usernames_data)
except:
    pass
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
def save_username(update: Update):
    user = update.effective_user
    if user and user.username:
        if user.username not in usernames:
            usernames.append(user.username)
            with open("usernames.json", "wt", encoding="utf-8") as f:
                f.write(json.dumps(usernames))
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    save_username(update)
    user = update.effective_user
    await update.message.reply_html(rf"Hi {user.mention_html()}!")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    save_username(update)
    await update.message.reply_text("Help!")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    save_username(update)
    text = update.message.text.lower()
    if text == "hi":
        await update.message.reply_text("hello friend")
    elif text == "bye":
        await update.message.reply_text("bye")
    else:
        await update.message.reply_text(update.message.text)
def main() -> None:
    application = Application.builder().token("YOUR BOT TOKEN").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()
if __name__ == "__main__":
    main()