# adk_example.py
"""
ADK / A2A conceptual example for InsightFlow.
This is NOT runnable as-is — it demonstrates how InsightFlow maps to ADK constructs:
- Agents, tools, loop agents, and A2A communication.
Include this file in the repo to show judges your ADK design/intent.
"""

ADK_EXAMPLE = """
# ADK Conceptual Mapping (Pseudo-code)

Orchestrator Agent:
- Name: Orchestrator
- Subagents: DataIntakeAgent, AnalyticsAgent, InsightWriterAgent
- Tools: load_and_profile_csv (python tool), compute_kpi (python tool), generate_plot (python tool)
- Memory: InMemorySessionService (short-term), MemoryBank (long-term)

DataIntakeAgent:
- LoopAgent pattern with OutlineValidationChecker-like validator
- Tool: load_and_profile_csv (returns profile + cleaned schema)
- On success: escalate to AnalyticsAgent

AnalyticsAgent:
- Runs compute_kpi with provided tools
- May spawn parallel tasks: KPI computation, anomaly detection, segmentation
- Writes charts via generate_plot tool

InsightWriterAgent:
- Uses Gemini (LLM) via ADK tool adapter
- Performs context compaction before calling LLM
- Produces executive summary + suggested actions

A2A Flow (simplified):
User -> Orchestrator -> (DataIntakeAgent -> AnalyticsAgent -> InsightWriterAgent) -> Orchestrator -> User

Observability:
- Each agent logs events to central tracing/logging
- Validation checkers raise event actions on failure -> loop retry
"""

if __name__ == "__main__":
    print(ADK_EXAMPLE)
