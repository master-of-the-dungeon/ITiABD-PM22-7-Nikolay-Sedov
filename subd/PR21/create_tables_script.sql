-- Создание таблицы 'airports'
CREATE TABLE airports (
    airport_code CHAR(3) PRIMARY KEY,
    airport_name VARCHAR(100) NOT NULL
);

-- Создание таблицы 'aircrafts'
CREATE TABLE aircrafts (
    aircraft_code CHAR(3) PRIMARY KEY,
    model VARCHAR(100),
    range INT NOT NULL
);

-- Создание таблицы 'flights'
CREATE TABLE flights (
    flight_id SERIAL PRIMARY KEY,
    flight_no CHAR(6),
    scheduled_departure TIMESTAMP NOT NULL,
    scheduled_arrival TIMESTAMP NOT NULL,
    departure_airport CHAR(3) REFERENCES airports(airport_code),
    arrival_airport CHAR(3) REFERENCES airports(airport_code),
    aircraft_code CHAR(3) REFERENCES aircrafts(aircraft_code),
    status VARCHAR(20),
    actual_departure TIMESTAMP,
    actual_arrival TIMESTAMP
);

-- Создание таблицы 'bookings'
CREATE TABLE bookings (
    book_ref CHAR(6) PRIMARY KEY,
    book_date TIMESTAMP NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы 'tickets'
CREATE TABLE tickets (
    ticket_no CHAR(13) PRIMARY KEY,
    book_ref CHAR(6) REFERENCES bookings(book_ref),
    passenger_id CHAR(20) NOT NULL,
    passenger_name VARCHAR(100) NOT NULL
);

-- Создание таблицы 'ticket_flights'
CREATE TABLE ticket_flights (
    ticket_no CHAR(13) REFERENCES tickets(ticket_no),
    flight_id INT REFERENCES flights(flight_id),
    fare_conditions VARCHAR(10),
    amount DECIMAL(10, 2) NOT NULL
);

-- Создание таблицы 'seats'
CREATE TABLE seats (
    aircraft_code CHAR(3) REFERENCES aircrafts(aircraft_code),
    seat_no VARCHAR(4),
    fare_conditions VARCHAR(10),
    PRIMARY KEY (aircraft_code, seat_no)
);

-- Создание таблицы 'boarding_passes'
CREATE TABLE boarding_passes (
    ticket_no CHAR(13) REFERENCES tickets(ticket_no),
    flight_id INT REFERENCES flights(flight_id),
    boarding_no INT NOT NULL,
    seat_no VARCHAR(4) NOT NULL,
    PRIMARY KEY (ticket_no, flight_id)
);

-- Добавление данных в таблицу 'airports'
INSERT INTO airports (airport_code, airport_name) VALUES
('JFK', 'John F. Kennedy International Airport'),
('LHR', 'London Heathrow Airport'),
('CDG', 'Charles de Gaulle Airport'),
('DME', 'Domodedovo International Airport');

-- Добавление данных в таблицу 'aircrafts'
INSERT INTO aircrafts (aircraft_code, model, range) VALUES
('B76', 'Boeing 767-300', 9700),
('A31', 'Airbus A319-100', 6700),
('SU9', 'Sukhoi Superjet-100', 3000);

-- Добавление данных в таблицу 'flights'
INSERT INTO flights (flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, aircraft_code, status) VALUES
('AF11', '2023-08-01 08:00:00', '2023-08-01 10:30:00', 'JFK', 'LHR', 'B76', 'Scheduled'),
('BA20', '2023-08-02 09:00:00', '2023-08-02 11:30:00', 'LHR', 'CDG', 'A31', 'Scheduled'),
('SU13', '2023-08-26 10:00:00', '2023-08-26 12:00:00', 'CDG', 'DME', 'SU9', 'Arrived');

-- Добавление данных в таблицу 'bookings'
INSERT INTO bookings (book_ref, book_date, total_amount) VALUES
('ABC12', '2023-08-01 12:00:00', 500.00),
('DEF45', '2023-08-02 13:00:00', 600.00),
('GHI78', '2023-08-03 14:00:00', 450.00);

-- Добавление данных в таблицу 'tickets'
INSERT INTO tickets (ticket_no, book_ref, passenger_id, passenger_name) VALUES
('TKT01', 'ABC12', 'PAX01', 'John Doe'),
('TKT02', 'DEF45', 'PAX02', 'Jane Doe'),
('TKT03', 'GHI78', 'PAX03', 'Alice Johnson');

-- Добавление данных в таблицу 'ticket_flights'
INSERT INTO ticket_flights (ticket_no, flight_id, fare_conditions, amount) VALUES
('TKT01', 1, 'Economy', 250.00),
('TKT02', 2, 'Economy', 350.00),
('TKT03', 3, 'Business', 300.00);

-- Добавление данных в таблицу 'boarding_passes'
INSERT INTO boarding_passes (ticket_no, flight_id, boarding_no, seat_no) VALUES
('TKT01', 1, 1, '12A'),
('TKT02', 2, 2, '14C'),
('TKT03', 3, 3, '2B');

-- Добавление данных в таблицу 'seats'
INSERT INTO seats (aircraft_code, seat_no, fare_conditions) VALUES
('B76', '12A', 'Economy'),
('A31', '14C', 'Economy'),
('SU9', '2B', 'Business');
