WITH model_flights AS (
  SELECT
    a.model,
    COUNT(f.flight_id) AS flights_count
  FROM
    aircrafts_data a
    JOIN flights f ON a.aircraft_code = f.aircraft_code
  GROUP BY
    a.model
)
SELECT
  model,
  flights_count,
  RANK() OVER (
    ORDER BY flights_count DESC
  ) AS rank
FROM
  model_flights
ORDER BY
  rank;
