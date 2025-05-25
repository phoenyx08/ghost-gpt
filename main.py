# Dependencies
# pip install python-telegram-bot openai
# pip install python-dotenv

# Environment
# export TELEGRAM_TOKEN="your-telegram-token"
# export OPENAI_API_KEY="your-openai-key"
# export AUTHORIZED_USER_ID="123456789"

from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from dotenv import load_dotenv
load_dotenv()

import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AUTHORIZED_USER_ID = int(os.getenv("AUTHORIZED_USER_ID"))

# openai.api_key = OPENAI_API_KEY

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    await update.message.reply_text("Hello! I'm your private ChatGPT bot.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    user_input = update.message.text

    response = client.chat.completions.create(
        model="gpt-4.1",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()