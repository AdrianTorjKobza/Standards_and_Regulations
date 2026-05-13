import unittest
from phi_sanity_hook.detectors import PHIDetector

class TestPHIDetection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.detector = PHIDetector()

    def test_npi_detection(self):
        findings = self.detector.scan_text("NPI: 1234567890")
        self.assertIn("NPI_ID", [f[0] for f in findings])

    def test_name_detection(self):
        findings = self.detector.scan_text("The patient is John Doe.")
        self.assertIn("PERSON", [f[0] for f in findings])

if __name__ == '__main__':
    unittest.main()