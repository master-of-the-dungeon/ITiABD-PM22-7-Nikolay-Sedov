SELECT model
FROM aircrafts_data
GROUP BY model
ORDER BY COUNT(*) DESC
LIMIT 1;
