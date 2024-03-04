SELECT
    f.flight_id,
    f.flight_no,
    f.scheduled_departure,
    f.scheduled_arrival,
    dep.airport_name AS departure_airport_name,
    arr.airport_name AS arrival_airport_name
FROM
    flights f
LEFT JOIN LATERAL (
    SELECT airport_name
    FROM airports
    WHERE airport_code = f.departure_airport
) dep ON true
LEFT JOIN LATERAL (
    SELECT airport_name
    FROM airports
    WHERE airport_code = f.arrival_airport
) arr ON true;
