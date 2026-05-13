import re
import spacy
from typing import List, Tuple

class PHIDetector:
    def __init__(self):
        """
        Initializes the PHI Detector with a Transformer-based NER model
        and standard clinical regex patterns.
        """
        try:
            # en_core_web_trf is a RoBERTa-based transformer model
            self.nlp = spacy.load("en_core_web_trf")
        except OSError:
            raise ImportError("Missing required SpaCy model. Run: python -m spacy download en_core_web_trf")

        # Regex for NPI (National Provider Identifier) - 10 digits
        self.npi_pattern = re.compile(r'\b\d{10}\b')
        
        # ICD-10 Pattern (General clinical code format)
        self.icd10_pattern = re.compile(r'\b[A-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}\b')

    def scan_text(self, text: str) -> List[Tuple[str, str]]:
        findings = []

        # Layer 1: Regex (Fast)
        if self.npi_pattern.search(text):
            findings.append(("NPI_ID", "Potential 10-digit NPI detected."))

        if self.icd10_pattern.search(text):
            findings.append(("ICD10_CODE", "Potential ICD-10 code detected."))

        # Layer 2: Transformer NER (Context Aware)
        doc = self.nlp(text)
        target_labels = {"PERSON", "GPE", "FACILITY", "DATE"}
        
        for ent in doc.ents:
            if ent.label_ in target_labels:
                findings.append((ent.label_, "Sensitive entity detected by NER."))

        return findings