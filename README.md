# Sales Data Analysis Dashboard 📊

An end-to-end Data Analysis project featuring a Python data pipeline (Generation, Cleaning, Analysis) and a comprehensive Power BI Dashboard design guide.

## 🚀 Project Overview

This project demonstrates a standard data analyst workflow:
1.  **Data Generation**: Creating a realistic raw sales dataset with intentional noise (duplicates, missing values).
2.  **Data Cleaning**: Using Python (Pandas) to handle missing values, remove duplicates, and engineer features like Profit Margin and Order Date hierarchies.
3.  **Exploratory Data Analysis (EDA)**: Generating key metrics and visual charts to identify sales trends and top-performing categories.
4.  **Power BI Dashboard**: A step-by-step guide to building an interactive, professional dashboard using the cleaned data.

---

## 📁 Repository Structure

*   `generate_dataset.py`: Creates the raw `sales_data.csv`.
*   `data_cleaning.py`: Cleans raw data and saves it as `cleaned_sales_data.csv`.
*   `data_analysis.py`: Performs EDA and generates PNG charts in the `charts/` folder.
*   `run_pipeline.py`: Master script to execute the entire Python workflow in one command.
*   `PowerBI_Dashboard_Guide.md`: Detailed instructions for building the Power BI visuals.
*   `insights_report.txt`: Automated summary of key business insights.
*   `charts/`: Directory containing generated visualizations.

---

## 🛠️ Getting Started

### Prerequisites
*   Python 3.7+
*   Pandas, Matplotlib, Seaborn
*   Power BI Desktop (for the dashboard part)

### Installation
1. Clone this repository or download the files.
2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```

### Execution
Run the full data pipeline with:
```bash
python run_pipeline.py
```
This will generate the datasets, clean them, and produce the analysis/charts.

---

## 📊 Key Insights from Analysis

*   **Top Region**: The **East** region leads in total sales volume.
*   **Most Profitable Category**: **Technology** provides the highest absolute profit.
*   **Seasonal Trends**: A significant spike in **Q4 (Oct-Dec)** suggests strong holiday demand.
*   **Top Product**: **Laptop Pro 15** is the highest-selling individual product.

---

## 🎨 Dashboard Design

The suggested Power BI layout includes:
*   **KPI Cards**: Total Sales, Total Profit, Profit Margin.
*   **Trend Analysis**: Monthly Sales (Line Chart).
*   **Market Share**: Sales by Category (Bar Chart).
*   **Geospatial**: Sales by Region (Map).

Refer to [PowerBI_Dashboard_Guide.md](PowerBI_Dashboard_Guide.md) for full setup instructions.

---

## 📝 License
This project is open-source and free to use for educational purposes.
