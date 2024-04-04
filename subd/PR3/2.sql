WITH flight_passengers AS (
  SELECT
    f.flight_id,
    f.scheduled_departure::date AS flight_date,
    a.model,
    COUNT(t.ticket_no) AS passengers
  FROM
    flights f
    JOIN aircrafts_data a ON f.aircraft_code = a.aircraft_code
    JOIN ticket_flights tf ON f.flight_id = tf.flight_id
    JOIN tickets t ON tf.ticket_no = t.ticket_no
  GROUP BY
    f.flight_id, a.model
),
daily_model_passengers AS (
  SELECT
    flight_date,
    model,
    SUM(passengers) OVER (PARTITION BY model, flight_date ORDER BY flight_date) AS daily_passengers
  FROM
    flight_passengers
)
SELECT
  flight_date,
  model,
  daily_passengers
FROM
  daily_model_passengers
ORDER BY
  flight_date, model;
