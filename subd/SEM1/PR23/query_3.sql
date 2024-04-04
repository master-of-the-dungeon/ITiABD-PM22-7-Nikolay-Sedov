
SELECT EXTRACT(MONTH FROM book_date) AS month, SUM(total_amount) AS total_amount
FROM bookings
GROUP BY month
ORDER BY month;
