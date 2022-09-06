-- Counts no of records with same score and lists them

SELECT DISTINCT score, COUNT(score) as number
FROM second_table;

