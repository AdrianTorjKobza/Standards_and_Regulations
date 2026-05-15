import yaml
from langchain_community.llms import Ollama
from pydantic import BaseModel, Field

class ClinicalSummary(BaseModel):
    summary_text: str = Field(description="The abstracted summary of the clinical note.")
    contains_phi: bool = Field(description="Flag if Protected Health Information was detected.")

class MedicalSummarizer:
    def __init__(self, config_path="model_config.yaml"):
        # This now uses the path passed from the test suite
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        params = self.config['model_parameters']
        
        self.llm = Ollama(
            model=params['model_name'],
            temperature=params['temperature'],
            top_p=params['top_p'],
            stop=["\n"]
        )

    def summarize(self, note: str) -> str:
        # Simple prompt engineered for abstractive summarization
        prompt = f"Summarize the following clinical note concisely. Do not diagnose. Note: {note}"
        return self.llm.invoke(prompt)