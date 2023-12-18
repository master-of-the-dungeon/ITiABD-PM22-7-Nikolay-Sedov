
SELECT AVG(total_amount) AS average_booking_amount
FROM bookings
WHERE EXTRACT(MONTH FROM book_date) = 8 AND EXTRACT(YEAR FROM book_date) = 2023;
