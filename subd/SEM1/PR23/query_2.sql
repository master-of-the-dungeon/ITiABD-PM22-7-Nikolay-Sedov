
SELECT book_date, COUNT(*) AS number_of_bookings
FROM bookings
WHERE EXTRACT(MONTH FROM book_date) = 8 AND EXTRACT(YEAR FROM book_date) = 2023
GROUP BY book_date
ORDER BY book_date DESC;
