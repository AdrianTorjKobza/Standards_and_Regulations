# Automated Model Card Generator for EU AI Act & FDA

**PCCP-Gen** is a regulatory compliance tool designed to bridge the gap between Machine Learning engineering and regulatory documentation. It extracts metadata from **MLflow** runs and generates auditor-ready **Model Cards** (PDF) that align with **FDA PCCP (Predetermined Change Control Plan)** guidelines and **EU AI Act Article 13** transparency requirements.

## Key Features
* **MCML Alignment:** Structured documentation based on Model Card Markup Language concepts.
* **Slicing Analysis:** Automated bias and performance checks across demographic groups (Age, Gender, etc.) using **Fairlearn**.
* **Automated Visualization:** Generates and embeds Confusion Matrices and performance plots.
* **Auditor-Ready:** Professional PDF output using **FPDF2**.

## Tech Stack
* **Tracking:** [MLflow](https://mlflow.org/)
* **Analysis:** [Fairlearn](https://fairlearn.org/), [Scikit-learn](https://scikit-learn.org/)
* **PDF Generation:** [FPDF2](https://py-pdf.github.io/fpdf2/)
* **Data Handling:** Pandas, NumPy
* **Visuals:** Matplotlib, Seaborn

## Setup & Execution

1. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start MLflow UI**
```bash
mlflow ui  # This defaults to http://localhost:5000
```

4. **Create a Sample Run**
```bash
python examples/sample_run.py
```

5. **Generate the Model Card**
```bash
python -m pccp_gen.cli --run-id YOUR_RUN_ID --output Regulatory_Model_Card.pdf
```