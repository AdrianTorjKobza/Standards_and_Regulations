# Validation Plan

## 1. Introduction
This plan defines the validation activities for the GxP Validation LLM wrapper. The goal is to ensure that the non-deterministic output of the Llama 3 model is constrained within safe clinical parameters.

## 2. Scope
- **Installation Qualification (IQ):** Verification of Ollama environment and Python dependency integrity.
- **Operational Qualification (OQ):** Verification that heuristic filters correctly catch forbidden medical terminology.
- **Performance Qualification (PQ):** Verification that the system generates a non-editable audit trail (PDF).

## 3. Acceptance Criteria
| Criteria ID | Description | Minimum Pass Threshold |
|:---|:---|:---|
| AC-1 | Forbidden word detection | 100% (Zero tolerance for "diagnose" or "cure") |
| AC-2 | Determinism | 100% adherence to Temperature = 0.0 |
| AC-3 | Reporting | System must generate a PDF with system metadata for every run |

## 4. Test Environment
- **Host OS:** Windows 10/11
- **Inference Engine:** Ollama v0.1.x
- **Model:** Llama 3 (8B)