SELECT
    a.airport_code,
    a.airport_name,
    a.city,
    a.coordinates,
    a.timezone,
    ABS(a.coordinates[1] - southern_airport.coordinates[1]) AS latitude_difference
FROM
    airports a
JOIN LATERAL (
    SELECT
        airport_code,
        coordinates
    FROM
        airports
    WHERE
        timezone = a.timezone
    ORDER BY
        coordinates[1] ASC
    LIMIT 1
) AS southern_airport ON true;
