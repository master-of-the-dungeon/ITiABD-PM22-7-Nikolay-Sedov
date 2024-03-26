CREATE OR REPLACE FUNCTION update_amount(new_amount NUMERIC)
RETURNS VOID AS $$
BEGIN
    UPDATE ticket_flights_copy
    SET amount = new_amount;
END;
$$ LANGUAGE plpgsql;


SELECT update_amount(100.00);

--------------------------------------------------------------------------------------


CREATE OR REPLACE FUNCTION reduce_total_amount(booking_record bookings)
RETURNS NUMERIC AS $$
BEGIN
    -- Возвращаем total_amount, уменьшенный на 30%
    RETURN booking_record.total_amount * 0.7;
END;
$$ LANGUAGE plpgsql;


SELECT reduce_total_amount((SELECT * FROM bookings WHERE id = 1));

-----------------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION get_passenger_details(ticket_number TEXT, OUT passenger_id INT, OUT passenger_name TEXT, OUT contact_data TEXT)
RETURNS record AS $$
BEGIN
    SELECT p.id, p.first_name || ' ' || p.last_name, p.contact_data
    INTO passenger_id, passenger_name, contact_data
    FROM passengers p
    JOIN tickets t ON p.id = t.passenger_id
    WHERE t.ticket_number = ticket_number;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_passenger_details('ABC123');

----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION sum_variadic(VARIADIC args NUMERIC[])
RETURNS NUMERIC AS $$
SELECT SUM(val) FROM unnest(args) AS val;
$$ LANGUAGE sql;


SELECT sum_variadic(1, 2, 3, 4, 5);


--------------------------------------------------------------------

CREATE OR REPLACE FUNCTION generate_comfort_seats_table()
RETURNS VOID AS $$
BEGIN
    -- Проверяем, существует ли уже таблица. Если да, то удаляем её.
    DROP TABLE IF EXISTS comfort_seats;
    
    -- Создаём новую таблицу на основе условия
    CREATE TABLE comfort_seats AS
    SELECT *
    FROM seats
    WHERE fare_conditions = 'Comfort';
END;
$$ LANGUAGE plpgsql;

SELECT generate_comfort_seats_table();


----------------------------------------------------------------


CREATE OR REPLACE FUNCTION get_business_seats()
RETURNS SETOF seats AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM seats WHERE fare_conditions = 'Business';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_business_seats_record()
RETURNS SETOF record AS $$
BEGIN
    RETURN QUERY
    SELECT id, seat_no, fare_conditions FROM seats WHERE fare_conditions = 'Business';
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_business_seats_record() AS (id INT, seat_no TEXT, fare_conditions TEXT);


-----------------------------------------------------------------------------------------------