SELECT
  departure_airport,
  arrival_airport,
  status,
  scheduled_departure::date AS departure_date,
  COUNT(*) AS flights_count
FROM
  flights
GROUP BY
  ROLLUP (departure_airport, arrival_airport, status, scheduled_departure::date)
ORDER BY
  departure_airport, arrival_airport, status, departure_date;


SELECT
  departure_airport,
  arrival_airport,
  status,
  scheduled_departure::date AS departure_date,
  COUNT(*) AS flights_count
FROM
  flights
GROUP BY
  CUBE (departure_airport, arrival_airport, status, scheduled_departure::date)
ORDER BY
  departure_airport, arrival_airport, status, departure_date;



SELECT
  departure_airport,
  arrival_airport,
  status,
  scheduled_departure::date AS departure_date,
  COUNT(*) AS flights_count
FROM
  flights
GROUP BY
  GROUPING SETS (
    (departure_airport, arrival_airport, status, scheduled_departure::date),
    (departure_airport, arrival_airport, status),
    (departure_airport, arrival_airport),
    (departure_airport),
    ()
  )
ORDER BY
  departure_airport, arrival_airport, status, departure_date;



