WITH daily_flights AS (
  SELECT
    f.scheduled_departure::date AS flight_date,
    a.model,
    COUNT(*) AS daily_flights
  FROM
    flights f
    JOIN aircrafts_data a ON f.aircraft_code = a.aircraft_code
  GROUP BY
    flight_date, a.model
),
cumulative_flights AS (
  SELECT
    flight_date,
    model,
    daily_flights,
    SUM(daily_flights) OVER (PARTITION BY model ORDER BY flight_date) AS cumulative_flights
  FROM
    daily_flights
),
rolling_average AS (
  SELECT
    flight_date,
    model,
    daily_flights,
    cumulative_flights,
    AVG(daily_flights) OVER (PARTITION BY model ORDER BY flight_date ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS rolling_avg_flights
  FROM
    cumulative_flights
),
total_flights AS (
  SELECT
    model,
    SUM(daily_flights) AS total_flights_period
  FROM
    daily_flights
  GROUP BY
    model
),
final_output AS (
  SELECT
    r.flight_date,
    r.model,
    r.daily_flights,
    r.cumulative_flights,
    r.rolling_avg_flights,
    r.daily_flights::decimal / tf.total_flights_period AS relative_flights
  FROM
    rolling_average r
    JOIN total_flights tf USING (model)
)
SELECT
  *
FROM
  final_output
ORDER BY
  model, flight_date;
