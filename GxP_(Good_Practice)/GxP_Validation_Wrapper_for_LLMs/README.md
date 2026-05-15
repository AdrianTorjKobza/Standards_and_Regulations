# GxP Validation Wrapper for LLMs POC

**GxP Validation** for Large Language Models (LLMs) used in regulated medical environments (MedTech/Life Sciences). It addresses the non-deterministic nature of AI by applying heuristic guardrails and automated audit trails.

## Features
- **Deterministic Locking:** Configuration-as-code ensures temperature and seed stability.
- **Heuristic Assertions:** Uses `DeepEval` and `Pytest` to enforce "Forbidden Word" lists.
- **Automated Evidence:** Generates a PDF Validation Report for Quality Management System (QMS) records.
- **Privacy First:** Built for **Ollama**, ensuring no patient data leaves the local machine.

## Tech Stack
*   **Inference Engine:** [Ollama](https://ollama.com/) (Local LLM hosting to ensure data residency/HIPAA alignment).
*   **Orchestration:** [LangChain](https://python.langchain.com/) (For structured prompt management and model interaction).
*   **Validation & Metrics:** [DeepEval](https://github.com/confident-ai/deepeval) & [Pytest](https://pytest.org/) (For heuristic assertions and unit-testing AI outputs).
*   **Schema Enforcement:** [Pydantic](https://docs.pydantic.dev/) (Ensures internal data structures remain valid).
*   **Reporting:** [FPDF2](https://github.com/fpdf2/fpdf2) (Automated generation of non-editable PDF validation reports).

## Installation (Windows)
1. Install [Ollama](https://ollama.com/).
2. Pull the model: `ollama pull llama3`.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run Unit Tests
    ```bash
    pytest tests/test_validation_suite.py
    ```
6. Generate Validation Report
    ```bash
    python run_validation.py
    ```