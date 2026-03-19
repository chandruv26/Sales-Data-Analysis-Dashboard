"""
run_pipeline.py
Master script to execute the entire Sales Data Analysis pipeline:
1. Generate Sample Data (sales_data.csv)
2. Clean Data (cleaned_sales_data.csv)
3. Perform Analysis & Generate charts (charts/ directory)
"""

import subprocess
import sys
import os

def run_script(script_name):
    print(f"\n>>> Running {script_name}...")
    try:
        # Capture as bytes and decode with errors='ignore' to prevent UnicodeEncodeError
        result = subprocess.run([sys.executable, script_name], 
                                capture_output=True, check=True)
        stdout_text = result.stdout.decode('utf-8', errors='ignore')
        print(stdout_text)
    except subprocess.CalledProcessError as e:
        print(f"ERROR running {script_name}:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    scripts = ["generate_dataset.py", "data_cleaning.py", "data_analysis.py"]
    
    print("=" * 60)
    print("  SALES DATA ANALYSIS — FULL PIPELINE")
    print("=" * 60)
    
    for script in scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"Skipping {script}: File not found.")
            
    print("\n" + "=" * 60)
    print("  PIPELINE COMPLETE!")
    print("  1. Dataset generated : sales_data.csv")
    print("  2. Data cleaned       : cleaned_sales_data.csv")
    print("  3. Analysis done      : insights_report.txt")
    print("  4. Visuals created   : charts/ folder")
    print("=" * 60)
    print("\nNext step: Follow PowerBI_Dashboard_Guide.md to build your dashboard.")
