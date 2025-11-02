import os
import pandas as pd

STAGED_PATH = "data/staged/Superstore_staged.csv"
CLEAN_PATH = "data/clean/Superstore_clean.csv"

def transform_data():
    print("Starting transformation process...")

    if not os.path.exists(STAGED_PATH):
        print(f"❌ Staged data not found at {STAGED_PATH}")
        return

    # Load staged data
    df = pd.read_csv(STAGED_PATH)
    print(f"✅ Loaded staged data. Rows: {len(df)} | Columns: {len(df.columns)}")

    # --- Step 1: Basic cleaning ---
    print("🧹 Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna(subset=["Order ID", "Sales", "Profit"], how="any")

    # --- Step 2: Rename columns (make them consistent) ---
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # --- Step 3: Create new calculated columns ---
    df["profit_margin"] = df["profit"] / df["sales"]
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    # --- Step 4: Filter out invalid or test data ---
    df = df[df["sales"] > 0]

    # --- Step 5: Save cleaned data ---
    os.makedirs("data/clean", exist_ok=True)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"📦 Cleaned data saved to: {CLEAN_PATH}")

    print("\n✅ Transformation completed successfully!")
    print(df.head())

if __name__ == "__main__":
    transform_data()
