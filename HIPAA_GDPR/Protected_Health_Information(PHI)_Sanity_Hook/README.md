# Automated PHI "Sanity Check" Hook

Security Git pre-commit hook, designed to prevent the accidental leakage of Protected Health Information (PHI) and clinical identifiers into version control or cloud buckets.

## Features
* **Transformer-based NER:** High-accuracy detection of Names, Facilities, and Locations.
* **Pattern Matching:** Detection of 10-digit NPIs and ICD-10 codes.
* **Strict Policy / Zero Trust:** No bypass allowed; files must be scrubbed to proceed.
* **Targeted Scanning:** Scans `.log`, `.json`, and `.txt` files.

## Tech Stack
* **NER Engine:** [spaCy](https://spacy.io/) with `en_core_web_trf` (RoBERTa-based transformer)

## Installation & Setup

### 1. Install Dependencies
```bash
# Create the environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# Install the package in editable mode with dev dependencies
pip install -r requirements.txt
pip install -e .

# Download the RoBERTa-based Transformer model
python -m spacy download en_core_web_trf

# Initialize Git
git init

# Run this command to register the hook with your local .git directory
pre-commit install
```

## Verification: The "Leak Test"
```bash
# Commit this file to your local repository:
git add leak_test.txt
git commit -m "Testing PHI security gate"

# The commit should fail with an output similar to this:
PHI Sanity Check.........................................................Failed
- hook id: phi-sanity-check
- exit code: 1

[!] PHI DETECTED in: leak_test.txt
   [!] Found: PERSON
   [!] Found: ICD10_CODE
   [!] Found: NPI_ID

[STRICT POLICY] Commit blocked. Please remove PHI from the files above.

## Running Tests
```bash
# To verify the NER engine is working correctly
python -m unittest discover tests