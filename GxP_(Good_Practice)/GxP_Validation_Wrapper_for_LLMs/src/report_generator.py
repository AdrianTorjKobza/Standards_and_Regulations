from fpdf import FPDF
import datetime
import platform

class ValidationReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "GxP Automated Validation Report - Lumina-Guard", ln=True, align="C")
        self.ln(5)

    def generate(self, results, config):
        self.add_page()
        self.set_font("Arial", size=10)
        
        # System Info (Installation Qualification)
        self.section_title("1. System Environment (IQ)")
        self.cell(0, 10, f"Date: {datetime.datetime.now()}", ln=True)
        self.cell(0, 10, f"OS: {platform.system()} {platform.release()}", ln=True)
        self.cell(0, 10, f"Python Version: {platform.python_version()}", ln=True)
        
        # Model Config
        self.section_title("2. Model Configuration Specification")
        for k, v in config['model_parameters'].items():
            self.cell(0, 10, f"{k}: {v}", ln=True)

        # Test Results
        self.section_title("3. Test Execution Results (OQ)")
        for test in results:
            status = "PASS" if test['success'] else "FAIL"
            self.cell(0, 10, f"Requirement: {test['name']} -> {status}", ln=True)
            if not test['success']:
                self.set_text_color(255, 0, 0)
                self.multi_cell(0, 10, f"Error: {test['message']}")
                self.set_text_color(0, 0, 0)

        self.output("Validation_Report.pdf")

    def section_title(self, label):
        self.set_font("Arial", "B", 11)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, label, ln=True, fill=True)
        self.set_font("Arial", size=10)