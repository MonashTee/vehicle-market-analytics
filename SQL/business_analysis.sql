/*==================
Business Analysis SQL Queries
===================*/

-- Brand Performance Analysis  

/* Business Question 1: Which vehicles brands have 
the most listings in the dataset
*/
SELECT brand, 
COUNT(*) AS total_listings
FROM used_cars
GROUP BY brand
ORDER BY total_listings DESC;

/* Business Question 2: What is the average listings 
price for each brand?
*/
SELECT brand,
COUNT(*) AS total_listings,
AVG(CAST(price AS DECIMAL(19,2))) AS avg_price
FROM used_cars
WHERE price IS NOT NULL
GROUP BY brand
ORDER BY avg_price DESC;

-- Vehicle Pricing Analysis

/* What are the 10 highest-priced vehicle listings
 in the dataset??
*/
SELECT TOP 10 brand, model, model_year, price
FROM used_cars
WHERE price IS NOT NULL
ORDER BY price DESC;

/* Business Question 4: What is the average price of vehicles 
by model year(do newer vehicles command higher prices)?
*/
SELECT model_year,
COUNT(*) AS total_listings,
AVG(CAST(price AS DECIMAL(19,2))) AS avg_price
FROM used_cars
WHERE price IS NOT NULL
GROUP BY model_year
ORDER BY model_year DESC;

-- Model Popularity Analysis 

/* Business Question 5: Which vehicle models appear most frequently
in the dataset for each brand?
*/
SELECT brand, model, COUNT(*) AS model_count
FROM used_cars
WHERE brand IS NOT NULL
  AND model IS NOT NULL
GROUP BY brand, model
ORDER BY brand, model_count DESC;

/* Business Question 6: What is the average listing price for each 
vehicle model with at least five listings?
*/
SELECT brand, model, COUNT(*) AS total_listings,
AVG(CAST(price AS DECIMAL(19,2))) AS avg_price
FROM used_cars
WHERE price IS NOT NULL
GROUP BY brand, model
HAVING COUNT(*) >= 5
ORDER BY avg_price DESC;

--Mileage and Age Analysis

/* Business Question 7: How do average prices vary across mileage ranges?
*/
WITH MileageGroups AS (
    SELECT
        CASE
            WHEN milage < 50000 THEN '0-50k'
            WHEN milage <= 100000 THEN '50k-100k'
            WHEN milage <= 150000 THEN '100k-150k'
            ELSE '150k+'
        END AS mileage_range,
        CASE
            WHEN milage < 50000 THEN 1
            WHEN milage <= 100000 THEN 2
            WHEN milage <= 150000 THEN 3
            ELSE 4
        END AS sort_order,
        price
    FROM used_cars
    WHERE price IS NOT NULL
      AND milage IS NOT NULL
)
SELECT
    mileage_range,
    AVG(CAST(price AS DECIMAL(19,2))) AS avg_price
FROM MileageGroups
GROUP BY mileage_range, sort_order
ORDER BY sort_order;
 
