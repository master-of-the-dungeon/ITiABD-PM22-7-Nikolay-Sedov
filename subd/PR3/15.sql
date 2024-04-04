WITH numbered_series AS (
  SELECT 
    generate_series(1, 100, 3) AS num,
    row_number() OVER (ORDER BY generate_series(1, 100, 3)) AS rank
)
SELECT 
  num, 
  rank
FROM 
  numbered_series
WHERE 
  num = 56;
