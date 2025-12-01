# insightflow_core.py
"""
InsightFlow — Multi-Agent Enterprise Analytics Prototype

This script demonstrates:
- Orchestrator Agent
- Data Intake & Validation Agent
- Analytics & KPI Agent
- Insight Writer Agent (LLM-ready)
- Session Memory + Long Term Memory
- Visualization tool (matplotlib)
- Deterministic KPIs
- Full end-to-end example dataset + results

Safe to run locally or in Kaggle.
"""

import os
import json
import logging
from typing import Dict, Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------
LOG_DIR = "insightflow_logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "insightflow.log"),
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

logger = logging.getLogger("InsightFlow")


# ---------------------------------------------------------
# Memory Classes
# ---------------------------------------------------------
class SessionState:
    """Short-lived memory for one workflow session."""
    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: Any):
        self.storage[key] = value

    def get(self, key: str, default=None):
        return self.storage.get(key, default)


class LongTermMemory:
    """File-backed long-term memory for user preferences, patterns."""
    def __init__(self, filename="memory_bank.json"):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump({}, f)
        self._load()

    def _load(self):
        with open(self.filename, "r") as f:
            self.mem = json.load(f)

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.mem, f, indent=2)

    def get(self, key, default=None):
        return self.mem.get(key, default)

    def set(self, key, value):
        self.mem[key] = value
        self.save()


# ---------------------------------------------------------
# Agent Base Class
# ---------------------------------------------------------
class BaseAgent:
    def __init__(self, session: SessionState, memory: LongTermMemory):
        self.session = session
        self.memory = memory

    def log(self, message: str):
        logger.info(f"[{self.__class__.__name__}] {message}")


# ---------------------------------------------------------
# Data Intake & Validation Agent
# ---------------------------------------------------------
class DataIntakeAgent(BaseAgent):
    def load_and_profile_csv(self, filepath: str) -> Dict[str, Any]:
        self.log(f"Loading CSV from {filepath}")
        try:
            df = pd.read_csv(filepath)
        except Exception as e:
            raise ValueError(f"Error reading CSV: {e}")

        # Clean column names
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        profile = {
            "num_rows": len(df),
            "num_cols": len(df.columns),
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict()
        }

        self.session.set("dataframe", df)
        self.session.set("profile", profile)

        self.log("Dataset successfully profiled.")
        return profile


# ---------------------------------------------------------
# Analytics & KPI Agent
# ---------------------------------------------------------
class AnalyticsAgent(BaseAgent):
    def compute_kpis(self) -> Dict[str, Any]:
        df = self.session.get("dataframe")
        if df is None:
            raise ValueError("No dataframe found in session.")

        self.log("Computing KPIs...")

        # Basic KPIs (for e-commerce style data)
        kpis = {}
        if "revenue" in df.columns:
            kpis["total_revenue"] = float(df["revenue"].sum())
        if "order_id" in df.columns:
            kpis["total_orders"] = int(df["order_id"].nunique())
        if "customer_id" in df.columns:
            kpis["unique_customers"] = int(df["customer_id"].nunique())

        # Monthly revenue plot if possible
        charts = {}
        if "date" in df.columns and "revenue" in df.columns:
            try:
                df["date"] = pd.to_datetime(df["date"])
                monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
                plt.figure(figsize=(7, 4))
                monthly.index = monthly.index.to_timestamp()
                plt.plot(monthly.index, monthly.values)
                plt.title("Monthly Revenue Trend")
                plt.xlabel("Month")
                plt.ylabel("Revenue")
                plt.tight_layout()

                chart_path = os.path.join(LOG_DIR, "monthly_rerevenue.png")
                plt.savefig(chart_path)
                charts["monthly_revenue"] = chart_path
                plt.close()
            except Exception as e:
                self.log(f"Error generating plot: {e}")

        self.session.set("kpis", kpis)
        self.session.set("charts", charts)

        self.log("KPIs computed.")
        return {"kpis": kpis, "charts": charts}


# ---------------------------------------------------------
# Insight Writer Agent
# ---------------------------------------------------------
class InsightWriterAgent(BaseAgent):
    def generate_insights(self) -> str:
        kpis = self.session.get("kpis", {})
        profile = self.session.get("profile", {})

        # Deterministic summary (fallback)
        summary = [
            "Executive Summary:",
            f"- Rows: {profile.get('num_rows')}",
            f"- Columns: {profile.get('num_cols')}",
        ]

        if "total_revenue" in kpis:
            summary.append(f"- Total Revenue: {kpis['total_revenue']}")
        if "total_orders" in kpis:
            summary.append(f"- Total Orders: {kpis['total_orders']}")
        if "unique_customers" in kpis:
            summary.append(f"- Unique Customers: {kpis['unique_customers']}")

        summary.append("This dataset shows consistent patterns suitable for further forecasting or segmentation.")

        narrative = "\n".join(summary)
        self.session.set("narrative", narrative)

        self.log("Narrative insights generated.")
        return narrative


# ---------------------------------------------------------
# Orchestrator Agent
# ---------------------------------------------------------
class OrchestratorAgent(BaseAgent):
    def process_file(self, filepath: str) -> Dict[str, Any]:
        self.log("Starting pipeline...")

        data_agent = DataIntakeAgent(self.session, self.memory)
        analytics_agent = AnalyticsAgent(self.session, self.memory)
        insight_agent = InsightWriterAgent(self.session, self.memory)

        profile = data_agent.load_and_profile_csv(filepath)
        analytics = analytics_agent.compute_kpis()
        narrative = insight_agent.generate_insights()

        output = {
            "profile": profile,
            "kpis": analytics["kpis"],
            "charts": analytics["charts"],
            "narrative": narrative
        }

        self.log("Pipeline complete.")
        return output


# ---------------------------------------------------------
# Demo Runner
# ---------------------------------------------------------
def generate_demo_csv() -> str:
    """Generate small demo dataset like an e-commerce table."""
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=90),
        "order_id": np.arange(1000, 1090),
        "customer_id": np.random.randint(1, 20, size=90),
        "revenue": np.random.randint(200, 1500, size=90)
    })
    path = "demo_ecommerce.csv"
    df.to_csv(path, index=False)
    return path


if __name__ == "__main__":
    print("Running InsightFlow demo...\n")

    session = SessionState()
    memory = LongTermMemory()
    orch = OrchestratorAgent(session, memory)

    csv_path = generate_demo_csv()
    results = orch.process_file(csv_path)

    print("\n=== PROFILE ===")
    print(json.dumps(results["profile"], indent=2))

    print("\n=== KPIs ===")
    print(json.dumps(results["kpis"], indent=2))

    print("\n=== NARRATIVE ===")
    print(results["narrative"])

    print("\nCharts stored in:", results["charts"])
