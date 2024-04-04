INSERT INTO flights (flight_id, flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code, actual_departure, actual_arrival)
SELECT 
    (SELECT MAX(flight_id) + ROW_NUMBER() OVER (), 
    'FL' || ROW_NUMBER() OVER () AS flight_no,
    CURRENT_TIMESTAMP + INTERVAL '1 day' * (ROW_NUMBER() OVER () % 7) AS scheduled_departure,
    CURRENT_TIMESTAMP + INTERVAL '2 day' * (ROW_NUMBER() OVER () % 7) AS scheduled_arrival,
    'DEP' || (ROW_NUMBER() OVER () % 10) AS departure_airport,
    'ARR' || (ROW_NUMBER() OVER () % 10) AS arrival_airport,
    'Scheduled' AS status,
    'AC' || (ROW_NUMBER() OVER () % 5) AS aircraft_code,
    CURRENT_TIMESTAMP + INTERVAL '1 day' * (ROW_NUMBER() OVER () % 7) AS actual_departure,
    CURRENT_TIMESTAMP + INTERVAL '2 day' * (ROW_NUMBER() OVER () % 7) AS actual_arrival
FROM 
    generate_series(1, 100) AS g;
