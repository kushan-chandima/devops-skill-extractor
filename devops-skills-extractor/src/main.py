import sys
from pathlib import Path

# Add scripts directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from generate_report import generate_reports
from generate_sri_lanka_report import generate_sri_lanka_report


def main():
    print("=" * 70)
    print("DEVOPS SKILLS EXTRACTOR - RUNNING ALL REPORTS")
    print("=" * 70)
    
    # Generate global DevOps skills report
    print("\n[1/2] Generating Global DevOps Skills Report...")
    global_reports = generate_reports()
    
    # Generate Sri Lanka specific report
    print("\n[2/2] Generating Sri Lanka DevOps Skills Report...")
    sri_lanka_reports = generate_sri_lanka_report()
    
    print("\n" + "=" * 70)
    print("ALL REPORTS GENERATED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()