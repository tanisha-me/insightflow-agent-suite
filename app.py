# app.py
"""
Simple Flask wrapper exposing InsightFlow as a minimal API.
Use for Cloud Run deployment or local testing.
DO NOT expose any API keys or secrets in the repo.
"""

import os
import tempfile
from flask import Flask, request, jsonify
from insightflow_core import SessionState, LongTermMemory, OrchestratorAgent

app = Flask(__name__)

# Create a simple singleton orchestrator for demo
SESSION = SessionState()
LTM = LongTermMemory()
ORCH = OrchestratorAgent(SESSION, LTM)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "name": "InsightFlow API"})

@app.route("/analyze-file", methods=["POST"])
def analyze_file():
    """
    Expects a multipart/form-data with 'file' field (CSV).
    Returns JSON with KPI summary and narrative.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Please upload a CSV file as 'file'"}), 400
    f = request.files['file']
    # Save temp file
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    f.save(tmp.name)
    tmp.flush()
    try:
        package = ORCH.process_file(tmp.name)
        # Remove dataframes / binary if large; keep summary
        result = {
            "profile": package["profile"],
            "kpis": package["kpis"],
            "narrative": package["narrative"],
            "charts": package.get("charts", {}),
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        try:
            os.unlink(tmp.name)
        except Exception:
            pass

if __name__ == "__main__":
    # For local testing
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
