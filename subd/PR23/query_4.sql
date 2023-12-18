
SELECT ac.aircraft_code, ac.model, COUNT(DISTINCT s.fare_conditions) AS number_of_fare_conditions
FROM aircrafts ac
JOIN seats s ON ac.aircraft_code = s.aircraft_code
GROUP BY ac.aircraft_code, ac.model
ORDER BY ac.model ASC, ac.aircraft_code DESC;
