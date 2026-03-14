# 🌌 Astraeus-Intelligence

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991.svg)](https://openai.com/)
[![Framework](https://img.shields.io/badge/Pattern-ReAct-green.svg)](https://arxiv.org/abs/2210.03629)

**Astraeus-Intelligence** is a high-performance framework for building autonomous AI agents capable of multi-step reasoning, planning, and precise tool execution. Designed for enterprise environments where tasks require more than just simple prompting—Astraeus agents utilize the **Reason + Act (ReAct)** paradigm to orchestrate complex workflows across heterogeneous APIs.

## 🚀 Vision
The goal of Astraeus is to move beyond static chat interfaces toward **goal-oriented autonomous systems**. By decoupling reasoning (the LLM) from execution (Modular Tools), Astraeus provides a scalable foundation for building agents that can:
- **Think:** Decompose complex user goals into actionable sub-tasks.
- **Act:** Interface with real-world APIs and internal systems.
- **Observe:** Incorporate feedback from tool outputs to refine future actions.

## 🏗 Architecture
- **Agent Core:** A modular reasoning engine with support for long-context LLMs.
- **Tool-Symphony:** A dynamic registry for injecting domain-specific capabilities (e.g., market data, search, risk engines).
- **Iteration Controller:** A safety-aware loop that prevents hallucination and infinite cycles.

## 🛠 Project Structure
`	ext
Astraeus-Intelligence/
├── src/
│   ├── agent.py         # Reasoning loop and LLM interface
│   └── tools.py         # Tool definitions and wrappers
├── examples/
│   └── task_execution.py # Real-world orchestration scenario
├── requirements.txt      # Dependencies
└── README.md             # Documentation
`

## 📖 Usage
1. **Setup Environment:**
   `ash
   pip install -r requirements.txt
   export OPENAI_API_KEY='your-key'
   `

2. **Run Example Orchestration:**
   `ash
   python examples/task_execution.py
   `

## 🔬 Enterprise AI Engineering
This repository serves as a demonstration of **Agentic AI Engineering**, focusing on prompt engineering, function calling, and structured output parsing.

---
*Developed by Cze Yee — Focused on Autonomous Systems & AI Orchestration.*