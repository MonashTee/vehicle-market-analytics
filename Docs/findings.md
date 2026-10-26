# Key Findings

## Data Quality

- Dataset contains 188,533 records.
- The currency is not specified in the dataset.
- Maximum vehicle price is 2,954,083.
- Minimum vehicle price is 2,000.
- The initial highest-price query returned 50 records with the same maximum price of 2,954,083 across different vehicle brands and models. This repeated value warrants further investigation and should not be treated as proof that the data is incorrect or as a reliable price ranking.

## SQL Findings

### Brand Analysis

- Ford had the highest number of listings.
- Bugatti had the highest average listing price in the dataset at 169,600 across 7 listings, followed by Lamborghini at approximately 159,176 across 809 listings.
- Business interpretation: The results show that brands with higher average prices are not necessarily the brands with the largest number of listings. Comparing average prices alongside listing counts provides a more informative view of the advertised vehicle listings in the dataset.

### Pricing Analysis

- Average prices generally increase across more recent model years in this dataset, rising from approximately 30,975 for 2015 to 95,708 for 2023. The 2023 average is based on 8,769 listings. The 2024 average is lower, at approximately 78,006 across 162 listings. Some older model years, including 1994 and 1974, also have relatively high average prices, but their listing counts are much smaller.
- Business interpretation: Comparing average prices by model year helps identify pricing patterns across vehicle listings. However, the results may also reflect differences in the brands, models, mileage and condition of vehicles listed for each year.

### Model Analysis

- The query identifies the frequency of each brand–model combination in the dataset. Examples include Ford F-150 XLT (2,934 records), BMW M3 Base (2,195), and Tesla Model Y Long Range (789).
- Business interpretation: Comparing the number of records for each brand–model combination helps describe which models are most represented in this dataset. Listing frequency does not necessarily indicate customer demand or actual sales performance.
- The analysis ranks vehicle brand–model combinations by their average recorded price, including only combinations with at least five listings. Among the displayed results, the Porsche Carrera GT Base has the highest average price at 356,937.25 across 8 listings, followed by the Lamborghini Gallardo SE at 275,387.05 across 21 listings.
- Business interpretation: Comparing average prices by brand and model helps identify differences in recorded prices across vehicle types. Including a minimum of five listings reduces the influence of combinations represented by only one or two records. However, the number of listings and the variation in vehicle characteristics should also be considered when interpreting the averages.

### Mileage and age Analysis

- Average recorded prices decline across the four mileage groups: approximately 67,881 for listings with mileage up to 50,000; 30,936 for listings with mileage between 50,001 and 100,000; 16,836 for listings with mileage between 100,001 and 150,000; and 13,138 for listings above 150,000.
- Business interpretation: Mileage ranges can help describe price differences across used-vehicle listings. The results suggest that lower-mileage vehicles tend to have higher recorded average prices in this dataset. This comparison could support exploratory pricing analysis.


## Python Exploratory Data Analysis

### Price Distribution and extreme values

- The dataset contains 188,533 vehicle listings. The mean recorded price is 43,878.02, while the median is 30,825.
- The 99th percentile is 259,500, compared with a maximum recorded price of 2,954,083, indicating a strongly right-skewed price distribution.
- A total of 148 listings have recorded prices of 1,000,000 or more. These listings share three repeated price values across numerous brands and models.
- In a sensitivity check excluding those 148 records, the mean decreases from 43,878.02 to 42,208.80 (approximately 3.80%), while the median decreases from 30,825 to 30,775.
- These unusually high values warrant further investigation, but they have not been confirmed as errors. No records were removed from the cleaned dataset.


### Mileage and Price

- Median recorded prices decline across the four mileage groups: 48,500 for listings with up to 50,000 mileage, 25,900 for 50,001–100,000, 13,000 for 100,001–150,000, and 9,750 for listings above 150,000.
- Mean prices exceed median prices in all four groups, suggesting that higher-priced listings influence the averages.
- The SQL and Python mean-price calculations were cross-checked and matched when consistent mileage-group boundaries were applied.
- These findings support using median prices alongside averages. However, the observed relationship does not establish that mileage alone explains price differences.

### Fuel-Type Comparison

- Hybrid listings have the highest median recorded price among the recorded fuel categories, at 44,900.
- Plug-In Hybrid listings have a median recorded price of 38,880, followed by Diesel at 38,500 and Gasoline at 29,999.
- E85 Flex Fuel listings have the lowest median recorded price, at 19,900, and the highest median mileage, at 98,000.
- Fuel type was missing for 5,879 listings. These records were analysed separately rather than treated as an actual fuel category.
- These differences are descriptive and may also reflect vehicle age, brand, model and other characteristics.

### Brand Price Reliability

- Among brands with at least 100 listings, Lamborghini has the highest median recorded price at 102,000, followed by McLaren at 87,500 and Rivian at 78,000.
- Pontiac has the largest mean-to-median price ratio among the analysed brands, at approximately 2.05. Its mean recorded price is 22,528.21, compared with a median of 10,999.50.
- Differences between mean and median prices show that average prices may not represent typical listings equally well across brands.
- Brand price comparisons should be interpreted alongside listing counts and differences in vehicle characteristics.

### Overall Interpretation

The Python analysis extends the SQL findings by examining price distribution, testing the influence of unusually high values, comparing mean and median prices, and introducing fuel-type comparisons. The results support using median prices alongside averages in subsequent analysis and dashboard design.

The dataset represents vehicle listings, not confirmed sales. It does not establish realised selling prices or actual market demand. 

## Recommendations

- Investigate the 148 listings with recorded prices of 1,000,000 or more, particularly the three repeated price values, before relying on the highest-price rankings.
- Use median prices alongside averages when comparing vehicles, mileage groups and brands because high-priced listings can influence mean prices.
- Interpret fuel-type and brand comparisons alongside listing counts and vehicle characteristics rather than assuming that any single factor explains price differences.
- Use the verified findings to guide the selection of meaningful Excel analyses and Power BI dashboard visuals.