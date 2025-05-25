# 🤖 ghost-gpt

**Personal AI assistant bot for Telegram using OpenAI’s GPT API**

This Telegram bot lets you chat privately with OpenAI's language models (like GPT-4 or GPT-3.5). It responds only to an authorized user and can be extended with more features.

---

## 🚀 Features

- Secure and private — responds only to one user
- Powered by OpenAI’s Chat Completions API
- Easy local setup using `.env` for credentials

---

## 🛠 Requirements

- Python 3.8+
- Telegram bot token
- OpenAI API key
- Your Telegram numeric user ID (chat ID)

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ghost-gpt.git
cd ghost-gpt
```

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root with the following content:

```env
TELEGRAM_TOKEN=your-telegram-bot-token
OPENAI_API_KEY=your-openai-api-key
AUTHORIZED_USER_ID=your-telegram-chat-id
```

Replace the values with your actual credentials.

---

## ▶️ Running the Bot

Start the bot by running:

```bash
python main.py
```

Once it's running, send a message to your Telegram bot from the authorized user (yourself), and it will reply using the OpenAI API.

---

## 🧪 Example

```
You: What's the capital of France?
Bot: The capital of France is Paris.
```

---

## 🧾 License

This project is open-source and licensed under the MIT License.

---

## 💡 Notes

- Only the Telegram user ID specified in `.env` can interact with the bot.
- The bot defaults to `gpt-4`. Change the model in `main.py` if needed.

---

## 🏗 Future Ideas

- Command handling (`/help`, `/reset`, etc.)
- Chat history/memory
- Cloud deployment (e.g., Railway, Render, etc.)

---

**Enjoy your private GPT assistant!**
