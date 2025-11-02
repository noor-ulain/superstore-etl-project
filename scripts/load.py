import os
import pandas as pd

CLEAN_PATH = "data/clean/Superstore_clean.csv"
WAREHOUSE_PATH = "data/warehouse/sales_summary.csv"

def load_data():
    print("🏗️ Starting Load Process...")

    if not os.path.exists(CLEAN_PATH):
        print(f"❌ Clean data not found at {CLEAN_PATH}")
        return

    # Step 1: Load cleaned data
    df = pd.read_csv(CLEAN_PATH)
    print(f"✅ Loaded clean data. Rows: {len(df)} | Columns: {len(df.columns)}")

    # Step 2: Aggregate to create a "warehouse-style" summary table
    print("📊 Aggregating sales and profit by region and category...")
    summary = (
        df.groupby(["region", "category"], as_index=False)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            avg_profit_margin=("profit_margin", "mean"),
        )
    )

    # Step 3: Round numbers for readability
    summary["total_sales"] = summary["total_sales"].round(2)
    summary["total_profit"] = summary["total_profit"].round(2)
    summary["avg_profit_margin"] = (summary["avg_profit_margin"] * 100).round(2)

    # Step 4: Save to warehouse folder
    os.makedirs("data/warehouse", exist_ok=True)
    summary.to_csv(WAREHOUSE_PATH, index=False)
    print(f"✅ Summary data saved to: {WAREHOUSE_PATH}")

    print("\n🔍 Preview of your warehouse table:")
    print(summary.head())

if __name__ == "__main__":
    load_data()
