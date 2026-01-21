from pathlib import Path
import pandas as pd 

RAW_PATH = Path("data/raw/sales_raw.csv")
OUT_PATH = Path("data/processed/sales_clean.csv")

def main():
    df = pd.read_csv(RAW_PATH)

    # basic inspection
    print("Rows/Cols:", df.shape)
    print(df.head(3))
    print("\nMissing values:\n", df.isna().sum())

    # clean: drop rows missing critical fields
    df = df.dropna(subset=["order_date", "customer_id", "product", "category"])

    # clean: fill missing numeric values with 0
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)

    # clean: fill missing city
    df["city"] = df["city"].fillna("Unknown").str.strip()

    #add derived column: total_amount
    df["total_amount"] = (df["unit_price"] * df["quantity"]).round(2)

    #ensure output folder exists
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUT_PATH, index=False)
    print(f"\nSaved clean data to: {OUT_PATH} | rows={len(df)}")


if __name__ == "__main__":
    main()