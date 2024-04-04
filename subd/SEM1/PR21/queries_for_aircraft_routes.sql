
-- а) Для всех самолетов
SELECT ac.aircraft_code, ac.model, r.departure_airport_name, r.arrival_airport_name
FROM aircrafts ac
JOIN routes r ON ac.aircraft_code = r.aircraft_code;

-- б) Только для самолетов, обслуживающих маршруты
SELECT DISTINCT ac.aircraft_code, ac.model, r.departure_airport_name, r.arrival_airport_name
FROM aircrafts ac
JOIN routes r ON ac.aircraft_code = r.aircraft_code
WHERE r.aircraft_code IS NOT NULL;
