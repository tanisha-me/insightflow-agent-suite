# InsightFlow - Enterprise Agent Suite

Orchestrated agents that automate the analytics lifecycle from raw CSV files to decision-ready insights.

InsightFlow is a multi-agent analytics system designed to automate repetitive data tasks such as ingestion, cleaning, KPI computation, chart generation, and executive summarization. It mirrors the workflow of an enterprise analytics team through coordinated agents, deterministic tooling, session memory, and structured orchestration.

This project was created as part of the Kaggle × Google AI Agents Intensive Capstone (2025).

---

## Features Demonstrated

This project demonstrates multiple required concepts for the capstone:

### Multi-Agent Architecture
- Orchestrator Agent  
- Data Intake & Validation Agent  
- Analytics & KPI Agent  
- Insight Writer Agent  

### Tool Usage
Custom Python tools:
- CSV ingestion and profiling  
- KPI computation  
- Plot generation  

Built-in tools:
- Python execution  
- File handling  

### Memory
- Short-term SessionState memory  
- Long-term Memory Bank (file-backed)  

### Observability
- Logging of tool runs  
- Agent transitions  
- Memory updates  
- Validation loops  

### Optional LLM/Gemini Integration
`llm_tools.py` contains a safe wrapper where Gemini or other LLM providers can be integrated via environment variables.

---

## Repository Structure

```
insightflow-agent-suite/
├── insightflow_core.py
├── llm_tools.py
├── adk_example.py
├── requirements.txt
├── README.md
├── thumbnail_560x280.png
├── architecture.png
└── workflow.png
└── insightflow_kaggle.ipynb  (optional)
```

---

## Running the Demo

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full pipeline:

```bash
python insightflow_core.py
```

This will:

1. Generate a demo e-commerce dataset  
2. Profile and clean the data  
3. Compute KPIs  
4. Generate charts  
5. Produce an executive summary  
6. Save logs and charts to `insightflow_logs/`

---

## LLM / Gemini Integration 

LLM integration is optional but supported.

To enable it:

1. Open `llm_tools.py`  
2. Insert your Gemini / Vertex API call inside `call_llm_generate()`  
3. Set your environment variable:

```bash
export GEMINI_API_KEY="your_key_here"
```

If no key is set, InsightFlow falls back to a deterministic template summary.

---

## ADK / A2A Conceptual Mapping (Bonus)

`adk_example.py` includes a structured mapping of InsightFlow’s architecture into:

- ADK Agents  
- Tool servers  
- A2A orchestration  
- Loop Agents  
- Memory services  

Though not executed directly, it shows how this prototype would translate to the official ADK framework.

---

## Deployment 

A minimal Flask API is provided (`app.py`) and a `Dockerfile` is included for deployment to:

- Google Cloud Run  
- Any Docker-based hosting  
- Local execution  

Developers can expose the pipeline via:

```
POST /analyze-file
```

which accepts a CSV and returns KPIs, charts, and narrative.

---

## Live demo & outputs

- KPI summary (generated): `kpi_summary.png`  
- Monthly revenue chart (generated): `monthly_rerevenue.png` *(typo retained if present; consider renaming to `monthly_revenue.png`)*

You can view these files in this repository.

---

## Features implemented

- **Multi-Agent pattern**: Orchestrator + Data Intake & Validation + Analytics & KPI + Insight Writer.  
- **Tool usage**: Python execution tools for deterministic KPI computation and chart generation.  
- **Memory & session state**: Basic session memory model for conversational follow-ups (illustrative).  
- **Observability**: Simple logging and output artifacts saved to `insightflow_logs/`.

---

## Repo structure

## Author

**Komal Meena**  
B.S.in Data Science & Applications - IIT Madras  
Kaggle × Google AI Agents Intensive (2025)

---

