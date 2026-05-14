# Map the MCML concepts into a professional PDF layout

from fpdf import FPDF
import datetime

class PCCPRenderer(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.set_text_color(100)
        self.cell(0, 10, "FDA PCCP / EU AI Act - Automated Model Card", 0, 1, "C")
        self.ln(5)

    def add_section(self, title):
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, 0, 1, "L")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def generate_card(self, data, slicing_df, plot_buf, output_path):
        self.add_page()
        
        # Section 1: Model Metadata
        self.add_section("1. Model Overview")
        self.set_font("Arial", "", 10)
        self.set_text_color(0)
        metadata = [
            ["Run ID", data['run_id']],
            ["Timestamp", str(datetime.datetime.now())],
            ["Owner", data['tags'].get('developer', 'N/A')],
            ["Intended Use", data['tags'].get('intended_use', 'Clinical Decision Support')]
        ]
        
        for row in metadata:
            self.cell(50, 8, f"{row[0]}:", 1)
            self.cell(140, 8, f" {row[1]}", 1, 1)
        
        self.ln(10)
        
        # Section 2: Performance Metrics
        self.add_section("2. Quantitative Performance")
        self.image(plot_buf, x=10, w=100)
        self.ln(5)

        # Section 3: Slicing Analysis (MCML Style)
        self.add_page()
        self.add_section("3. Slicing Analysis (Bias Check)")
        self.set_font("Arial", "B", 10)
        
        # Table Header
        cols = ["Group", "Accuracy", "Recall", "Count"]
        for col in cols:
            self.cell(45, 10, col, 1, 0, "C")
        self.ln()
        
        self.set_font("Arial", "", 10)
        for index, row in slicing_df.iterrows():
            self.cell(45, 10, str(index), 1)
            self.cell(45, 10, f"{row['accuracy']:.4f}", 1)
            self.cell(45, 10, f"{row['recall']:.4f}", 1)
            self.cell(45, 10, str(int(row['count'])), 1, 1)

        self.output(output_path)