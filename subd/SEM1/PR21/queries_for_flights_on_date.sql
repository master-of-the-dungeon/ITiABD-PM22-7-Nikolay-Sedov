
-- а) Только с действительными датами отправления и прибытия
SELECT f.flight_id, f.flight_no, f.scheduled_departure, f.scheduled_arrival, 
       f.actual_departure, f.actual_arrival, f.status,
       dep.airport_name AS departure_airport, arr.airport_name AS arrival_airport
FROM flights f
JOIN airports dep ON f.departure_airport = dep.airport_code
JOIN airports arr ON f.arrival_airport = arr.airport_code
WHERE f.scheduled_departure::DATE = '2022-08-26' AND f.actual_departure IS NOT NULL AND f.actual_arrival IS NOT NULL;

-- б) Включая строки без дат отправления и прибытия
SELECT f.flight_id, f.flight_no, f.scheduled_departure, f.scheduled_arrival, 
       f.actual_departure, f.actual_arrival, f.status,
       dep.airport_name AS departure_airport, arr.airport_name AS arrival_airport
FROM flights f
JOIN airports dep ON f.departure_airport = dep.airport_code
JOIN airports arr ON f.arrival_airport = arr.airport_code
WHERE f.scheduled_departure::DATE = '2022-08-26';
