# 🦙 LlamaLens – AI-Powered API Debugger  
**Built for FutureStack GenAI Hackathon**  
*By Swayam Prakash Sahu*  

---

## 🚀 Overview  

**LlamaLens** is an AI-powered **API Debugger** that helps developers instantly understand and fix issues in API responses, logs, or error messages.  

Just paste your API response or log snippet — and **LlamaLens**, powered by **Meta’s Llama 4 (Scout 17B)** via **Cerebras Cloud**, analyzes it in real time, explains what went wrong in plain English, and suggests possible fixes.  

Containerized with **Docker**, it’s portable, easy to run anywhere, and showcases integration of multiple sponsor technologies (Meta + Docker + Cerebras).  

---

## 💡 Problem Statement  

Debugging APIs is time-consuming. Developers often face cryptic error messages, inconsistent logs, or poorly documented endpoints.  
LlamaLens acts as your **AI debugging companion**, simplifying the process using generative AI reasoning.  

---

## 🎯 Key Features  

✅ Paste any API response or log and get instant insights  
✅ Human-readable explanation of the issue  
✅ Fix suggestions, code hints, and API best practices  
✅ Powered by **Meta Llama 4 (Scout 17B)** via **Cerebras Cloud SDK**  
✅ Portable via **Docker MCP Gateway** – runs anywhere in one command  
✅ Streamlit UI for smooth local or web demo  

---

## 🧠 Tech Stack  

| Layer | Technology |
|-------|-------------|
| **AI Model** | Meta Llama 4 Scout 17B (Instruct) |
| **AI Platform** | Cerebras Cloud SDK |
| **Frontend/UI** | Streamlit |
| **Containerization** | Docker |
| **Language** | Python 3.10 |
| **Deployment (optional)** | Render / Hugging Face Spaces |

---

## 🧩 Architecture  

```
          ┌─────────────────────────────┐
          │        User (Developer)     │
          │  Paste API response/logs    │
          └──────────────┬──────────────┘
                         │
                         ▼
                ┌────────────────────┐
                │   Streamlit UI     │
                │  (app.py frontend) │
                └────────┬───────────┘
                         │
                         ▼
                ┌────────────────────┐
                │  llama_client.py   │
                │ Cerebras SDK calls │
                └────────┬───────────┘
                         │
                         ▼
          ┌────────────────────────────────────┐
          │   Cerebras Cloud – Llama 4 Scout   │
          │   Meta’s 17B Instruct Model        │
          └────────────────────────────────────┘
```

---

## 📁 Project Structure  

```
llama-lens/
│
├── app.py                     # Streamlit UI
├── llama_client.py             # Llama 4 Cerebras API wrapper
├── utils.py                    # Helper utilities
├── Dockerfile                  # Docker container setup
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
└── assets/
    └── architecture.png         # Architecture diagram (optional)
```

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/yourusername/llama-lens.git
cd llama-lens
```

---

### 2️⃣ Create and Activate Virtual Environment  

**Mac/Linux:**  
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**  
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies  

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variable  

You need a **Cerebras Cloud API Key** (sign up on [Cerebras Cloud](https://cloud.cerebras.ai)).  

```bash
export CEREBRAS_API_KEY="your_cerebras_api_key_here"
```

*(On Windows PowerShell)*  
```bash
setx CEREBRAS_API_KEY "your_cerebras_api_key_here"
```

---

### 5️⃣ Run the Application  

```bash
streamlit run app.py
```

Then open in your browser →  
👉 **http://localhost:8501**

---

## 🧪 How to Test the App  

Once the app loads, you’ll see:  
> “🦙 LlamaLens – AI-Powered API Debugger”

Paste this into the text area:  

```json
{"error": "401 Unauthorized", "message": "Invalid API token"}
```

Click **Analyze with Llama 🧠**

You should see something like:  
> The API returned a 401 Unauthorized error.  
> ✅ Fix: Check your authentication header or refresh your token.  

---

## 🧠 Backend Verification  

To verify Cerebras integration:  

Add a debug print inside `llama_client.py`:
```python
print("✅ Calling Llama API via Cerebras...")
```

Run again — you should see this printed each time you click **Analyze**.

---

## 🐳 Run with Docker (Sponsor Track: Docker MCP)  

### Build the Image  

```bash
docker build -t llama-lens .
```

### Run the Container  

```bash
docker run -e CEREBRAS_API_KEY=$CEREBRAS_API_KEY -p 8501:8501 llama-lens
```

Then open → [http://localhost:8501](http://localhost:8501)

This proves your app runs in a **portable, sponsor-compliant** containerized environment.  

---

## 🧪 Health Check (Optional)  

You can run a quick backend test:  

```bash
python health_check.py
```

Output:  
```
✅ Llama response: The API returned 404 Not Found. This means the requested endpoint does not exist...
```

---

## 🧱 Example Project Workflow  

1️⃣ User pastes an API response or log in Streamlit UI  
2️⃣ The app calls `call_llama()` → sends request to Cerebras Cloud  
3️⃣ Meta Llama 4 Scout processes and returns human-readable explanation  
4️⃣ Streamlit displays suggested fixes and debug reasoning  

---

## 🏅 Hackathon Deliverables  

| Item | Description |
|------|--------------|
| **GitHub Repo** | Contains code, commits, and README |
| **2-Minute Demo Video** | Show app usage, explanation, and Docker run |
| **(Optional)** Deployment | Host on Render / Hugging Face Spaces |
| **Sponsor Techs Used** | Meta Llama 4 + Cerebras SDK + Docker |

---

## 🎥 Demo Video Script (Suggestion)  

1. **Intro (10 s)** – “Hi, I’m Swayam, and this is LlamaLens.”  
2. **Show app** – Paste API error → click **Analyze**  
3. **Explain output** – Llama suggests fix  
4. **Show Docker run** – `docker build` + `docker run`  
5. **End** – Show architecture diagram + GitHub link  

---

## 🧠 Design Principles  

- 🧩 Modular Code (UI, Logic, Helpers separated)  
- 🔐 Secure – API key via environment variable  
- ⚡ Fast – Uses Cerebras streaming API  
- 🐳 Portable – Dockerized for reproducibility  
- 🧹 Clean – PEP 8 style and docstrings  

---

## 🧰 Dependencies  

| Library | Purpose |
|----------|----------|
| **Streamlit** | UI frontend |
| **Cerebras-Cloud-SDK** | Llama 4 API access |
| **Requests** | HTTP helper |
| **Python 3.10+** | Core runtime |

Install all via:  
```bash
pip install -r requirements.txt
```

---

## 💬 Example Interaction  

**Input:**  
```json
{"status":500,"error":"Internal Server Error","message":"Cannot parse JSON input"}
```

**LlamaLens Output:**  
> The API returned a 500 error because the server couldn’t parse the request body.  
> ✅ Fix: Ensure valid JSON formatting and `Content-Type: application/json` header.  

---

## 📦 Future Improvements  

🚀 Add support for file uploads (log files)  
💬 Integrate syntax-highlighted explanations  
📊 Visualize frequent API issues using charts  
🔗 Support multiple LLM providers (Cerebras, OpenAI, Anthropic)  

---

## 📜 License  

MIT License © 2025 Swayam Prakash Sahu  
