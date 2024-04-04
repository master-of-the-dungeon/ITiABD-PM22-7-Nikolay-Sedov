
SELECT ac.model, COUNT(*) AS number_of_flights
FROM flights f
JOIN aircrafts ac ON f.aircraft_code = ac.aircraft_code
WHERE f.scheduled_departure::DATE = '2023-08-26'
GROUP BY ac.model;
