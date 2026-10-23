# Vehicle Market Analytics — Data Quality Report

## 1. Purpose

This report documents the initial data-quality checks and cleaning decisions applied to the used-car listings dataset before exploratory analysis and dashboard development.

## 2. Dataset Overview

| Check | Result |
|---|---:|
| Rows | 188,533 |
| Columns | 13 |
| Duplicate rows | 0 |
| Duplicate IDs | 0 |
| Total missing cells after cleaning | 29,750 |

The dataset includes vehicle identifiers, brands, models, model years, mileage, fuel types, engine and transmission details, colours, accident information, clean-title information and prices.

## 3. Missing Values

| Column | Missing values after cleaning |
|---|---:|
| `fuel_type` | 5,879 |
| `accident` | 2,452 |
| `clean_title` | 21,419 |
| All other columns | 0 |

Missing values were retained rather than filled with assumptions.

- Missing `fuel_type` values were left missing when the fuel type could not be established.
- Missing `accident` values were not interpreted as evidence that no accident had occurred.
- Missing `clean_title` values were not automatically converted to `Yes` or `No`.

## 4. Cleaning Decisions

### Fuel type

The values `–` and `not supported` were normalised to missing values (`pd.NA`).

This increased the missing count from 5,083 to 5,879. The change reflects the treatment of 796 placeholder entries, not the deletion of records.

### Duplicate checks

The dataset was checked for duplicate rows and duplicate IDs. No duplicates were found, so no rows were removed for duplication.

### Price values

Price values were retained in the cleaned dataset while further investigation is pending.

The maximum recorded price is 2,954,083, and 50 listings have this value. In total, 148 listings have prices of at least 1,000,000.

These repeated extreme values may affect averages and visualisations. However, the available checks have not established whether they are errors or valid high-value listings. They will be investigated during EDA rather than automatically removed.

## 5. Export

The cleaned DataFrame was exported to:

`Data/used_cars_cleaned.csv`

The export is intended to provide a consistent input for Python EDA and dashboard development.

## 6. Limitations

- The currency has not been confirmed from the available dataset information.
- Missing accident and clean-title information limits what can be concluded about vehicle condition.
- Extreme price values require further investigation.
- Cleaning placeholders does not guarantee that every field is accurate or complete.

## 7. Next Steps

1. Complete exploratory analysis of the cleaned CSV.
2. Investigate the extreme prices and compare summary statistics with and without flagged records.
3. Compare mean and median prices across mileage and age groups.
4. Use verified results to inform dashboard metrics and document the remaining limitations.
