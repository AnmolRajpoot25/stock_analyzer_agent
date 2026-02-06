# 📊 Financial Analyst Multi-Agent System

An AI-powered **Financial Analyst Agent** built using **Phi (phidata)** and **Groq LLMs**.  
It combines multiple agents to analyze stocks, fetch analyst recommendations, gather latest news, and present results in clean tables with sources.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture**
- 📈 Analyst recommendations (Yahoo Finance)
- 📰 Latest company news
- 🌐 Web search with sources (DuckDuckGo)
- 📊 Table-based financial insights
- ⚡ Groq-powered LLM (fast inference)
- 🔄 Streaming responses

---

## 🧠 Tech Stack

- Python 3.9+
- phidata (phi)
- Groq LLM (llama-3.3-70b)
- Yahoo Finance Tools
- DuckDuckGo Search
- python-dotenv

---

## 📁 Project Structure

```text
practice/
├── financial_agent.py

├── playground.py

├── requirements.txt

├── .env

└── README.md


┌──────────────────────┐
│  Team Agent (Groq)   │
└──────────┬───────────┘
           │
   ┌───────┴────────┐
   │                │
▼ Web Search Agent  ▼ Finance Agent
  (DuckDuckGo)       (Yahoo Finance)




⚙️ Run the Project Locally

Follow these steps to run the project on your local machine.

1️⃣ Clone the Repository
git clone https://github.com/your-username/financial-analyst-agent.git
cd financial-analyst-agent

2️⃣ Create & Activate Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set API Key (Terminal Method – Recommended)

This project uses Groq, so only one API key is required.

Windows (PowerShell)
setx GROQ_API_KEY "your_groq_api_key_here"


Restart the terminal after running this.

Verify:

echo $env:GROQ_API_KEY

macOS / Linux
export GROQ_API_KEY="your_groq_api_key_here"


Verify:

echo $GROQ_API_KEY

5️⃣ (Optional) Using .env File

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here


Make sure this is added at the top of your Python file:

from dotenv import load_dotenv
load_dotenv()

6️⃣ Run the Application 🚀
python financial_agent.py


Example prompt used internally:

Summarize analyst recommendations and share the latest news about NVIDIA.