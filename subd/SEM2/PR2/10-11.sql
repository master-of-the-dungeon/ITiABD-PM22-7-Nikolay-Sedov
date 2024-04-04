CREATE OR REPLACE FUNCTION get_formatted_passenger_info(ticket_number character(13))
RETURNS text AS $$
DECLARE
    -- Объявляем переменные для хранения данных о пассажире и контактной информации
    passenger_name text;
    contact_data jsonb;
    formatted_name text;
    formatted_contact_info text;
BEGIN
    -- Получаем имя пассажира и контактные данные по номеру билета
    SELECT passenger_name, contact_data INTO passenger_name, contact_data
    FROM bookings.tickets
    WHERE ticket_no = ticket_number;
    
    -- Преобразуем каждое слово в формат "Имя Фамилия"
    SELECT array_to_string(ARRAY(SELECT initcap(word) FROM unnest(string_to_array(passenger_name, ' ')) word), ' ')
    INTO formatted_name;
    
    -- Формируем строку контактной информации
    -- Здесь предполагается, что контактные данные хранятся в формате JSONB и содержат ключ "phone"
    formatted_contact_info := ', contact_data: phone: ' || contact_data->>'phone';
    
    -- Возвращаем отформатированную строку
    RETURN formatted_name || formatted_contact_info;
END;
$$ LANGUAGE plpgsql;


-- Замените 'ABC1234567890' на реальный номер билета
SELECT get_formatted_passenger_info('ABC1234567890');

-----------------------------------------------------------------------------------------------


CREATE OR REPLACE FUNCTION get_longest_flight_info(aircraft_code_input character(3))
RETURNS text AS $$
DECLARE
    longest_flight_record record;
BEGIN
    -- Найти самый длительный перелёт для указанного кода самолёта
    SELECT f.flight_no, f.scheduled_departure, f.scheduled_arrival, a.model->>'name' AS model_name
    INTO longest_flight_record
    FROM bookings.flights AS f
    JOIN bookings.aircrafts_data AS a ON f.aircraft_code = a.aircraft_code
    WHERE f.aircraft_code = aircraft_code_input
    ORDER BY (f.scheduled_arrival - f.scheduled_departure) DESC
    LIMIT 1;

    -- Вернуть отформатированную строку с информацией о самом длительном перелёте
    RETURN aircraft_code_input || ', ' || longest_flight_record.model_name || ', ' || longest_flight_record.scheduled_departure || ', ' ||
           longest_flight_record.scheduled_arrival || ', ' || longest_flight_record.flight_no;
END;
$$ LANGUAGE plpgsql;

SELECT get_longest_flight_info('747'); -- Замените '747' на код интересующего самолёта

------------------------------------------------------------------------------------------------


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

SELECT * FROM get_seats_count_by_aircraft_model('Boeing 747'); 


---------------------------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION get_tickets_sold_for_flight(flight_id_input integer)
RETURNS bigint AS $$
DECLARE
    tickets_sold bigint;
BEGIN
    -- Подсчет количества билетов для заданного рейса
    SELECT COUNT(*) INTO tickets_sold
    FROM bookings.ticket_flights
    WHERE flight_id = flight_id_input;

    RETURN tickets_sold;
END;
$$ LANGUAGE plpgsql;


SELECT get_tickets_sold_for_flight(123);



----------------------------------------------------------------------------------------

