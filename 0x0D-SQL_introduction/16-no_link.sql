-- List all records of the second_table
-- Don't list rows without name
-- Order by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
