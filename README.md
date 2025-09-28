# CrewAI Project Suite

## Overview
This repository bundles five independent multi-agent automations built with [CrewAI](https://crewai.com). Each "crew" orchestrates specialised large-language-model agents to tackle a different workflow—from structured debates and code generation to financial research, software delivery, and live stock screening. The projects share a common toolchain and environment so you can explore contrasting collaboration patterns side by side.

## Core Stack & Tooling
- **Python 3.12+** with [uv](https://docs.astral.sh/uv/) or `crewai` CLI for dependency and run-command management.
- **CrewAI 0.193+ & crewai-tools** for agent process orchestration, task routing, memory, and tool ingestion.
- **LLM providers** wired through API keys in `.env`: OPENAI, Anthropic, Gemini, XAI (Grok), Groq, DeepSeek, Meta (Llama), and Google Vertex.
- **External services & utilities:** Serper.dev search (`SerperDevTool`), a custom Pushover push notification tool, Gradio for lightweight UIs, and optional structured outputs through Pydantic models.
- **Memory & persistence** (Stock Picker crew): CrewAI short-term/entity RAG storage and SQLite-backed long-term memory for cross-run recall.

## Getting Started
1. Install dependencies at the repo root (recommended):
   ```bash
   uv sync
   ```
   or
   ```bash
   crewai install
   ```
2. Duplicate `.env.example` (or update `.env`) with your own API credentials. Required keys vary by crew but include `OPENAI_API_KEY`, `GEMINI_API_KEY`, `XAI_API_KEY`, `SERPER_API_KEY`, and (for notifications) `PUSHOVER_USER`/`PUSHOVER_TOKEN`.
3. Run an individual crew from its folder, e.g.:
   ```bash
   cd clash_of_the_llms
   crewai run
   ```
   or invoke the module entry point with `uv run python -m <package>.main`.

_All output artifacts land in each project’s `output/` directory so you can inspect generated content without digging into logs._

## Project Catalog

### Clash of the LLMs (`clash_of_the_llms/`)
- **What it does:** stages a formal debate on a supplied motion, then issues a verdict.
- **Agents & flow:** sequential Pro Debater (OpenAI), Con Debater (Gemini), and a neutral Judge (xAI) execute tasks `propose`, `oppose`, and `decide` respectively.
- **Concepts & tools:** showcases cross-provider ensembles, configurable debate prompts, and optional custom CrewAI tools (`tools/custom_tool.py`) you can extend.
- **Outputs:** argument markdown files (`output/propose.md`, `output/oppose.md`) plus a judgment in `output/decide.md`.

### Code Master (`code_master/`)
- **What it does:** turns a natural-language assignment into production-ready Python, executes it in CrewAI’s safe sandbox, and packages code plus runtime output.
- **Agent:** a single expert "Coder" (OpenAI) that plans, writes, and verifies solutions with `allow_code_execution=True`.
- **Concepts & tools:** demonstrates CrewAI code execution, retry controls, and sequential task orchestration for one-agent crews.
- **Outputs:** consolidated script and stdout captured in `output/code_and_output.txt` for reproducible grading or review.

### Engineering Team (`engineering_team/`)
- **What it does:** simulates a four-person software squad to deliver a full feature slice (design → backend module → Gradio demo → unit tests) for an account management system.
- **Agents & flow:** Engineering Lead (OpenAI) drafts the design; Backend Engineer, Frontend Engineer, and Test Engineer (xAI) implement, build a UI, and author tests, sharing context across sequential tasks.
- **Concepts & tools:** collaborative engineering lifecycle, CrewAI code execution, Gradio UI scaffolding, cross-agent hand-offs via task context.
- **Outputs:** design spec (`output/accounts.py_design.md`), backend module (`output/accounts.py`), prototype UI (`output/app.py`), and tests (`output/test_accounts.py`).

### Financial Researcher (`financial_researcher/`)
- **What it does:** compiles a fully sourced company research dossier and turns it into an investor-ready market analysis report.
- **Agents & flow:** Researcher (OpenAI) uses Serper-powered search to complete a templated dossier; Analyst (Gemini) consumes that dossier to synthesize executive insights.
- **Concepts & tools:** external search integration via `SerperDevTool`, strict markdown templates, citation handling, and multi-stage editorial refinement.
- **Outputs:** structured research in `output/research.md` plus a polished narrative report in `output/report.md`.

### Stock Picker (`stock_picker/`)
- **What it does:** monitors a sector for trending companies, researches each candidate, selects the single best opportunity, and emits a notification-ready decision.
- **Agents & flow:** Hierarchical process led by a Manager. Specialists include a Serper-backed Trending Company Finder and Financial Researcher (OpenAI) plus a Stock Picker agent (OpenAI) that finalizes decisions.
- **Concepts & tools:** CrewAI hierarchical crews, Pydantic-enforced task outputs, multi-level memory (short-term/entity RAG + SQLite long-term), and a custom `PushNotificationTool` that integrates with Pushover.
- **Outputs:** structured JSON artifacts (`output/trending_companies.json`, `output/research_report.json`) and a final Markdown recommendation (`output/decision.md`) alongside live push notifications when credentials are configured.

## Additional Notes
- Every subproject ships with a `knowledge/` seed folder and `tests/` scaffolding so you can extend domain knowledge or add unit tests as workflows evolve.
- You can add or swap agents by editing each crew’s `config/agents.yaml` and `config/tasks.yaml`. Crew definitions in `crew.py` expose where to plug in extra tools or adjust processes (sequential vs. hierarchical).
- The root `pyproject.toml` aggregates optional extras (LangChain, LangGraph, Semantic Kernel, SendGrid, etc.) should you expand these crews into larger automations.

Happy experimenting with multi-agent patterns!
