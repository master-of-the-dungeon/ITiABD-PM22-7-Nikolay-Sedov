SELECT r.departure_airport, r.arrival_airport
FROM routes r
WHERE NOT EXISTS (
  SELECT 1
  FROM ticket_flights tf
  JOIN flights f ON tf.flight_id = f.flight_id
  WHERE f.departure_airport = r.departure_airport AND f.arrival_airport = r.arrival_airport
);


--------------------2-----------------------

SELECT COUNT(*)
FROM bookings
WHERE total_amount > (
  SELECT MAX(total_amount) / 3
  FROM bookings
);



----------------------3----------------



SELECT aircraft_code,
       (SELECT COUNT(*) FROM seats WHERE fare_conditions = 'Business' AND seats.aircraft_code = ac.aircraft_code) AS business_class_seats,
       (SELECT COUNT(*) FROM seats WHERE fare_conditions = 'Comfort' AND seats.aircraft_code = ac.aircraft_code) AS comfort_class_seats,
       (SELECT COUNT(*) FROM seats WHERE fare_conditions = 'Economy' AND seats.aircraft_code = ac.aircraft_code) AS economy_class_seats
FROM aircrafts_data ac;



------------------4--------------------


SELECT city, airport_code, airport_name
FROM airports
WHERE city IN (
  SELECT city
  FROM airports
  GROUP BY city
  HAVING COUNT(airport_code) > 2
);



----------------5-----------------------

SELECT flight_no
FROM flights f
WHERE EXISTS (
  SELECT 1
  FROM boarding_passes bp
  WHERE bp.flight_id = f.flight_id
);



SELECT model
FROM aircrafts_data
WHERE aircraft_code IN (
  SELECT DISTINCT aircraft_code
  FROM flights
  WHERE scheduled_departure >= '2023-01-01'
);


------------6------------------------


SELECT f.flight_id, f.flight_no, f.scheduled_departure, f.scheduled_arrival, f.actual_departure, f.actual_arrival, f.status,
       dep.airport_name AS departure_airport_name, arr.airport_name AS arrival_airport_name
FROM flights f
JOIN airports dep ON f.departure_airport = dep.airport_code
JOIN airports arr ON f.arrival_airport = arr.airport_code
WHERE EXTRACT(MONTH FROM f.scheduled_departure) = 8 AND EXTRACT(DAY FROM f.scheduled_departure) = 26
AND f.arrival_airport <> 'VKO';


---------------------7-------------------
SELECT ad.model, COUNT(f.flight_id) AS flights_count, 'August 26' AS flight_date
FROM flights f
JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
WHERE EXTRACT(MONTH FROM f.scheduled_departure) = 8 AND EXTRACT(DAY FROM f.scheduled_departure) = 26
GROUP BY ad.model
UNION
SELECT ad.model, COUNT(f.flight_id) AS flights_count, 'August 28' AS flight_date
FROM flights f
JOIN aircrafts_data ad ON f.aircraft_code = ad.aircraft_code
WHERE EXTRACT(MONTH FROM f.scheduled_departure) = 8 AND EXTRACT(DAY FROM f.scheduled_departure) = 28
GROUP BY ad.model;


--------------8--------------------

SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Москва', 'Санкт-Петербург', 'Казань')
INTERSECT
SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Москва')
INTERSECT
SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Санкт-Петербург')
INTERSECT
SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Казань');



SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Москва', 'Санкт-Петербург')
EXCEPT
SELECT DISTINCT arrival_city
FROM routes
WHERE departure_city IN ('Казань');


    (SELECT DISTINCT arrival_city FROM routes WHERE departure_city = 'Москва')
UNION
(SELECT DISTINCT r.arrival_city FROM routes r WHERE NOT EXISTS (
  SELECT 1 FROM routes r2 WHERE r2.departure_city = 'Санкт-Петербург' AND r2.arrival_city = r.arrival_city
));


-----------------------9-------------------------------


SELECT airport_code, airport_name FROM airports WHERE city = 'Москва'
UNION
SELECT airport_code, airport_name FROM airports WHERE city = 'Санкт-Петербург';



SELECT flight_no FROM flights WHERE departure_airport = 'DME'
INTERSECT
SELECT flight_no FROM flights WHERE arrival_airport = 'LED';


SELECT city
FROM airports
EXCEPT
SELECT city
FROM airports
WHERE airport_code = 'DME';
