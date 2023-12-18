
-- а) Для Боинга 767-300
SELECT s.aircraft_code, a.model, s.seat_no, s.fare_conditions
FROM seats s
JOIN aircrafts a ON s.aircraft_code = a.aircraft_code
WHERE a.model = 'Boeing 767-300';

-- б) Для Аэробуса A319-100
SELECT s.aircraft_code, a.model, s.seat_no, s.fare_conditions
FROM seats s
JOIN aircrafts a ON s.aircraft_code = a.aircraft_code
WHERE a.model = 'Airbus A319-100';
