WITH daily_flights AS (
  SELECT
    f.scheduled_departure::date AS flight_date,
    ad.model,
    COUNT(*) AS daily_flights
  FROM
    flights f
    JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
  GROUP BY
    flight_date, ad.model
)
SELECT
  flight_date,
  model,
  daily_flights,
  AVG(daily_flights) OVER (
    PARTITION BY model
    ORDER BY flight_date
    ROWS BETWEEN 3 PRECEDING AND 1 FOLLOWING
  ) AS rolling_avg_flights
FROM
  daily_flights
ORDER BY
  model, flight_date;
