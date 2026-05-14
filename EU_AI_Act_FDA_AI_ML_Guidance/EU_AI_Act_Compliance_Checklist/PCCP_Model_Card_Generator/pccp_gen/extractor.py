# Handles the retrieval of metadata and artifacts.

import mlflow
import pandas as pd
from mlflow.tracking import MlflowClient

class MLflowExtractor:
    def __init__(self, tracking_uri="http://localhost:5000"):
        mlflow.set_tracking_uri(tracking_uri)
        self.client = MlflowClient()

    def fetch_run_data(self, run_id):
        run = self.client.get_run(run_id)
        metrics = run.data.metrics
        params = run.data.params
        tags = run.data.tags
        
        # In a real scenario, we'd download the model or validation dataset artifact here.
        return {
            "run_id": run_id,
            "metrics": metrics,
            "params": params,
            "tags": tags,
            "start_time": run.info.start_time
        }