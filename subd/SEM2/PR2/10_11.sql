CREATE OR REPLACE FUNCTION get_formatted_passenger_info(ticket_number character(13))
RETURNS text AS $$
DECLARE
    passenger_name text;
    contact_data jsonb;
    formatted_name text;
    formatted_contact_info text;
BEGIN
    SELECT passenger_name, contact_data INTO passenger_name, contact_data
    FROM bookings.tickets
    WHERE ticket_no = ticket_number;
    
    SELECT array_to_string(ARRAY(SELECT initcap(word) FROM unnest(string_to_array(passenger_name, ' ')) word), ' ')
    INTO formatted_name;
    
    formatted_contact_info := ', contact_data: phone: ' || contact_data->>'phone';
    
    RETURN formatted_name || formatted_contact_info;
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT get_formatted_passenger_info('ABC1234567890');


CREATE OR REPLACE FUNCTION get_longest_flight_info(aircraft_code_input character(3))
RETURNS text AS $$
DECLARE
    longest_flight_record record;
BEGIN
    SELECT f.flight_no, f.scheduled_departure, f.scheduled_arrival, a.model->>'name' AS model_name
    INTO longest_flight_record
    FROM bookings.flights AS f
    JOIN bookings.aircrafts_data AS a ON f.aircraft_code = a.aircraft_code
    WHERE f.aircraft_code = aircraft_code_input
    ORDER BY (f.scheduled_arrival - f.scheduled_departure) DESC
    LIMIT 1;

    RETURN aircraft_code_input || ', ' || longest_flight_record.model_name || ', ' || longest_flight_record.scheduled_departure || ', ' ||
           longest_flight_record.scheduled_arrival || ', ' || longest_flight_record.flight_no;
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT get_longest_flight_info('747');


CREATE OR REPLACE FUNCTION get_seats_count_by_aircraft_model(aircraft_model text)
RETURNS TABLE(economy_count bigint, business_count bigint, comfort_count bigint) AS $$
BEGIN
    RETURN QUERY
    SELECT
        COUNT(*) FILTER (WHERE s.fare_conditions = 'Economy') AS economy_count,
        COUNT(*) FILTER (WHERE s.fare_conditions = 'Business') AS business_count,
        COUNT(*) FILTER (WHERE s.fare_conditions = 'Comfort') AS comfort_count
    FROM
        bookings.seats s
    JOIN
        bookings.aircrafts_data a ON s.aircraft_code = a.aircraft_code
    WHERE
        a.model ->> 'name' = aircraft_model;
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT * FROM get_seats_count_by_aircraft_model('Boeing 747');



CREATE OR REPLACE FUNCTION get_tickets_sold_for_flight(flight_id_input integer)
RETURNS bigint AS $$
DECLARE
    tickets_sold bigint;
BEGIN
    SELECT COUNT(*) INTO tickets_sold
    FROM bookings.ticket_flights
    WHERE flight_id = flight_id_input;

    RETURN tickets_sold;
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT get_tickets_sold_for_flight(123);


CREATE OR REPLACE FUNCTION update_amount(new_amount numeric)
RETURNS void AS $$
BEGIN
    UPDATE bookings.ticket_flights_copy
    SET amount = new_amount;
END;
$$ LANGUAGE plpgsql;

-- Для выполнения:
-- SELECT update_amount(100.00);


CREATE OR REPLACE FUNCTION reduce_total_amount(booking_row bookings.bookings%ROWTYPE)
RETURNS numeric AS $$
BEGIN
    RETURN booking_row.total_amount * 0.7;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION sum_variadic(VARIADIC args numeric[])
RETURNS numeric AS $$
DECLARE
    total_sum numeric := 0;
BEGIN
    FOREACH i IN ARRAY args LOOP
        total_sum := total_sum + i;
    END LOOP;
    RETURN total_sum;
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT sum_variadic(10, 20, 30);


CREATE OR REPLACE FUNCTION create_comfort_seats_table()
RETURNS void AS $$
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS comfort_seats AS
    SELECT *
    FROM bookings.seats
    WHERE fare_conditions = 'Comfort';
END;
$$ LANGUAGE plpgsql;

-- Для выполнения:
-- SELECT create_comfort_seats_table();


CREATE OR REPLACE FUNCTION get_business_seats()
RETURNS SETOF bookings.seats AS $$
BEGIN
    RETURN QUERY SELECT * FROM bookings.seats WHERE fare_conditions = 'Business';
END;
$$ LANGUAGE plpgsql;

-- Для вывода:
-- SELECT * FROM get_business_seats();



