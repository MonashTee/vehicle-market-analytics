/* the syntaxs below answered questions on
How many rows does the table have?
Are there missing values?
Are there duplicates vehicles IDs?
Are the Columns names correct?
Can the data be trusted
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