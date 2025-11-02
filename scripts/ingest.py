import os
import pandas as pd

RAW_DATA_PATH = "data/raw/Superstore.csv"   # 👈 change if your file name differs
STAGED_DATA_PATH = "data/staged/Superstore_staged.csv"

def ingest_data():
    print("Starting ingestion process...")

    if not os.path.exists(RAW_DATA_PATH):
        print(f"❌ File not found: {RAW_DATA_PATH}")
        return

    try:
        # Some Superstore CSVs use "ISO-8859-1" or "latin1" encoding instead of utf-8
        df = pd.read_csv(RAW_DATA_PATH, encoding="latin1")
        print(f"✅ Loaded CSV successfully. Rows: {len(df)} | Columns: {len(df.columns)}")

    except Exception as e:
        print("❌ Failed to read CSV file.")
        print(e)
        return

    print("\n🔍 Preview of data:")
    print(df.head())

    os.makedirs("data/staged", exist_ok=True)
    df.to_csv(STAGED_DATA_PATH, index=False)
    print(f"\n📦 Data saved to staged folder: {STAGED_DATA_PATH}")

if __name__ == "__main__":
    ingest_data()
