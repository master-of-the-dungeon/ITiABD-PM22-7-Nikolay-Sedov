WITH daily_sales AS (
  SELECT
    b.book_date::date AS sale_date,
    SUM(b.total_amount) AS daily_total
  FROM
    bookings b
  JOIN tickets t ON b.book_ref = t.book_ref
  GROUP BY
    b.book_date::date
),
cumulative_sales AS (
  SELECT
    sale_date,
    daily_total,
    SUM(daily_total) OVER (
      PARTITION BY EXTRACT(YEAR FROM sale_date), EXTRACT(MONTH FROM sale_date)
      ORDER BY sale_date
      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_total
  FROM
    daily_sales
)
SELECT
  sale_date,
  daily_total,
  cumulative_total
FROM
  cumulative_sales
ORDER BY
  sale_date;
