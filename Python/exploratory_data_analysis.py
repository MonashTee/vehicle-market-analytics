from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

project_root = Path(__file__).resolve().parent.parent
file_path = project_root / "Data" / "used_cars_cleaned.csv"

df = pd.read_csv(file_path)
print("Data loaded successfully from:", file_path)
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five rows:")
print(df.head())


# ==========================================
# 1. PRICE DISTRIBUTION ANALYSIS
# ==========================================

# Ensure price is numeric and exclude missing values
prices = pd.to_numeric(df["price"], errors="coerce").dropna()

# Calculate descriptive statistics
price_stats = prices.describe(
    percentiles=[0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
)

print("\n--- PRICE DISTRIBUTION ---")
print(f"Valid price records: {len(prices):,}")
print(f"Mean price: {prices.mean():,.2f}")
print(f"Median price: {prices.median():,.2f}")
print(f"Minimum price: {prices.min():,.2f}")
print(f"Maximum price: {prices.max():,.2f}")

print("\nPrice percentiles:")
print(price_stats.loc[
    ["25%", "50%", "75%", "90%", "95%", "99%"]
].to_string())

# Investigate unusually high recorded prices
print("\n--- HIGH-PRICE INVESTIGATION ---")

million_plus = prices[prices >= 1_000_000]

print(f"Listings priced at 1,000,000 or more: {len(million_plus):,}")

print("\nTen highest distinct recorded prices and their counts:")
print(
    prices.value_counts()
    .sort_index(ascending=False)
    .head(10)
    .to_string()
)


# ==========================================
# 1.2. INVESTIGATE EXTREME RECORDED PRICES
# ==========================================

high_price_records = df.loc[
    pd.to_numeric(df["price"], errors="coerce") >= 1_000_000,
    ["price", "brand", "model", "model_year", "milage"]
].copy()

# Check whether each extreme price appears across different brands and models
price_frequency = (
    high_price_records
    .groupby("price")
    .agg(
        listings=("price", "size"),
        distinct_brands=("brand", "nunique"),
        distinct_models=("model", "nunique")
    )
    .sort_index(ascending=False)
)

print("\n--- EXTREME PRICE VALUES BY BRAND AND MODEL DIVERSITY ---")
print(price_frequency.to_string())

# Identify brand-model combinations that appear most often
brand_model_counts = (
    high_price_records
    .groupby(["brand", "model"])
    .size()
    .sort_values(ascending=False)
)

print("\n--- MOST FREQUENT BRAND-MODEL COMBINATIONS AMONG EXTREME PRICES ---")
print(brand_model_counts.head(15).to_string())

# Inspect examples of the highest-priced records
print("\n--- EXAMPLE EXTREME-PRICE RECORDS ---")
print(
    high_price_records
    .sort_values("price", ascending=False)
    .head(20)
    .to_string(index=False)
)

# ==========================================
# 1.3. PRICE SENSITIVITY CHECK
# ==========================================

# These price values are flagged for investigation,
# not confirmed invalid records.
flagged_prices = [2954083, 1950995, 1599000]

# Create a separate series for comparison.
# The original dataframe remains unchanged.
diagnostic_prices = prices[~prices.isin(flagged_prices)]

print("\n--- PRICE SENSITIVITY CHECK ---")

print("\nAll valid price records:")
print(f"Listings: {len(prices):,}")
print(f"Mean price: {prices.mean():,.2f}")
print(f"Median price: {prices.median():,.2f}")

print("\nExcluding the three flagged price values (diagnostic only):")
print(f"Listings: {len(diagnostic_prices):,}")
print(f"Mean price: {diagnostic_prices.mean():,.2f}")
print(f"Median price: {diagnostic_prices.median():,.2f}")

mean_difference = prices.mean() - diagnostic_prices.mean()

print("\nDifference in mean price:")
print(f"{mean_difference:,.2f}")
print(
    f"Percentage change relative to the original mean: "
    f"{mean_difference / prices.mean() * 100:.2f}%"
)


# ==========================================
# 2. MILEAGE VERSUS PRICE ANALYSIS
# ==========================================

# Prepare the columns required for this analysis
mileage_df = df[["milage", "price"]].copy()

mileage_df["milage"] = pd.to_numeric(
    mileage_df["milage"], errors="coerce"
)
mileage_df["price"] = pd.to_numeric(
    mileage_df["price"], errors="coerce"
)

mileage_df = mileage_df.dropna(subset=["milage", "price"])

# Create mileage groups consistent with the SQL analysis
bins = [0, 50_000, 100_000, 150_000, float("inf")]

labels = [
    "Up to 50,000",
    "50,001–100,000",
    "100,001–150,000",
    "Over 150,000"
]

mileage_df["mileage_group"] = pd.cut(
    mileage_df["milage"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Compare mean and median prices within each group
mileage_analysis = (
    mileage_df
    .groupby("mileage_group", observed=False)
    .agg(
        listings=("price", "count"),
        mean_price=("price", "mean"),
        median_price=("price", "median"),
        median_mileage=("milage", "median")
    )
    .round(2)
)

print("\n--- MILEAGE VERSUS PRICE ---")
print(mileage_analysis.to_string())

# Visualise mean versus median price
ax = mileage_analysis[
    ["mean_price", "median_price"]
].plot(
    kind="bar",
    figsize=(10, 6),
    width=0.8
)

ax.set_title("Mean and Median Recorded Price by Mileage Group")
ax.set_xlabel("Mileage group")
ax.set_ylabel("Recorded price")
ax.legend(["Mean price", "Median price"])
ax.ticklabel_format(style="plain", axis="y")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ==========================================
# 3. FUEL TYPE VERSUS PRICE ANALYSIS
# ==========================================

fuel_df = df[["fuel_type", "price", "milage"]].copy()

# Ensure the numeric columns are numeric
fuel_df["price"] = pd.to_numeric(
    fuel_df["price"], errors="coerce"
)
fuel_df["milage"] = pd.to_numeric(
    fuel_df["milage"], errors="coerce"
)

# Keep missing fuel types visible in the analysis
fuel_df["fuel_type"] = fuel_df["fuel_type"].fillna(
    "Missing / not recorded"
)

# Compare listing counts, prices and mileage
fuel_analysis = (
    fuel_df
    .dropna(subset=["price", "milage"])
    .groupby("fuel_type")
    .agg(
        listings=("price", "count"),
        mean_price=("price", "mean"),
        median_price=("price", "median"),
        median_mileage=("milage", "median")
    )
    .sort_values("median_price", ascending=False)
    .round(2)
)

print("\n--- FUEL TYPE VERSUS PRICE ---")
print(fuel_analysis.to_string())

# Visualise median price by fuel type
ax = fuel_analysis["median_price"].sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

ax.set_title("Median Recorded Price by Fuel Type")
ax.set_xlabel("Median recorded price")
ax.set_ylabel("Fuel type")
ax.ticklabel_format(style="plain", axis="x")

plt.tight_layout()
plt.show()


# ==========================================
# 4. BRAND PRICE RELIABILITY ANALYSIS
# ==========================================

brand_df = df[["brand", "price"]].copy()

brand_df["price"] = pd.to_numeric(
    brand_df["price"], errors="coerce"
)

brand_df = brand_df.dropna(subset=["brand", "price"])

# Summarise prices for each brand
brand_analysis = (
    brand_df
    .groupby("brand")
    .agg(
        listings=("price", "count"),
        mean_price=("price", "mean"),
        median_price=("price", "median")
    )
)

# Exclude brands with fewer than 100 listings
# to reduce the influence of very small samples.
# This is an analytical cutoff, not a universal rule.
brand_analysis = brand_analysis[
    brand_analysis["listings"] >= 100
].copy()

# Compare the mean with the median
brand_analysis["mean_median_gap"] = (
    brand_analysis["mean_price"]
    - brand_analysis["median_price"]
)

brand_analysis["mean_median_ratio"] = (
    brand_analysis["mean_price"]
    / brand_analysis["median_price"]
)

# Show brands with the highest median prices
top_median_brands = (
    brand_analysis
    .sort_values("median_price", ascending=False)
    .head(15)
)

print("\n--- TOP 15 BRANDS BY MEDIAN PRICE ---")
print(
    top_median_brands[
        [
            "listings",
            "mean_price",
            "median_price",
            "mean_median_gap"
        ]
    ].round(2).to_string()
)

# Identify brands where the mean is high relative to the median
largest_gaps = (
    brand_analysis
    .sort_values("mean_median_ratio", ascending=False)
    .head(10)
)

print("\n--- BRANDS WITH LARGEST MEAN-TO-MEDIAN PRICE RATIOS ---")
print(
    largest_gaps[
        [
            "listings",
            "mean_price",
            "median_price",
            "mean_median_ratio"
        ]
    ].round(2).to_string()
)

# Visualise the 10 brands with the highest median prices
top_10_brands = (
    brand_analysis
    .nlargest(10, "median_price")
    .sort_values("median_price")
)

ax = top_10_brands["median_price"].plot(
    kind="barh",
    figsize=(10, 6)
)

ax.set_title("10 Highest Median-Price Brands (At Least 100 Listings)")
ax.set_xlabel("Median recorded price")
ax.set_ylabel("Brand")
ax.ticklabel_format(style="plain", axis="x")

plt.tight_layout()
plt.show()

# Visualise the distribution up to the 99th percentile.
# This is a display choice only; no records are deleted from the analysis.
price_99th_percentile = prices.quantile(0.99)
prices_for_chart = prices[prices <= price_99th_percentile]

plt.figure(figsize=(10, 6))
plt.hist(prices_for_chart, bins=40, edgecolor="black")
plt.title("Distribution of Recorded Vehicle Prices (Up to 99th Percentile)")
plt.xlabel("Recorded Price")
plt.ylabel("Number of Listings")
plt.ticklabel_format(style="plain", axis="x")
plt.tight_layout()
plt.show()

# Box plot using the same display range
plt.figure(figsize=(10, 4))
plt.boxplot(prices_for_chart, orientation="horizontal")
plt.title("Recorded Vehicle Prices (Up to 99th Percentile)")
plt.xlabel("Recorded Price")
plt.ticklabel_format(style="plain", axis="x")
plt.tight_layout()
plt.show()
