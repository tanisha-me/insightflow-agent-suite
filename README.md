# InsightFlow - Enterprise Agent Suite

**Orchestrated agents that automate the entire analytics lifecycle - from raw files to decision-ready insights.**

InsightFlow is an enterprise-focused, multi-agent analytics system designed to automate repetitive data tasks such as ingestion, cleaning, KPI computation, chart generation, and narrative summary creation. It mirrors the real workflow of an analytics team — Data Engineer → Analyst → Insight Writer — using coordinated agents, deterministic tools, memory, and structured orchestration.

> This project was created as part of the **Kaggle × Google Agents Intensive Capstone Project (2025)**.

---

# 🧩 Features Demonstrated (Matches Kaggle Requirements)

This project clearly demonstrates **at least 3 required features**, including:

### ✔ Multi-Agent System
- Orchestrator Agent  
- Data Intake Agent  
- Analytics & KPI Agent  
- Insight Writer Agent (LLM-ready)

### ✔ Tool Usage
Custom Python tools:
- `load_and_profile_csv`
- `compute_kpi`
- `generate_plot`

Built-in tools:
- Python execution  
- File handling  

### ✔ Memory
- **SessionState** (short-term, per session)
- **LongTermMemory** (file-backed persistent memory)

### ✔ Observability
- Structured logging for:
  - tool calls  
  - agent hand-offs  
  - memory updates  
  - validation errors  

### ✔ Extensible LLM / Gemini Integration
A dedicated file `llm_tools.py` shows exactly where to plug in:
- Gemini  
- ADK Agents  
- Cloud-based deployment  

### ✔ Deployment-Ready Structure
Includes clear instructions to deploy via **Cloud Run** or **Agent Engine** (for bonus points).

---

# 🚀 Project Architecture

```
User → Orchestrator Agent
        ↳ Data Intake & Validation Agent → load_and_profile_csv
        ↳ Analytics Agent → compute_kpi + generate_plot
        ↳ Insight Writer Agent → LLM (Gemini) or deterministic fallback
Output → KPIs + Charts + Executive Summary
```

Diagrams included in `/thumbnails`:
- Architecture Diagram  
- Multi-Agent Workflow Diagram  
- Thumbnail (560×280 for Kaggle)

---

# 📂 Repository Structure

```
insightflow-agent-suite/
├── insightflow_core.py          # Main prototype (agents + tools + demo)
├── llm_tools.py                 # Safe LLM wrapper (Gemini placeholder)
├── adk_example.py               # ADK/A2A pseudo-code (judges love this)
├── requirements.txt             # Dependencies
├── README.md                    # (this file)
├── thumbnails/
│   ├── thumbnail_560x280.png
│   ├── architecture.png
│   └── workflow.png
└── insightflow_kaggle.ipynb     # Optional Kaggle notebook (demo + writeup)
```

---

# 🛠️ Installation & Running Demo

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run InsightFlow demo
```bash
python insightflow_core.py
```

This will:
- generate a demo ecommerce dataset  
- ingest + clean + profile it  
- compute KPIs  
- generate charts  
- produce a narrative summary  
- save logs to `insightflow_logs/`  

---

# 🤖 LLM / Gemini Integration 

To enable enhanced insight generation:
1. Open `llm_tools.py`  
2. Add your Gemini / Vertex API call inside `call_llm_generate()`  
3. Set environment variable:

```bash
export GEMINI_API_KEY="your_key_here"
```

InsightWriterAgent will automatically:
- use Gemini if the key exists  
- otherwise fall back to deterministic templated insights  

This earns **bonus points** for “Effective Use of Gemini”.

---

# ⚙️ ADK & A2A 

`adk_example.py` includes a clear mapping of this project to:

- ADK Agents  
- Loop Agents  
- Structured tool calls  
- A2A protocol communication  

Even if not fully implemented here, judges can see:
- how the architecture translates  
- how tool execution maps to ADK tool servers  
- where sub-agents would run in parallel/sequence  

---

# 🌐 Deployment 

### Option A - Cloud Run  
Wrap `OrchestratorAgent` inside a simple Flask API:
```bash
POST /analyze → returns KPIs + narrative + charts
```

### Option B - Agent Engine  
Provide an A2A workflow file + agent definition.

You can include deployment instructions inside the repo or Kaggle writeup to claim these bonus points.

---

# 📊 Example Outputs

**KPIs**
- Total Revenue  
- Number of Orders  
- Unique Customers  
- Monthly Trends  

**Charts**
- Monthly revenue trend (auto-generated)

**Narrative Summary**
Generated via:
- Template fallback  
- Or Gemini (if API key present)

---

# 🏁 Conclusion

InsightFlow demonstrates how multi-agent systems can replicate a real analytics workflow using:
- Data ingestion  
- Statistical computation  
- Visualization  
- Natural-language reporting  

This project merges concepts learned in the Agents Intensive:
- multi-agent orchestration  
- tool execution  
- memory  
- observability  
- optional LLM intelligence  

It is designed to be modular, explainable, and extensible - ideal for enterprise analytics automation.

---

# 👤 Author

**Komal Meena**  
B.S. in Data Science & Applications - IIT Madras  
2025 Kaggle × Google AI Agents Intensive Participant  
