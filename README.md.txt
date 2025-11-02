# 🧱 Mini Data Engineering Project — Superstore ETL Pipeline

This is a beginner-friendly **Data Engineering + Data Analysis** project built from scratch using Python.

---

## 🚀 Overview

This project demonstrates a simple **ETL (Extract → Transform → Load)** pipeline using the **Superstore Sales Dataset**.

**Goal:**  
To clean, aggregate, and analyze retail data to identify top-performing regions, categories, and profit margins.

---

## 🧩 Steps

### 1. Extract
- Ingested raw Superstore CSV data.
- Handled encoding and missing values.
- Stored staged data in `/data/staged/`.

### 2. Transform
- Cleaned column names and data types.
- Calculated total sales, profit, and profit margins.
- Saved to `/data/clean/`.

### 3. Load
- Aggregated metrics by region and category.
- Exported a final dataset to `/data/warehouse/final_superstore.csv`.

### 4. Explore
- Visualized key insights in Jupyter Notebook:
  - Total Sales by Region
  - Total Profit by Category
  - Average Profit Margin by Region

---

## 📊 Insights Summary
- The **West region** has the highest total sales.
- The **Technology category** generates the most profit.
- The **Central region** shows the highest average profit margin.

---

## 🛠️ Tech Stack
- Python (Pandas, Matplotlib)
- Jupyter Notebook
- Virtual Environment (venv)
- Git + GitHub

---

## 🧠 Learning Outcomes
- Built an end-to-end ETL pipeline.
- Structured and automated data cleaning.
- Created simple but meaningful visualizations.
- Gained exposure to both Data Engineering and Data Analysis.

---

## 📁 Folder Structure
data_engineering_project/
├── data/
├── scripts/
├── notebooks/
└── README.md


---

## 🌟 Next Steps
- Automate ETL with **Airflow** (intermediate level).
- Move processed data into a **SQL or cloud warehouse**.
- Visualize results in **Power BI or Tableau**.
