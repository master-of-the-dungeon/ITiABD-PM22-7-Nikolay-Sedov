
-- а) С использованием JOIN
SELECT s.aircraft_code, a.model, s.seat_no, s.fare_conditions
FROM seats s
JOIN aircrafts a ON s.aircraft_code = a.aircraft_code
WHERE a.model LIKE 'Bo%';

-- б) Без использования JOIN
SELECT s.aircraft_code, s.seat_no, s.fare_conditions
FROM seats s
WHERE EXISTS (
    SELECT 1
    FROM aircrafts a
    WHERE s.aircraft_code = a.aircraft_code AND a.model LIKE 'Bo%'
);
