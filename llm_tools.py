# llm_tools.py
"""
LLM wrapper for InsightFlow.
- Uses environment variable GEMINI_API_KEY if present.
- Placeholder function: replace with actual ADK/Gemini/Vertex call per your credentials.
- Keeps deterministic fallback when no API key present (safe for Kaggle demo).
"""

import os
import json
import logging
from typing import Optional

logger = logging.getLogger("InsightFlow.LLM")
logger.setLevel(logging.INFO)

def call_llm_generate(prompt: str, model: str = "gemini", max_tokens: int = 512) -> str:
    """
    Lightweight wrapper to call an LLM. Replace the internals with your provider SDK.
    Uses env var GEMINI_API_KEY. If not present, returns a deterministic fallback string.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.warning("No GEMINI_API_KEY/OPENAI_API_KEY found. Returning deterministic fallback.")
        # Deterministic fallback: shorten prompt and echo key high-level items
        # Keep it useful but reproducible for judges who run offline
        short = prompt[:800].replace("\n", " ")
        return f"DETERMINISTIC FALLBACK SUMMARY: {short[:800]}"

    # Example pseudocode: replace with real provider call
    # --- PSEUDOCODE START ---
    # from google.cloud import aiplatform
    # client = aiplatform.gapic.PredictionServiceClient()
    # response = client.predict(endpoint=..., instances=[{"prompt": prompt}], parameters=...)
    # return response.predictions[0]['content']
    # --- PSEUDOCODE END ---

    # For safety in this repo, we don't include SDK calls or keys.
    raise NotImplementedError("Insert your LLM provider SDK call here (Gemini/ADK/OpenAI).")
