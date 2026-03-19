"""
data_cleaning.py
Step 1 — Clean the raw sales dataset and engineer new features.
Output: cleaned_sales_data.csv
"""

import pandas as pd
import numpy as np
import sys

# Force UTF-8 encoding for stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAW_FILE     = r"c:\Users\chand\Downloads\Sales Data Analysis Dashboard\sales_data.csv"
CLEANED_FILE = r"c:\Users\chand\Downloads\Sales Data Analysis Dashboard\cleaned_sales_data.csv"

# ──────────────────────────────────────────
# 1. Load Data
# ──────────────────────────────────────────
print("=" * 55)
print("  SALES DATA - CLEANING PIPELINE")
print("=" * 55)

df = pd.read_csv(RAW_FILE)
print(f"\n[LOAD]  Raw rows: {len(df)}  |  Columns: {list(df.columns)}")
print(f"        Missing values per column:\n{df.isnull().sum()}")

# ──────────────────────────────────────────
# 2. Remove Duplicates
# ──────────────────────────────────────────
before = len(df)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"\n[DEDUP] Removed {before - len(df)} duplicate rows. Remaining: {len(df)}")

# ──────────────────────────────────────────
# 3. Handle Missing Values
# ──────────────────────────────────────────
# Numeric columns — fill with median
for col in ["Sales Amount", "Profit"]:
    median_val = df[col].median()
    filled     = df[col].isnull().sum()
    df[col].fillna(median_val, inplace=True)
    print(f"[NULL]  '{col}': filled {filled} missing values with median ({median_val:.2f})")

# Categorical columns — fill with mode
for col in ["Region", "Customer Segment"]:
    mode_val = df[col].mode()[0]
    filled   = df[col].isnull().sum()
    df[col].fillna(mode_val, inplace=True)
    print(f"[NULL]  '{col}': filled {filled} missing values with mode ('{mode_val}')")

# Drop any remaining rows with nulls (e.g. Order Date or Product Name)
before = len(df)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"[NULL]  Dropped {before - len(df)} remaining rows with missing values.")

# ──────────────────────────────────────────
# 4. Format Date Column
# ──────────────────────────────────────────
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df.dropna(subset=["Order Date"], inplace=True)
df.reset_index(drop=True, inplace=True)
print(f"\n[DATE]  'Order Date' parsed as datetime. Sample: {df['Order Date'].iloc[0]}")

# ──────────────────────────────────────────
# 5. Create New Columns
# ──────────────────────────────────────────
df["Year"]          = df["Order Date"].dt.year
df["Month"]         = df["Order Date"].dt.month
df["Month Name"]    = df["Order Date"].dt.strftime("%b")  # Jan, Feb ...
df["Profit Margin"] = (df["Profit"] / df["Sales Amount"]).round(4)

print(f"\n[FEAT]  Created columns: Year, Month, Month Name, Profit Margin")

# ──────────────────────────────────────────
# 6. Data Type Cleanup
# ──────────────────────────────────────────
df["Sales Amount"]  = df["Sales Amount"].round(2)
df["Profit"]        = df["Profit"].round(2)
df["Region"]        = df["Region"].str.strip().str.title()
df["Customer Segment"] = df["Customer Segment"].str.strip().str.title()
df["Product Category"] = df["Product Category"].str.strip().str.title()
df["Product Name"]  = df["Product Name"].str.strip()

# ──────────────────────────────────────────
# 7. Summary
# ──────────────────────────────────────────
print("\n" + "=" * 55)
print("  CLEANED DATASET SUMMARY")
print("=" * 55)
print(f"  Final rows      : {len(df)}")
print(f"  Columns         : {list(df.columns)}")
print(f"  Date range      : {df['Order Date'].min().date()} → {df['Order Date'].max().date()}")
print(f"  Remaining nulls : {df.isnull().sum().sum()}")
print(f"\nHead (5 rows):\n{df.head().to_string()}")

# ──────────────────────────────────────────
# 8. Save
# ──────────────────────────────────────────
df.to_csv(CLEANED_FILE, index=False)
print(f"\n[SAVE]  Cleaned data saved → {CLEANED_FILE}")
print("=" * 55)
