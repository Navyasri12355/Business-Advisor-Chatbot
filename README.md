# 💼 Business Advisor Chatbot

An AI-powered chatbot built using Streamlit and Google's Gemini API (Generative AI) to help users with business-related queries. It provides insights and advice on topics like finance, marketing, strategy, startups, and more.

## 🚀 Features

- Conversational AI assistant focused on business advice
- Powered by Google's Gemini (Generative AI) models
- Context-aware responses using conversation history
- Business-topic detection to keep the chatbot focused
- Easy-to-use Streamlit interface
- Special commands: `exit`, `quit`, `clear` to manage sessions

## 🧠 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Model**: Google Generative AI (`gemini-2.0-flash-thinking-exp`)
- **Language**: Python 3

## 📦 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/business-advisor-chatbot.git
   cd business-advisor-chatbot
   
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Set up your API Key:**
   - Create a .streamlit/secrets.toml file in the root of your project.
   - You can get an API key by signing up at Google AI Studio.
   - Add your Google Generative AI API key:
   ```bash
   GOOGLE_API_KEY = "your-api-key-here"
   
5. **Run the chatbot:**
   ```bash
   streamlit run app.py

---

## ✨ How to Use
- Ask questions related to business (marketing, finance, startups, etc.)
- Type clear to reset the conversation.
- Type exit, quit, or bye to end the session.
- Non-business queries are politely filtered out.

---

## 📝 Example Queries
- "How can I grow my startup with limited funds?"
- "Give me a marketing strategy for a new product launch."
- "What are the best investment options in 2025?"
- "How do I manage cash flow in a small business?"

---

## 📌 Notes
- Only business-related queries will be accepted.
- The conversation history is retained for context during the session.
