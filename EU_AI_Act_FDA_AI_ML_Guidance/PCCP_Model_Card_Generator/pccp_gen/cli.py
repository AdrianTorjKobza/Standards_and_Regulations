import argparse
from pccp_gen.extractor import MLflowExtractor
from pccp_gen.analyzer import ModelAnalyzer
from pccp_gen.renderer import PCCPRenderer
import pandas as pd
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="PCCP Model Card Generator")
    parser.add_argument("--run-id", required=True, help="MLflow Run ID")
    parser.add_argument("--output", default="ModelCard.pdf", help="Output PDF filename")
    args = parser.parse_args()

    print(f"[*] Extracting data for Run: {args.run_id}...")
    extractor = MLflowExtractor()
    data = extractor.fetch_run_data(args.run_id)

    # For local demo: Generate synthetic evaluation data
    # In production, you'd pull the actual validation set from MLflow
    y_true = np.random.randint(0, 2, 100)
    y_pred = np.random.randint(0, 2, 100)
    sensitive_features = np.random.choice(['Age: 18-35', 'Age: 36-60', 'Age: 60+'], 100)

    print("[*] Performing Slicing Analysis...")
    analyzer = ModelAnalyzer()
    slicing_results = analyzer.perform_slicing(y_true, y_pred, sensitive_features)
    plot_buf = analyzer.generate_plots(y_true, y_pred)

    print(f"[*] Rendering PDF: {args.output}...")
    pdf = PCCPRenderer()
    pdf.generate_card(data, slicing_results, plot_buf, args.output)
    print("[+] Model Card generated successfully.")

if __name__ == "__main__":
    main()