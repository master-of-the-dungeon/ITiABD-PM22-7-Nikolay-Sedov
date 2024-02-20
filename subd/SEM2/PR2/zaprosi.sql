SET search_path TO bookings;

WITH RelevantFlights AS (
    SELECT 
        f.flight_id,
        f.scheduled_departure
    FROM flights f
    WHERE f.scheduled_departure > '2017-07-28'::date
),
MaxPrice AS (
    SELECT 
        tf.flight_id,
        tf.ticket_no,
        MAX(tf.amount) AS max_price
    FROM ticket_flights tf
    JOIN RelevantFlights rf ON tf.flight_id = rf.flight_id
    WHERE tf.fare_conditions = 'Business'
    GROUP BY tf.flight_id, tf.ticket_no
),
MaxPricePerFlight AS (
    SELECT
        mp.flight_id,
        MAX(mp.max_price) AS max_price
    FROM MaxPrice mp
    GROUP BY mp.flight_id
),
Passengers AS (
    SELECT
        t.passenger_name,
        tf.flight_id,
        tf.amount,
        tf.fare_conditions
    FROM ticket_flights tf
    JOIN tickets t ON tf.ticket_no = t.ticket_no
    JOIN MaxPricePerFlight mpf ON tf.flight_id = mpf.flight_id AND tf.amount = mpf.max_price
    WHERE tf.fare_conditions = 'Business'
)
SELECT 
    p.*
FROM Passengers p;



---------------------------------------------------------------------


SET search_path TO bookings;

WITH CityAirports AS (
    SELECT 
        ad.airport_code
    FROM airports_data ad
    WHERE ad.city ->> 'name' LIKE 'М%' -- Предполагаем, что имя города хранится в JSONB в поле 'name'
),
AugustFlights AS (
    SELECT 
        f.flight_id,
        f.departure_airport,
        f.arrival_airport
    FROM flights f
    JOIN CityAirports ca ON f.departure_airport = ca.airport_code
    WHERE f.scheduled_departure >= '2023-08-01'::date
    AND f.scheduled_departure < '2023-09-01'::date
),
PassengerFlights AS (
    SELECT 
        t.passenger_id,
        COUNT(DISTINCT tf.flight_id) AS flights_count
    FROM ticket_flights tf
    JOIN tickets t ON tf.ticket_no = t.ticket_no
    JOIN AugustFlights af ON tf.flight_id = af.flight_id
    GROUP BY t.passenger_id
),
MinFlights AS (
    SELECT 
        MIN(flights_count) AS min_flights
    FROM PassengerFlights
),
PassengersWithMinFlights AS (
    SELECT 
        pf.passenger_id,
        pf.flights_count
    FROM PassengerFlights pf
    JOIN MinFlights mf ON pf.flights_count = mf.min_flights
)
SELECT 
    COUNT(*) AS passengers_count,
    flights_count
FROM PassengersWithMinFlights
GROUP BY flights_count;


------------------------------------------------------------------------

CREATE TABLE flights_copy AS SELECT * FROM flights;

CREATE TABLE flights_log (
    flight_id INTEGER,
    departure_airport_code CHAR(3),
    departure_city TEXT,
    scheduled_departure TIMESTAMP WITH TIME ZONE,
    scheduled_arrival TIMESTAMP WITH TIME ZONE
);

WITH MovedFlights AS (
    DELETE FROM flights_copy f
    USING airports_data a
    WHERE f.departure_airport = a.airport_code
    AND a.city ->> 'name' IN ('Воронеж', 'Москва', 'Самара')
    AND f.scheduled_departure BETWEEN '2017-07-29' AND '2017-08-12'
    RETURNING f.flight_id, f.departure_airport AS departure_airport_code, 
              a.city ->> 'name' AS departure_city, f.scheduled_departure, f.scheduled_arrival
)
INSERT INTO flights_log (flight_id, departure_airport_code, departure_city, scheduled_departure, scheduled_arrival)
SELECT flight_id, departure_airport_code, departure_city, scheduled_departure, scheduled_arrival
FROM MovedFlights;


---------------------------------------------------------------------------------


WITH RECURSIVE SumSeries AS (
    SELECT 
        1 AS n, -- Начальное значение n
        1 * (1 + 1) AS term_value -- Вычисление первого слагаемого
    UNION ALL
    SELECT 
        n + 1, -- Увеличение n на 1 на каждом шаге рекурсии
        (n + 1) * ((n + 1) + 1) -- Вычисление текущего слагаемого
    FROM SumSeries
    WHERE n < 6 -- Ограничение количества шагов рекурсии до 6
)
SELECT SUM(term_value) AS total_sum
FROM SumSeries;


---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    parent_id INT NULL REFERENCES comments(id),
    comment_text TEXT
);

INSERT INTO comments (parent_id, comment_text) VALUES
(NULL, 'Root Comment 1'),
(NULL, 'Root Comment 2');

-- Добавляем потомков для "Root Comment 1"
INSERT INTO comments (parent_id, comment_text) VALUES
(1, 'Child 1 of Comment 1'),
(1, 'Child 2 of Comment 1'),
(1, 'Child 3 of Comment 1'),
(1, 'Child 4 of Comment 1'),
(1, 'Child 5 of Comment 1');

-- Добавляем потомков для "Root Comment 2"
INSERT INTO comments (parent_id, comment_text) VALUES
(2, 'Child 1 of Comment 2'),
(2, 'Child 2 of Comment 2'),
(2, 'Child 3 of Comment 2'),
(2, 'Child 4 of Comment 2'),
(2, 'Child 5 of Comment 2');

-- Добавляем потомков для последующих комментариев в соответствии с заданием

-- Рекурсивный запрос для обхода в глубину
WITH RECURSIVE depth_first AS (
    SELECT id, parent_id, comment_text, 1 AS depth
    FROM comments
    WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.parent_id, c.comment_text, df.depth + 1
    FROM comments c
    JOIN depth_first df ON c.parent_id = df.id
)
SELECT * FROM depth_first ORDER BY depth, id;

-- Рекурсивный запрос для обхода в ширину
WITH RECURSIVE breadth_first AS (
    SELECT id, parent_id, comment_text, ARRAY[id] AS path
    FROM comments
    WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.parent_id, c.comment_text, bf.path || c.id
    FROM comments c
    JOIN breadth_first bf ON c.parent_id = bf.id
)
SELECT * FROM breadth_first ORDER BY path;


--------------------------------------------------------------------------------------

CREATE VIEW aircraft_seats_count AS
SELECT
    a.model,
    COUNT(CASE WHEN s.fare_conditions = 'Business' THEN 1 END) AS business_class_seats,
    COUNT(CASE WHEN s.fare_conditions = 'Economy' THEN 1 END) AS economy_class_seats
FROM
    seats s
JOIN
    aircrafts a ON s.aircraft_code = a.aircraft_code
GROUP BY
    a.model;


------------------------------------------------------------------------

CREATE MATERIALIZED VIEW flights_passengers_2017 AS
SELECT
    f.flight_id,
    f.flight_no,
    f.scheduled_departure,
    f.scheduled_arrival,
    f.departure_airport,
    f.arrival_airport,
    t.passenger_name
FROM
    flights f
JOIN
    ticket_flights tf ON f.flight_id = tf.flight_id
JOIN
    tickets t ON tf.ticket_no = t.ticket_no
WHERE
    f.scheduled_departure BETWEEN '2017-01-01' AND '2017-12-31';


------------------------------------------------------------------------

DROP TABLE airports CASCADE;


--------------------------------------------------------------------------


CREATE VIEW tickets_view AS
SELECT ticket_no, book_ref, passenger_id, passenger_name
FROM tickets;



INSERT INTO tickets_view (ticket_no, book_ref, passenger_id, passenger_name)
VALUES ('123456789012', 'ABC123', 'PID12345', 'Иван Иванов');


UPDATE tickets_view
SET passenger_name = 'Петр Петров'
WHERE ticket_no = '123456789012';


DELETE FROM tickets_view
WHERE ticket_no = '123456789012';




-----------------------------------------------------------------------------------------

ALTER VIEW flights_v RENAME TO flights_view;

ALTER VIEW flights_view OWNER TO новый_владелец;

ALTER MATERIALIZED VIEW routes RENAME TO routes_view;

REFRESH MATERIALIZED VIEW routes_view;

ALTER MATERIALIZED VIEW routes_view OWNER TO новый_владелец;

