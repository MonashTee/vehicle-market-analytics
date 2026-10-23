# Key Findings

## Data Quality

- Dataset contains 188,533 records.
- Currency is not specified.
- Maximum vehicle price is 2,954,083.
- Minimum vehicle price is 2,000.
- The initial highest-price query returned 50 records with the same maximum price of 2,954,083 across different vehicle brands and models. This pattern requires further investigation before the highest-priced listings can be interpreted as a reliable ranking.

That is an observation, not a conclusion that the data is incorrect.

## Brand Analysis

- Ford had the highest number of  listings.
- Bugatti had the highest average listing price in the dataset at 169,600 across 7 listings, followed by Lamborghini at approximately 159,176 across 809 listings.
- Business interpretation: The results show that brands with higher average prices are not necessarily the brands with the largest number of listings. Comparing average prices alongside listing counts provides a more informative view of the advertised vehicle listings in the dataset.

## Pricing Analysis

- Average prices generally increase across more recent model years in this dataset, rising from approximately 30,975 for 2015 to 95,708 for 2023. The 2023 average is based on 8,769 listings. The 2024 average is lower, at approximately 78,006 across 162 listings. Some older model years, including 1994 and 1974, also have relatively high average prices, but their listing counts are much smaller.
- Business interpretation: Comparing average prices by model year helps identify pricing patterns across vehicle listings. However, the results may also reflect differences in the brands, models, mileage and condition of vehicles listed for each year.

## Model Analysis

- The query identifies the frequency of each brand–model combination in the dataset. Examples include Ford F-150 XLT (2,934 records), BMW M3 Base (2,195), and Tesla Model Y Long Range (789).
- Business interpretation: Comparing the number of records for each brand–model combination helps describe which models are most represented in this dataset. Listing frequency does not necessarily indicate customer demand or actual sales performance.

- The analysis ranks vehicle brand–model combinations by their average recorded price, including only combinations with at least five listings. Among the displayed results, the Porsche Carrera GT Base has the highest average price at 356,937.25 across 8 listings, followed by the Lamborghini Gallardo SE at 275,387.05 across 21 listings.
- Business interpretation: Comparing average prices by brand and model helps identify differences in recorded prices across vehicle types. Including a minimum of five listings reduces the influence of combinations represented by only one or two records. However, the number of listings and the variation in vehicle characteristics should also be considered when interpreting the averages.

## Mileage and age Analysis

- Average recorded prices decrease as mileage increases across the four mileage groups. Vehicles in the 0–50k range have the highest average price at approximately 68,245.35, while vehicles in the 150k+ range have the lowest average at approximately 13,137.87. The two middle groups have average prices of approximately 30,997.61 and 16,836.29, respectively.
- Business interpretation: Mileage ranges can help describe price differences across used-vehicle listings. The results suggest that lower-mileage vehicles tend to have higher recorded prices in this dataset. This comparison could support exploratory pricing analysis.

## Recommendations

- Investigate extremely high-priced vehicles for possible outliers.
