# Vehicle Market Analytics

## Project Overview

This project analyses a large-scale used-car dataset using SQL Server, Python, Excel, and Power BI.

The objective is to explore vehicle pricing trends, assess data quality, identify high-demand vehicle segments, and develop reporting dashboards that support business decision-making.

---

## Business Problem

Vehicle dealers and exporters need insights into:

- High-performing vehicle brands and models
- Vehicle pricing patterns
- Inventory characteristics
- Market trends
- Data quality issues impacting reporting

This project uses data analytics techniques to transform raw vehicle listing data into actionable business insights.

---

## Dataset

**Source:** Kaggle - Used Cars Dataset

**Dataset Size:**
- Approximately 188,533 vehicle records

Key fields include:

- Brand
- Model
- Model Year
- Mileage
- Fuel Type
- Engines
- Transmission
- Accident History
- Price

---

## Tools Used

- SQL Server
- Python (Pandas, NumPy)
- Excel
- Power BI
- Git & GitHub

---

## Project Workflow

### 1. Data Acquisition

- Downloaded raw vehicle dataset
- Imported data into SQL Server

### 2. Data Quality Assessment

- Row count validation
- Missing value analysis
- Duplicate record checks
- Data profiling

### 3. SQL Business Analysis

- Brand performance analysis
- Vehicle pricing analysis
- Model popularity analysis
- Mileage and age analysis

### 4. Data Cleaning & Transformation

- Removed duplicates
- Handled missing values
- Standardised data formats
- Created derived business metrics

### 5. Dashboard Development

- Excel reporting dashboard
- Power BI executive dashboard

---

## Project Structure

```text
Vehicle-Market-Analytics
│
├── data
├── sql
├── python
├── excel
├── powerbi
├── images
├── docs
└── README.md

### Limitation

The dataset does not specify the currency used for the vehicle prices. Therefore, all price related analysis is performed using the reported values without applying currency conversion.