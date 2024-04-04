
SELECT dep.airport_name AS departure_airport, arr.airport_name AS arrival_airport, COUNT(f.status) AS number_of_flight_statuses
FROM flights f
JOIN airports dep ON f.departure_airport = dep.airport_code
JOIN airports arr ON f.arrival_airport = arr.airport_code
GROUP BY dep.airport_name, arr.airport_name
ORDER BY dep.airport_name ASC, arr.airport_name ASC;
