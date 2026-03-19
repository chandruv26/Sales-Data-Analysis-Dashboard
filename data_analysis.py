"""
data_analysis.py
Step 2 — Analyse the cleaned dataset and generate charts + insights.
Outputs:
  charts/  monthly_sales_trend.png
           sales_by_region.png
           sales_by_category.png
           top10_products.png
           profit_margin_by_category.png
  insights_report.txt
"""

import os
import textwrap
import sys
import pandas as pd
import matplotlib

# Force UTF-8 encoding for stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
matplotlib.use("Agg")           # headless rendering — no display required
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# -- paths ------------------------------------------------------------------
BASE_DIR     = r"c:\Users\chand\Downloads\Sales Data Analysis Dashboard"
CLEANED_FILE = os.path.join(BASE_DIR, "cleaned_sales_data.csv")
CHART_DIR    = os.path.join(BASE_DIR, "charts")
REPORT_FILE  = os.path.join(BASE_DIR, "insights_report.txt")
os.makedirs(CHART_DIR, exist_ok=True)

# -- style ------------------------------------------------------------------
PALETTE  = ["#2E86AB", "#A23B72", "#F18F01", "#C73E1D", "#3B1F2B"]
sns.set_theme(style="whitegrid", palette=PALETTE, font_scale=1.1)
TITLE_KW = dict(fontsize=14, fontweight="bold", pad=14)

df = pd.read_csv(CLEANED_FILE, parse_dates=["Order Date"])

print("=" * 60)
print("  SALES DATA ANALYSIS")
print("=" * 60)

# ══════════════════════════════════════════════════════════════
# A. HIGH-LEVEL METRICS
# ══════════════════════════════════════════════════════════════
total_sales        = df["Sales Amount"].sum()
total_profit       = df["Profit"].sum()
overall_margin     = (total_profit / total_sales) * 100
avg_order_value    = df["Sales Amount"].mean()
num_orders         = df["Order ID"].nunique()

print(f"\n{'─'*30} KPIs {'─'*25}")
print(f"  Total Sales        : ${total_sales:>12,.2f}")
print(f"  Total Profit       : ${total_profit:>12,.2f}")
print(f"  Overall Margin     : {overall_margin:>11.2f}%")
print(f"  Avg Order Value    : ${avg_order_value:>12,.2f}")
print(f"  Unique Orders      : {num_orders:>12,}")

# ══════════════════════════════════════════════════════════════
# B. SALES BY REGION
# ══════════════════════════════════════════════════════════════
region_sales = (
    df.groupby("Region")["Sales Amount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
best_region = region_sales.iloc[0]["Region"]
print(f"\n{'─'*30} Sales by Region {'─'*13}")
print(region_sales.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(region_sales["Region"], region_sales["Sales Amount"],
              color=PALETTE, edgecolor="white", linewidth=0.6)
ax.bar_label(bars, fmt="${:,.0f}", padding=4, fontsize=9)
ax.set_title("Sales by Region", **TITLE_KW)
ax.set_xlabel("Region", labelpad=8)
ax.set_ylabel("Total Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "sales_by_region.png"), dpi=150)
plt.close()
print("[CHART] sales_by_region.png saved")

# ══════════════════════════════════════════════════════════════
# C. SALES BY CATEGORY
# ══════════════════════════════════════════════════════════════
cat_sales = (
    df.groupby("Product Category")[["Sales Amount", "Profit"]]
    .sum()
    .sort_values("Sales Amount", ascending=False)
    .reset_index()
)
best_category        = cat_sales.iloc[0]["Product Category"]
most_profitable_cat  = cat_sales.sort_values("Profit", ascending=False).iloc[0]["Product Category"]
print(f"\n{'─'*30} Sales by Category {'─'*10}")
print(cat_sales.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 5))
x = range(len(cat_sales))
bars = ax.bar(x, cat_sales["Sales Amount"], color=PALETTE[:len(cat_sales)],
              edgecolor="white", linewidth=0.6)
ax.bar_label(bars, fmt="${:,.0f}", padding=4, fontsize=9)
ax.set_xticks(list(x))
ax.set_xticklabels(cat_sales["Product Category"], rotation=20, ha="right")
ax.set_title("Sales by Product Category", **TITLE_KW)
ax.set_xlabel("Category", labelpad=8)
ax.set_ylabel("Total Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "sales_by_category.png"), dpi=150)
plt.close()
print("[CHART] sales_by_category.png saved")

# ══════════════════════════════════════════════════════════════
# D. MONTHLY SALES TREND
# ══════════════════════════════════════════════════════════════
monthly = (
    df.groupby(["Year", "Month"])["Sales Amount"]
    .sum()
    .reset_index()
)
monthly["Period"] = pd.to_datetime(
    monthly["Year"].astype(str) + "-" + monthly["Month"].astype(str).str.zfill(2)
)
monthly.sort_values("Period", inplace=True)

peak_period = monthly.loc[monthly["Sales Amount"].idxmax(), "Period"]
peak_month_label = peak_period.strftime("%B %Y")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly["Period"], monthly["Sales Amount"],
        color=PALETTE[0], linewidth=2.2, marker="o", markersize=4)
ax.fill_between(monthly["Period"], monthly["Sales Amount"],
                alpha=0.15, color=PALETTE[0])
ax.set_title("Monthly Sales Trend", **TITLE_KW)
ax.set_xlabel("Month", labelpad=8)
ax.set_ylabel("Total Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "monthly_sales_trend.png"), dpi=150)
plt.close()
print("[CHART] monthly_sales_trend.png saved")

# Seasonal insight
q4_sales = df[df["Month"].isin([10, 11, 12])]["Sales Amount"].sum()
q1_sales = df[df["Month"].isin([1, 2, 3])]["Sales Amount"].sum()
q4_q1_pct = ((q4_sales - q1_sales) / q1_sales) * 100

# ══════════════════════════════════════════════════════════════
# E. TOP 10 PRODUCTS BY SALES
# ══════════════════════════════════════════════════════════════
top10 = (
    df.groupby("Product Name")["Sales Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
print(f"\n{'─'*30} Top 10 Products {'─'*12}")
print(top10.to_string(index=False))

fig, ax = plt.subplots(figsize=(9, 6))
colors_top = sns.color_palette(PALETTE * 2, n_colors=10)
bars = ax.barh(top10["Product Name"][::-1], top10["Sales Amount"][::-1],
               color=colors_top[::-1], edgecolor="white", linewidth=0.5)
ax.bar_label(bars, fmt="${:,.0f}", padding=4, fontsize=8)
ax.set_title("Top 10 Products by Sales", **TITLE_KW)
ax.set_xlabel("Total Sales ($)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1e3:.0f}K"))
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "top10_products.png"), dpi=150)
plt.close()
print("[CHART] top10_products.png saved")

# ══════════════════════════════════════════════════════════════
# F. PROFIT MARGIN BY CATEGORY
# ══════════════════════════════════════════════════════════════
cat_margin = (
    df.groupby("Product Category")
    .apply(lambda g: (g["Profit"].sum() / g["Sales Amount"].sum()) * 100)
    .reset_index(name="Profit Margin %")
    .sort_values("Profit Margin %", ascending=False)
)
highest_margin_cat = cat_margin.iloc[0]["Product Category"]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(cat_margin["Product Category"], cat_margin["Profit Margin %"],
              color=PALETTE[:len(cat_margin)], edgecolor="white", linewidth=0.6)
ax.bar_label(bars, fmt="%.1f%%", padding=4, fontsize=9)
ax.set_title("Profit Margin by Category", **TITLE_KW)
ax.set_xlabel("Category", labelpad=8)
ax.set_ylabel("Profit Margin (%)")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "profit_margin_by_category.png"), dpi=150)
plt.close()
print("[CHART] profit_margin_by_category.png saved")

# ══════════════════════════════════════════════════════════════
# G. INSIGHTS REPORT
# ══════════════════════════════════════════════════════════════
insights = f"""
################################################################
#           SALES DATA ANALYSIS - INSIGHTS REPORT            #
################################################################
Generated: {pd.Timestamp.now().strftime("%Y-%m-%d %H:%M")}

---------------------------------
 KEY PERFORMANCE INDICATORS (KPIs)
---------------------------------
  * Total Sales          : ${total_sales:,.2f}
  * Total Profit         : ${total_profit:,.2f}
  * Overall Profit Margin: {overall_margin:.2f}%
  * Average Order Value  : ${avg_order_value:,.2f}
  * Total Unique Orders  : {num_orders:,}

---------------------------------
 REGIONAL PERFORMANCE
---------------------------------
  * Highest-performing region: {best_region}
{region_sales.to_string(index=False)}

  -> Insight: The {best_region} region leads in total sales. Consider
     allocating more marketing budget and inventory there to sustain growth.

---------------------------------
 CATEGORY PERFORMANCE
---------------------------------
  * Top sales category       : {best_category}
  * Most profitable category : {most_profitable_cat}
  * Highest margin category  : {highest_margin_cat}
{cat_sales.to_string(index=False)}

  -> Insight: {most_profitable_cat} delivers the highest absolute profit.
     Focus on upselling premium items within this category.

---------------------------------
 SEASONAL / MONTHLY TRENDS
---------------------------------
  * Peak sales month  : {peak_month_label}
  * Q4 vs Q1 uplift   : {q4_q1_pct:+.1f}%

  -> Insight: Sales spike significantly in Q4 (Oct-Dec), suggesting
     strong holiday/end-of-year demand. Plan promotions and stock levels
     accordingly. Q1 is the slowest period - consider targeted discounts.

---------------------------------
 TOP 10 PRODUCTS
---------------------------------
{top10.to_string(index=False)}

---------------------------------
 RECOMMENDATIONS
---------------------------------
  1. Double down on {best_region} - it's your highest-revenue region.
  2. Promote {most_profitable_cat} products more aggressively; the margins justify it.
  3. Run Q4 campaigns early (September) to capture peak demand.
  4. Investigate underperforming regions and categories for root causes.
  5. Bundle low-margin Office Supplies with high-margin Technology items.

---------------------------------
 CHART FILES (saved in charts/ folder)
---------------------------------
  * monthly_sales_trend.png
  * sales_by_region.png
  * sales_by_category.png
  * top10_products.png
  * profit_margin_by_category.png
"""

with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write(insights)

print("\n" + insights)
print(f"[SAVE] Insights saved → {REPORT_FILE}")
print("=" * 60)
