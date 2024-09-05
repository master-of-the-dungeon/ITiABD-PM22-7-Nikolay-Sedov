WITH ticket_cte AS MATERIALIZED (
    SELECT * FROM ticket_flights WHERE amount > 7000
)
SELECT SUM(amount) FROM ticket_cte;

EXPLAIN ANALYZE
WITH ticket_cte AS MATERIALIZED (
    SELECT * FROM ticket_flights WHERE amount > 7000
)
SELECT SUM(amount) FROM ticket_cte;


