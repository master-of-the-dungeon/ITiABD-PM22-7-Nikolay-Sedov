WITH ticket_counts AS (
    SELECT
        flight_id,
        amount
    FROM
        ticket_flights
)
SELECT
    percentile,
    MIN(amount) AS min_amount,
    MAX(amount) AS max_amount,
    COUNT(flight_id) AS number_of_flights
FROM (
    SELECT
        amount,
        NTILE(100) OVER (ORDER BY amount) AS percentile
    FROM
        ticket_counts
) AS ticket_percentiles
WHERE
    percentile IN (10, 25, 50, 95)
GROUP BY
    percentile;
