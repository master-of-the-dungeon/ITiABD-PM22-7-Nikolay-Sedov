CREATE TABLE aircrafts_tmp AS TABLE aircrafts;
CREATE TABLE aircraft_log AS TABLE aircrafts WITH NO DATA;


-------------------2-------------------

CREATE OR REPLACE FUNCTION log_new_aircraft()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO aircraft_log SELECT NEW.*;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_insert_aircraft
AFTER INSERT ON aircrafts_tmp
FOR EACH ROW
EXECUTE FUNCTION log_new_aircraft();


-------------------3-------------------

CREATE TABLE flights_tmp AS TABLE flights;
CREATE TABLE aircrafts_tmp AS TABLE aircrafts;
CREATE TABLE seats_tmp AS TABLE seats;


CREATE OR REPLACE FUNCTION before_delete_aircraft()
RETURNS TRIGGER AS $$
BEGIN
  DELETE FROM flights_tmp WHERE aircraft_id = OLD.aircraft_id;
  DELETE FROM seats_tmp WHERE aircraft_id = OLD.aircraft_id;
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER before_delete_aircraft_trigger
BEFORE DELETE ON aircrafts_tmp
FOR EACH ROW
EXECUTE FUNCTION before_delete_aircraft();



---------------4-------------------------



CREATE OR REPLACE FUNCTION update_total_amount()
RETURNS TRIGGER AS $$
BEGIN

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_total_amount_after_insert_or_update
AFTER INSERT OR UPDATE ON ticket_flights
FOR EACH ROW
EXECUTE FUNCTION update_total_amount();



