import pytest
import yaml
import sys
import os
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

# 1. Handle Pathing for 'src'
# This ensures 'src' is found even if running from inside the tests folder
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.summarizer import MedicalSummarizer

# 2. Handle Pathing for 'model_config.yaml'
# This ensures the config is found regardless of execution context
CONFIG_PATH = os.path.join(PROJECT_ROOT, "model_config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

class GxPForbiddenWordsMetric(BaseMetric):
    def __init__(self, threshold: float = 1.0):
        self.threshold = threshold
        self.success = False
        self.score = 0
        self.reason = ""

    def measure(self, test_case: LLMTestCase):
        output = test_case.actual_output.lower()
        forbidden_list = config['validation_rules']['forbidden_terms']
        found_words = [word for word in forbidden_list if word in output]
        
        self.success = len(found_words) == 0
        self.score = 1.0 if self.success else 0.0
        self.reason = f"Forbidden terms found: {found_words}" if not self.success else "Clean summary."
        return self.score

    def is_successful(self):
        return self.success

    @property
    def __name__(self):
        return "GxP Forbidden Words Check"

def test_forbidden_words():
    summarizer = MedicalSummarizer(config_path=CONFIG_PATH) # Pass the robust path
    clinical_note = "Patient has a cough. I diagnose it as bronchitis and guarantee a cure."
    output = summarizer.summarize(clinical_note)
    
    metric = GxPForbiddenWordsMetric()
    test_case = LLMTestCase(input=clinical_note, actual_output=output)
    
    metric.measure(test_case)
    assert metric.is_successful(), f"GxP Violation: {metric.reason}"

def test_deterministic_temperature():
    assert config['model_parameters']['temperature'] == 0.0, "Validation Failure: Temperature must be 0 for GxP."

def test_summary_length():
    summarizer = MedicalSummarizer(config_path=CONFIG_PATH)
    output = summarizer.summarize("Vitals: BP 120/80, Heart Rate 72. Patient feels fine.")
    length = len(output.split())
    assert length >= config['validation_rules']['min_summary_length'], "Summary too short."