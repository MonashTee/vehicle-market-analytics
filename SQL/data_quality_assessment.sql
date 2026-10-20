/* the syntaxs below answered questions on
How many rows does the table have?
Are there missing values?
Are there duplicates vehicles IDs?
Are the Columns names correct?
Can the data be trusted
what brands/models exist in the dataset?
Are there any suspicious values?
what does the price distribution look like?
*/

SELECT COUNT(*) AS Totalrows
FROM used_cars;

SELECT COUNT(*) - 
COUNT(price) AS MissingPrice
FROM used_cars;

SELECT COUNT(*) -
COUNT(brand) AS MissingBrand
FROM used_cars;

SELECT COUNT(*) -
COUNT(model) AS MissingModel
FROM used_cars;

SELECT id,
COUNT(*) AS DuplicateID
FROM used_cars
GROUP BY id 
HAVING COUNT(*) >1;

SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'used_cars';

SELECT DISTINCT brand
FROM used_cars
ORDER BY brand;

SELECT 
MAX(price) AS MaxPrice,
MIN(price) AS MinPrice,
AVG(CAST(price AS DECIMAL(10,2))) AS AvgPrice
FROM used_cars;

SELECT TOP 20
brand, model, price, model_year, milage
FROM used_cars
ORDER BY price DESC;

-- Data Profiling Findings
-- Currency not specified in dataset.
/* Price Range:
Min price = 2,000
Max price = 2,954,083
Avg price = 43,878
Further investigation required to determine on high-value
vehicle recods*/


