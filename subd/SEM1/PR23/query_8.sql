
SELECT f.flight_id, f.flight_no, MAX(tf.amount) AS max_price
FROM ticket_flights tf
JOIN flights f ON tf.flight_id = f.flight_id
GROUP BY f.flight_id, f.flight_no;
