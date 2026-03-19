# 📊 Power BI Dashboard — Sales Data Analysis
### Step-by-Step Beginner-Friendly Guide

---

## 1. What You'll Build

A 1-page interactive Power BI report with:

| Visual | Purpose |
|---|---|
| 3 KPI Cards | Total Sales · Total Profit · Profit Margin |
| Line Chart | Monthly Sales Trend over time |
| Bar Chart | Sales by Product Category |
| Clustered Bar | Sales by Region |
| Horizontal Bar | Top 10 Products by Sales |
| Map | Sales concentration by Region |
| Slicers | Year · Region · Product Category |

---

## 2. Prerequisites

- **Power BI Desktop** (free) — [Download here](https://powerbi.microsoft.com/desktop)
- The file `cleaned_sales_data.csv` from this project

---

## 3. Load Data into Power BI

1. Open **Power BI Desktop** → click **Home → Get Data → Text/CSV**
2. Browse to `cleaned_sales_data.csv` → click **Open**
3. In the preview window click **Load**
4. In the **Fields** pane on the right you'll see all columns

---

## 4. Verify Data Types

Go to **Home → Transform Data** (opens Power Query Editor):

| Column | Expected Type |
|---|---|
| Order Date | Date |
| Sales Amount | Decimal Number |
| Profit | Decimal Number |
| Profit Margin | Decimal Number |
| Year | Whole Number |
| Month | Whole Number |

Click **Close & Apply** when done.

---

## 5. Create Measures (DAX)

In the **Fields** pane, right-click the table name → **New Measure**:

```dax
-- Total Sales
Total Sales = SUM('cleaned_sales_data'[Sales Amount])

-- Total Profit
Total Profit = SUM('cleaned_sales_data'[Profit])

-- Overall Profit Margin (%)
Profit Margin % = DIVIDE([Total Profit], [Total Sales]) * 100

-- Average Order Value
Avg Order Value = AVERAGE('cleaned_sales_data'[Sales Amount])
```

---

## 6. Build the Dashboard — Visual by Visual

### 6.1 KPI Cards
1. Click an empty canvas area
2. In **Visualizations** pane, select **Card** icon
3. Drag `Total Sales` measure into **Fields**
4. Format: *Display units = Thousands*, add a title "💰 Total Sales"
5. Repeat for `Total Profit` and `Profit Margin %`
6. Arrange the 3 cards side by side at the top

### 6.2 Monthly Sales Line Chart
1. Click **Line chart** in Visualizations
2. **X-Axis** → `Order Date` (set to Month hierarchy or drag `Month Name`)
3. **Y-Axis** → `Total Sales` measure
4. **Legend** → (optional) `Year` to compare years
5. Title: "📈 Monthly Sales Trend"

> **Tip:** Right-click the X-axis → *Sort Ascending by Month* to ensure correct order.

### 6.3 Sales by Category (Bar Chart)
1. Select **Clustered bar chart**
2. **Y-Axis** → `Product Category`
3. **X-Axis** → `Total Sales`
4. **Color** → enable data colors per bar (Format → Data Colors → turn on)
5. Title: "📦 Sales by Category"

### 6.4 Sales by Region (Clustered Bar Chart)
1. Select **Clustered bar chart**
2. **Y-Axis** → `Region`
3. **X-Axis** → `Total Sales`
4. Title: "🌍 Sales by Region"

### 6.5 Top 10 Products (Horizontal Bar)
1. Select **Bar chart** (horizontal)
2. **Y-Axis** → `Product Name`
3. **X-Axis** → `Total Sales`
4. In **Filters** pane → add `Product Name` as filter → set **Top N = 10** by `Total Sales`
5. Title: "🏆 Top 10 Products by Sales"

### 6.6 Map Visual
1. Select **Map** visual (or **Filled Map**)
2. **Location** → `Region`
3. **Size/Values** → `Total Sales`
4. Title: "🗺️ Sales by Region (Map)"

> **Note:** Power BI maps work best with actual geography. Since "Region" contains generic names (East, West etc.), use the **Filled Map** with custom regions or replace with a bar chart if bubbles don't appear correctly.

### 6.7 Slicers (Filters)
1. Select **Slicer** visual
2. Drag `Year` into **Field** → choose *List* style
3. Repeat for `Region` and `Product Category`
4. Place slicers on the left side or top of the canvas

---

## 7. Format the Dashboard

### Canvas settings
- **View → Page view → Fit to page** for best proportions
- Go to **Format Page** → Canvas background → choose a light grey (`#F5F5F5`) or dark theme

### Theme
- **Home → Themes** → pick "Executive" or "Teal" for a professional look
- Or upload a custom `.json` theme file

### Titles & Borders
- Select each visual → **Format visual** → turn on **Title**
- Add a border: **General → Effects → Visual border → On**

### Card formatting
- Format each KPI card: **Format visual → Callout value** → increase font size to 28–32 pt

---

## 8. Add a Report Title

1. **Insert → Text Box**
2. Type: **Sales Data Analysis Dashboard**
3. Font size: 28, Bold, dark blue or white if on dark background
4. Place at the top-centre of the canvas

---

## 9. Add Interactions

Power BI cross-filtering is automatic — clicking any bar or region will filter all other visuals. To customise:
- **Format → Edit Interactions** → choose which visuals respond to filters from each visual

---

## 10. Publish / Export

| Option | How |
|---|---|
| **Export PDF** | File → Export → Export to PDF |
| **Publish to Power BI Service** | Home → Publish → select your workspace |
| **Share as PBIX** | File → Save As → share the `.pbix` file |

---

## 11. Suggested Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│          💼 Sales Data Analysis Dashboard                   │
├─────────────┬──────────────────────┬────────────────────────┤
│ 💰 KPI:     │  📈 Monthly Sales    │  🗺️ Sales Map          │
│ Total Sales │      Trend           │   (by Region)          │
│ Total Profit│  (Line Chart)        │                        │
│ Margin %    │                      │                        │
├─────────────┴──────────┬───────────┴────────────────────────┤
│  📦 Sales by Category  │  🌍 Sales by Region                │
│  (Bar Chart)           │  (Bar Chart)                       │
├────────────────────────┴────────────────────────────────────┤
│                🏆 Top 10 Products by Sales                  │
│                (Horizontal Bar Chart)                       │
├─────────────────────────────────────────────────────────────┤
│  Slicers: [Year ▼]   [Region ▼]   [Category ▼]             │
└─────────────────────────────────────────────────────────────┘
```

---

## 12. Key Insights to Highlight on Dashboard

Add **Text Boxes** near each visual with callout insights, for example:

- 🏅 *"East region drives the highest revenue"*
- 📦 *"Technology is the top-selling category"*
- 📈 *"Q4 (Oct–Dec) sees a 30%+ sales spike — plan campaigns early"*

---

*Guide created for Power BI Desktop (latest version). Layout and option names may vary slightly between versions.*
