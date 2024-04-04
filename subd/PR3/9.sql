SELECT
  EXTRACT(DOW FROM scheduled_departure) AS day_of_week,
  departure_airport,
  COUNT(*) AS flights_count
FROM
  flights
GROUP BY
  EXTRACT(DOW FROM scheduled_departure),
  departure_airport
ORDER BY
  EXTRACT(DOW FROM scheduled_departure),
  departure_airport;
