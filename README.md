# 🤖 NeoStats AI Chatbot – RAG + Web Search

An intelligent chatbot built using **Streamlit, LangChain, and Groq LLM** that can answer questions using **document knowledge (RAG)** and **live web search**.

---

# 🚀 Features

- 💬 Conversational AI chatbot  
- 📄 Retrieval Augmented Generation (RAG) using local documents  
- 🌐 Live Web Search for real-time information  
- ⚡ Powered by Groq LLM (LLaMA 3.1)  
- 🧠 Vector embeddings for semantic document search  
- 🎛 Response Modes:
  - Concise answers
  - Detailed explanations
- 🖥 Interactive UI using Streamlit  

---

# 🏗 Architecture

User Query  
↓  
Streamlit UI  
↓  
LangChain Processing  
↓  
Groq LLM  
↓  
Optional Tools  
- RAG Document Search  
- Web Search  
↓  
Final AI Response

---

# 📂 Project Structure

```
AI_UseCase/
│
├── app.py
├── requirements.txt
│
├── config/
│     └── config.py
│
├── models/
│     ├── llm.py
│     └── embeddings.py
│
├── utils/
│      ├── rag.py
│      └── web_search.py
│
└── README.md
```

---

# ⚙️ Installation

- Clone the repository

```
git clone https://github.com/YOUR_USERNAME/neostats-ai-chatbot.git

```
```

cd neostats-ai-chatbot

```

- Create virtual environment

```
python -m venv venv

```
- Activate environment

  Windows:
  
```
venv\Scripts\activate
```

- Install dependencies
```
pip install -r requirements.txt
```

---

# 🔑 API Key Setup

Create a `.env` file in the project root and add:

```
GROQ_API_KEY=your_api_key_here
```

You can generate the API key from the **Groq Console**.

---

# ▶️ Run the Application

```
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

# ☁️ Deployment

You can deploy the application using **Streamlit Cloud**.

Steps:

1. Push the project to GitHub
2. Open Streamlit Cloud
3. Click **New App**
4. Select your repository
5. Choose `app.py` as the main file
6. Add the API key in **Secrets**
```
GROQ_API_KEY="your_api_key"
```


---

# 🧪 Example Use Cases

- AI Study Assistant  
- Interview Preparation Chatbot  
- Research Knowledge Assistant  
- Company Policy Assistant  

---

# 🛠 Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- FAISS Vector Database
- HuggingFace Embeddings
- DuckDuckGo Web Search

---

# 📊 Key Concepts Implemented

- Retrieval Augmented Generation (RAG)
- Semantic Search using Embeddings
- Tool Integration with LLM
- Prompt Engineering
- Modular Python Architecture

---

# 🚧 Challenges Faced

- Integrating RAG with Streamlit UI  
- Managing embeddings efficiently  
- Handling API key security in deployment  
- Combining web search with LLM responses  

---

# ⭐ Future Improvements

- Multi-document support (PDF, DOCX)  
- Conversation memory  
- Advanced AI agents  
- UI improvements  
- Multi-LLM support  

---

# 📜 License

This project is for educational and demonstration purposes.
