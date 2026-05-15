# Software Traceability Matrix (RTM)

The following table ensures that every regulatory requirement is verified by a specific test case within the `tests/` directory or the `run_validation.py` script.

| Req. ID | Category | Requirement Description | Implementation | Verification (Test ID) | Status |
|:---|:---|:---|:---|:---|:---|
| **REQ-01** | Safety | The system shall suppress diagnostic claims made by the LLM. | `src/summarizer.py` | `VAL-001` (Forbidden Terms) | **PASS** |
| **REQ-02** | Utility | Clinical summaries must be at least 20 words to ensure utility. | `src/summarizer.py` | `VAL-002` (Min Length) | **PASS** |
| **REQ-03** | GxP | System configuration (temp/seed) must be locked to ensure reproducibility. | `model_config.yaml` | `test_deterministic_temperature` | **PASS** |
| **REQ-04** | Audit | A non-editable PDF report must be generated for each validation run. | `src/report_generator.py`| `run_validation.py` | **PASS** |

**Legend:**
- **REQ**: Requirement
- **VAL**: Validation Test Case (Operational)
- **Status**: Updated as of last system run.