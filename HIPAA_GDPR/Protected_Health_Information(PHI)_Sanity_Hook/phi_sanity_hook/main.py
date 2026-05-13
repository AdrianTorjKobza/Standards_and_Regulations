import sys
import argparse
from .detectors import PHIDetector

def main():
    parser = argparse.ArgumentParser(description="PHI Sanity Check Hook")
    parser.add_argument('filenames', nargs='*', help='Files to scan')
    args = parser.parse_args()

    TARGET_EXTENSIONS = ('.log', '.json', '.txt')
    files_to_check = [f for f in args.filenames if f.endswith(TARGET_EXTENSIONS)]

    if not files_to_check:
        sys.exit(0)

    detector = PHIDetector()
    violation_found = False

    for filename in files_to_check:
        with open(filename, 'r', encoding='utf-8') as f:
            results = detector.scan_text(f.read())
            
            if results:
                violation_found = True
                print(f"[!] PHI DETECTED in: {filename}")
                for label in set([r[0] for r in results]):
                    print(f"   [!] Found: {label}")

    if violation_found:
        print("\n[STRICT POLICY] Commit blocked. Remove PHI to proceed.")
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()