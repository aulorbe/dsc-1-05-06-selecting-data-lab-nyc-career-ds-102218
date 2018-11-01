--UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;

UPDATE planets
SET num_of_moons = 68
WHERE name = 'Jupiter'
