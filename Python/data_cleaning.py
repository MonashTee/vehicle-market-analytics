import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

connection_string = quote_plus(
    "Driver={SQL SERVER};"
    "Server=RCCGAGADMIN\\SQLEXPRESS;"
    "Database=vehicle_market_analysis;"
    "Trusted_Connection=yes;"
)

engine= create_engine(
    f"mssql+pyodbc:///?odbc_connect={connection_string}"
                      )    

query = """
SELECT *
FROM dbo.used_cars
"""

df =pd.read_sql(query, engine)

print("Data fetched successfully from the database.")

print("\nFirst 5 rows of the DataFrame:", df.head())

print("\nDataFrame shape:", df.shape)

print("\nDataFrame information:")
df.info()

print("\nData types of each column:" , df.dtypes)

print("\nNumerical summary:", df.describe())

print("\nMissing values in each column:", df.isnull().sum())

print("\nDuplicated values in the DataFrame:", df.duplicated().sum())


## Data quality checks
# Check whether IDs are unique
print("\nUnique ID check:")
print("Unique IDs:", df["id"].nunique())
print("Duplicate IDs:", df["id"].duplicated().sum())

# Check the range of model years
print("\nModel year check:")
print("Earliest model year:", df["model_year"].min())
print("Latest model year:", df["model_year"].max())
print("Records before 1974:", (df["model_year"] < 1974).sum())
print("Records after 2024:", (df["model_year"] > 2024).sum())

# Check mileage and price for zero or negative values
print("\nMileage check:")
print("Zero mileage:", (df["milage"] == 0).sum())
print("Negative mileage:", (df["milage"] < 0).sum())
print("\nPrice check:")
print("Zero or negative prices:", (df["price"] <= 0).sum())

# Inspect the 10 highest-priced listings
print("\n10 highest-priced listings:")
print(
    df.nlargest(10, "price")[
        ["brand", "model", "model_year", "milage", "price"]
    ].to_string(index=False)
)

# Inspect the most common values in columns with missing data
print("\nFuel type distribution:")
print(df["fuel_type"].value_counts(dropna=False).head(10))

print("\nAccident information distribution:")
print(df["accident"].value_counts(dropna=False))

print("\nClean title distribution:")
print(df["clean_title"].value_counts(dropna=False))

# Investigate suspicious price values
print("\nPrice distribution:")
print(
    df["price"].describe(
        percentiles=[0.90, 0.95, 0.99, 0.999]
    )
)

print("\nMost frequent prices:")
print(df["price"].value_counts().head(10))

print("\nRecords with the maximum price:")
max_price = df["price"].max()

print(
    df.loc[
        df["price"] == max_price,
        ["id", "brand", "model", "model_year", "milage", "price"]
    ].to_string(index=False)
)

print("\nNumber of records with maximum price:")
print((df["price"] == max_price).sum())

# Check whether other extreme prices also repeat
print("\nHighest distinct price values:")
print(
    sorted(df["price"].unique(), reverse=True)[:15]
)

# Check missing values occurring in the same rows
print("\nMissing-value overlap:")
print(
    df[["fuel_type", "accident", "clean_title"]]
    .isnull()
    .sum(axis=1)
    .value_counts()
    .sort_index()
)

# Assess the impact of extreme prices
print("\nListings priced at 1,000,000 or more:")
extreme_prices = df[df["price"] >= 1_000_000]

print("Number of records:", len(extreme_prices))

print("\nExtreme prices and their frequencies:")
print(
    extreme_prices["price"]
    .value_counts()
    .sort_index(ascending=False)
)

print("\nOverall price statistics:")
print("Mean:", df["price"].mean())
print("Median:", df["price"].median())

# Sensitivity analysis only:
# Compare statistics without the repeated maximum price.
# This does NOT delete or modify the original DataFrame.

max_price = df["price"].max()
comparison_df = df[df["price"] != max_price]

print("\nSensitivity analysis excluding the maximum price value:")
print("Records remaining:", len(comparison_df))
print("Mean:", comparison_df["price"].mean())
print("Median:", comparison_df["price"].median())

print("\nPercentage of records at the maximum price:")
print(round((df["price"] == max_price).mean() * 100, 4), "%")

# Inspect fuel type values before standardization

print("\nAll distinct fuel type values:")
print(sorted(df["fuel_type"].dropna().unique()))

print("\nFuel type frequencies, including missing values:")
print(
    df["fuel_type"]
    .value_counts(dropna=False)
    .sort_values(ascending=False)
)

# Standardize missing values in fuel_type

df["fuel_type"] = df["fuel_type"].replace(
    ["–", "not supported"],
    pd.NA
)

print("\nFuel type distribution after cleaning:")
print(df["fuel_type"].value_counts(dropna=False))

print("\nMissing fuel_type values after cleaning:")
print(df["fuel_type"].isna().sum())

# Inspect accident values before cleaning

print("\nDistinct accident values:")
print(df["accident"].dropna().unique())

print("\nAccident distribution before cleaning:")
print(df["accident"].value_counts(dropna=False))

# Check for leading or trailing whitespace
print("\nAccident values with surrounding whitespace:")
non_missing_accident = df["accident"].dropna()

print(
    non_missing_accident[
        non_missing_accident
        != non_missing_accident.str.strip()
    ].value_counts()
)

# Inspect clean_title values before cleaning

print("\nDistinct clean_title values:")
print(df["clean_title"].dropna().unique())

print("\nClean title distribution:")
print(df["clean_title"].value_counts(dropna=False))

# Check for leading or trailing whitespace
non_missing_title = df["clean_title"].dropna()

print("\nClean title values with surrounding whitespace:")
print(
    non_missing_title[
        non_missing_title != non_missing_title.str.strip()
    ].value_counts()
)

# Final data quality summary

print("\n========== FINAL DATA QUALITY SUMMARY ==========")

print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate IDs:", df["id"].duplicated().sum())

print("\nMissing values by column:")
print(df.isna().sum())

print("\nTotal missing cells:", df.isna().sum().sum())

print("\nNumeric validation:")
print("Minimum model year:", df["model_year"].min())
print("Maximum model year:", df["model_year"].max())
print("Minimum mileage:", df["milage"].min())
print("Minimum price:", df["price"].min())
print("Maximum price:", df["price"].max())

print("\nFuel type categories:")
print(sorted(df["fuel_type"].dropna().unique()))

print("\nAccident categories:")
print(sorted(df["accident"].dropna().unique()))

print("\nClean title categories:")
print(sorted(df["clean_title"].dropna().unique()))

from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
output_folder = project_root / "Data"
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "used_cars_cleaned.csv"

df.to_csv(output_file, index=False)

print("\nCleaned dataset exported successfully.")
print("Output file:", output_file)
print("Exported rows:", len(df))
print("Exported columns:", len(df.columns))

engine.dispose()