# Run this script first to create a local MLflow entry so the CLI has something to read.

import mlflow

def create_mock_run():
    mlflow.set_tracking_uri("http://localhost:5000") # Ensure mlflow server is running.

    with mlflow.start_run() as run:
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_metric("accuracy", 0.945)
        mlflow.set_tag("developer", "Applied AI Engineer")
        mlflow.set_tag("intended_use", "FDA Class II Medical Device Diagnostic")
        print(f"Mock Run Created! ID: {run.info.run_id}")

if __name__ == "__main__":
    create_mock_run()