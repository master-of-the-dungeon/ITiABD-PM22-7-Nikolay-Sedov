
SELECT f.flight_id, f.flight_no, MIN(tf.amount) AS min_price
FROM ticket_flights tf
JOIN flights f ON tf.flight_id = f.flight_id
GROUP BY f.flight_id, f.flight_no;
