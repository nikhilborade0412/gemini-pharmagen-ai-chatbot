
# 💊 PharmaGen AI  
### Production-Ready Pharmaceutical Industry Assistant (Powered by Nikhil Borade)

PharmaGen AI is a domain-specific, production-grade GenAI chatbot designed to assist users with pharmaceutical industry knowledge.  
It leverages Google's Gemini 2.5 model and is built with a modular architecture suitable for real-world deployment.

---

## 🚀 Project Overview

PharmaGen AI simulates a real-world Generative AI production system with:

- ✅ Proper Gemini API integration
- ✅ Multi-turn conversation memory
- ✅ Advanced prompt engineering
- ✅ Streamlit interactive UI
- ✅ Secure API key handling
- ✅ Clean modular code structure
- ✅ Deployment-ready architecture

This chatbot is restricted strictly to pharmaceutical industry topics.

---

## 🏗 System Architecture

```

User (Browser)
↓
Streamlit UI
↓
Application Layer (Python Backend)
↓
Conversation Memory Manager
↓
Prompt Engineering Layer
↓
Gemini 2.5 Flash Model
↓
Response Output

```

---

## 🧠 Features

### 🔹 Domain-Specific Intelligence
PharmaGen AI only answers questions related to:
- Drug Development Lifecycle
- GMP & GLP Guidelines
- Pharmaceutical Manufacturing
- QA / QC Processes
- Regulatory Authorities (FDA, WHO, CDSCO, EMA)
- Pharmacopeia Standards

### 🔹 Multi-Turn Memory
Maintains session-based chat history for contextual responses.

### 🔹 Secure API Integration
Uses `.env` file for environment-based API key management.

### 🔹 Production-Level Structure
```

pharmagen-ai/
│
├── app.py
├── chatbot/
│   ├── gemini_client.py
│   ├── memory_manager.py
│   ├── prompt_builder.py
│
├── .env
├── requirements.txt
└── README.md

````

---

## ⚙️ Tech Stack

- Python 3.12
- Streamlit
- Google GenAI SDK
- Gemini 2.5 Flash Model
- dotenv (Environment variable management)

---

## 🔐 Environment Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd pharmagen-ai
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

Windows:

```bash
myenv\Scripts\activate
```

Mac/Linux:

```bash
source myenv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file:

```bash
pip install streamlit google-genai python-dotenv
```

---

### 4️⃣ Configure Environment Variables


```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application runs on:

```
http://localhost:8501
```

---

## 🧪 Example Queries

* What is GMP in pharmaceutical manufacturing?
* Explain drug development lifecycle.
* What is the role of FDA in drug approval?
* What is pharmacopeia?

---

## ⚠️ Limitations

* Does NOT provide medical diagnosis.
* Does NOT provide treatment advice.
* Restricted to pharmaceutical industry knowledge only.

---

## ☁️ Deployment (AWS EC2 Ready)

PharmaGen AI is fully deployable on:

* AWS EC2
* Render
* Railway
* Azure VM
* GCP VM

Run using:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

---

## 🛡 Security Considerations

* API keys stored in `.env`
* `.gitignore` configured
* No hardcoded credentials
* Domain-restricted prompt enforcement

---

## 📌 Future Improvements

* Database-backed persistent memory
* User authentication
* Role-based access
* Logging & monitoring
* CI/CD integration
* Custom frontend framework
* Docker containerization

---

## 👨‍💻 Author

Nikhil Borade
Computer Science Graduate | AI & Data Science Enthusiast

---

## 📄 License

This project is developed for educational and demonstration purposes.


---
