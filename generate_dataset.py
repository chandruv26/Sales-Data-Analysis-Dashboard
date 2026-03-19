"""
generate_dataset.py
Generates a realistic sample sales dataset (sales_data.csv) for the
Sales Data Analysis Dashboard project.
Run this ONCE to create the raw data file.
"""

import pandas as pd
import numpy as np
import random
import sys
from datetime import datetime, timedelta

# Force UTF-8 encoding for stdout to handle piped output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

random.seed(42)
np.random.seed(42)

NUM_ROWS = 520   # slightly more than 500 so we can drop duplicates later

categories = {
    "Technology": ["Laptop Pro 15", "Wireless Mouse", "USB-C Hub", "Monitor 27\"",
                   "Mechanical Keyboard", "Webcam HD", "External SSD 1TB"],
    "Furniture":  ["Executive Chair", "Standing Desk", "Bookshelf 5-Tier",
                   "Filing Cabinet", "Conference Table", "Ergonomic Footrest"],
    "Office Supplies": ["Sticky Notes Pack", "Ball Pens Box", "Printer Paper A4",
                        "Stapler Set", "Whiteboard Markers", "Binder Clips Pack",
                        "File Folders"],
    "Clothing":   ["Business Suit", "Formal Shirt", "Casual Jacket",
                   "Polo T-Shirt", "Office Trousers"],
}

regions   = ["East", "West", "North", "South", "Central"]
segments  = ["Consumer", "Corporate", "Home Office", "Small Business"]

start_date = datetime(2022, 1, 1)
end_date   = datetime(2024, 12, 31)
date_range = (end_date - start_date).days

rows = []
for i in range(1, NUM_ROWS + 1):
    category = random.choice(list(categories.keys()))
    product  = random.choice(categories[category])
    region   = random.choice(regions)
    segment  = random.choice(segments)

    # seasonal uplift: Q4 sales are higher
    order_date = start_date + timedelta(days=random.randint(0, date_range))
    q4_boost   = 1.3 if order_date.month in [10, 11, 12] else 1.0

    base_sales = {
        "Technology": random.uniform(200, 2000),
        "Furniture":  random.uniform(100, 1500),
        "Office Supplies": random.uniform(10, 200),
        "Clothing":   random.uniform(50, 500),
    }[category] * q4_boost

    sales  = round(base_sales, 2)
    margin = random.uniform(0.05, 0.40)
    profit = round(sales * margin, 2)

    rows.append({
        "Order ID":         f"ORD-{i:05d}",
        "Order Date":       order_date.strftime("%Y-%m-%d"),
        "Product Category": category,
        "Product Name":     product,
        "Sales Amount":     sales,
        "Profit":           profit,
        "Region":           region,
        "Customer Segment": segment,
    })

df = pd.DataFrame(rows)

# Inject 15 duplicate rows
duplicates = df.sample(15, random_state=7)
df = pd.concat([df, duplicates], ignore_index=True)

# Inject ~3 % missing values
for col in ["Sales Amount", "Profit", "Region", "Customer Segment"]:
    mask = np.random.rand(len(df)) < 0.03
    df.loc[mask, col] = np.nan

df.to_csv(
    r"c:\Users\chand\Downloads\Sales Data Analysis Dashboard\sales_data.csv",
    index=False
)
print(f"Dataset created: {len(df)} rows x {len(df.columns)} columns")
# head() can occasionally cause console errors on Windows if columns have special formatting
# Printing a simplified version
print(df[["Order ID", "Order Date", "Product Category", "Sales Amount"]].head().to_string())
