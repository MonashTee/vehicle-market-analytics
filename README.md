# Vehicle Market Analytics

## Project Overview

This project analyses a used-car listing dataset using SQL Server, Python, Excel, and Power BI.

The objective is to examine vehicle listing prices, compare brand and model listing volumes, explore vehicle characteristics, and assess data quality to support used-vehicle market analysis and reporting.

---

## Business Problem

Vehicle marketplaces, dealers, and exporters need to understand the composition and pricing patterns of vehicle listings to support market research and reporting.

This project investigates four key areas:

- **Brand and model representation:** Which vehicle brands and models have the highest listing volumes, and how do their recorded prices differ?
- **Vehicle pricing patterns:** How do advertised prices vary across brands, model years, mileage ranges, fuel types, and price bands?
- **Vehicle characteristics:** How are listings distributed by mileage, fuel type, transmission, accident status, and clean-title information?
- **Data quality and reporting reliability:** How do missing values, inconsistent categorical entries, and unusually high listed prices affect data interpretation and reporting?

SQL Server, Python, and Excel are used to analyse and interpret the listing data, while Power BI is being used to develop an interactive dashboard.

The analysis focuses on recorded vehicle listings. Listing volumes do not establish actual buyer demand or sales performance, and advertised prices are not confirmed selling prices.

---

## Dataset

**Source:** Kaggle — Used Cars Dataset

**Dataset Size:** 188,533 vehicle records

Key fields include:

- Brand
- Model
- Model Year
- Mileage
- Fuel Type
- Engine
- Transmission
- Accident Status
- Clean Title
- Price

**Dataset limitation:** The currency used for vehicle prices is not specified. All price-related analysis therefore uses the reported values without applying currency conversion.

---

## Tools Used

- SQL Server and SQL Server Management Studio (SSMS)
- Python (Pandas, NumPy)
- Microsoft Excel
- Microsoft Power BI
- Git and GitHub

---

## Project Workflow

### 1. Data Acquisition

- Obtained the used-car dataset from Kaggle.
- Imported the data into SQL Server for analysis.

### 2. Data Quality Assessment

- Validated dataset row counts.
- Assessed missing values across key fields.
- Checked for duplicate records and IDs.
- Profiled data distributions and investigated unusually high recorded prices.

### 3. SQL Business Analysis

- Analysed listing volumes by brand and brand–model combination.
- Compared average recorded prices across brands and models.
- Examined pricing patterns across model years and mileage ranges.
- Investigated vehicle age and mileage characteristics.

### 4. Data Cleaning and Transformation

- Standardised inconsistent categorical values.
- Assessed and handled missing values.
- Checked for duplicate records.
- Created derived fields to support analysis.

### 5. Python Exploratory Data Analysis

- Examined price distributions using mean, median, and percentiles.
- Investigated extreme recorded prices and tested their influence on summary statistics.
- Compared mean and median prices across mileage groups and brands.
- Analysed recorded prices and mileage by fuel type.

### 6. Excel Analysis

- Compared price-band distributions across accident-status groups using PivotTables and a 100% stacked column chart.
- Summarised price distributions using statistical formulas.
- Applied the interquartile range (IQR) method to flag potential price outliers for further review.

### 7. Power BI Dashboard

- Develop a single-page interactive dashboard summarising listing volumes, pricing patterns, and vehicle characteristics.
- Enable exploration through filters for selected vehicle attributes.

---

## Project Structure

```text
Vehicle-Market-Analytics/
├── Data/
├── SQL/
├── Python/
├── Excel/
├── PowerBI/
├── Docs/
├── image/
└── README.md
```

---

## Limitations

- **Currency:** The dataset does not specify the currency used for vehicle prices. Reported prices are analysed without currency conversion.
- **Listing prices:** Prices represent recorded advertised prices, not confirmed selling prices.
- **Market trends:** The dataset does not provide historical listing dates or snapshots, so it cannot establish changes in market prices over time.
- **Demand and performance:** Listing counts indicate the representation of brands and models in the dataset, not actual buyer demand, sales performance, or profitability.
- **Data completeness:** Missing accident or clean-title information indicates that the relevant information was not recorded; it does not establish a negative vehicle history.
- **Unusual prices:** Extremely high recorded prices were flagged for further investigation but have not been confirmed as data errors. No records were removed solely because of these unusually high prices.
