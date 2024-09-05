SELECT MAX(amount) FROM ticket_flights;


SELECT amount FROM ticket_flights ORDER BY amount DESC LIMIT 1;


EXPLAIN ANALYZE SELECT MAX(amount) FROM ticket_flights;


EXPLAIN ANALYZE SELECT amount FROM ticket_flights ORDER BY amount DESC LIMIT 1;


CREATE INDEX idx_ticket_flights_amount ON ticket_flights(amount);


EXPLAIN ANALYZE SELECT MAX(amount) FROM ticket_flights;


EXPLAIN ANALYZE SELECT amount FROM ticket_flights ORDER BY amount DESC LIMIT 1;


