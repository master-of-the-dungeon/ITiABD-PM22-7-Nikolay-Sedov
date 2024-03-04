SELECT
  ad.model,
  EXTRACT(MONTH FROM f.scheduled_departure) AS month,
  EXTRACT(DAY FROM f.scheduled_departure) AS day,
  SUM(tf.amount) AS total_sales
FROM
  ticket_flights tf
  JOIN flights f ON tf.flight_id = f.flight_id
  JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
GROUP BY
  ROLLUP (ad.model, EXTRACT(MONTH FROM f.scheduled_departure), EXTRACT(DAY FROM f.scheduled_departure))
ORDER BY
  ad.model, month, day;




SELECT
  ad.model,
  EXTRACT(MONTH FROM f.scheduled_departure) AS month,
  EXTRACT(DAY FROM f.scheduled_departure) AS day,
  SUM(tf.amount) AS total_sales
FROM
  ticket_flights tf
  JOIN flights f ON tf.flight_id = f.flight_id
  JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
GROUP BY
  CUBE (ad.model, EXTRACT(MONTH FROM f.scheduled_departure), EXTRACT(DAY FROM f.scheduled_departure))
ORDER BY
  ad.model, month, day;





SELECT
  ad.model,
  EXTRACT(MONTH FROM f.scheduled_departure) AS month,
  EXTRACT(DAY FROM f.scheduled_departure) AS day,
  SUM(tf.amount) AS total_sales
FROM
  ticket_flights tf
  JOIN flights f ON tf.flight_id = f.flight_id
  JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
GROUP BY
  CUBE (ad.model, EXTRACT(MONTH FROM f.scheduled_departure), EXTRACT(DAY FROM f.scheduled_departure))
ORDER BY
  ad.model, month, day;







SELECT
  ad.model,
  EXTRACT(MONTH FROM f.scheduled_departure) AS month,
  EXTRACT(DAY FROM f.scheduled_departure) AS day,
  SUM(tf.amount) AS total_sales
FROM
  ticket_flights tf
  JOIN flights f ON tf.flight_id = f.flight_id
  JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
GROUP BY
  GROUPING SETS (
    (ad.model, EXTRACT(MONTH FROM f.scheduled_departure), EXTRACT(DAY FROM f.scheduled_departure)),
    (ad.model, EXTRACT(MONTH FROM f.scheduled_departure)),
    (ad.model),
    ()
  )
ORDER BY
  ad.model, month, day;
