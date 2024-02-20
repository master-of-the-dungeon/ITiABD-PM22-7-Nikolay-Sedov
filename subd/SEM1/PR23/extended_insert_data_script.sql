
-- Добавление дополнительных данных в таблицу 'bookings'
INSERT INTO bookings (book_ref, book_date, total_amount) VALUES
('GHI789', '2023-08-01 14:00:00', 450.00),
('JKL012', '2023-08-02 15:00:00', 550.00),
('MNO345', '2023-08-03 16:00:00', 650.00);

-- Добавление дополнительных данных в таблицу 'tickets'
INSERT INTO tickets (ticket_no, book_ref, passenger_id, passenger_name) VALUES
('TKT003', 'GHI789', 'PAX003', 'Alice Johnson'),
('TKT004', 'JKL012', 'PAX004', 'Bob Smith'),
('TKT005', 'MNO345', 'PAX005', 'Carol White');

-- Добавление дополнительных данных в таблицу 'flights'
INSERT INTO flights (flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, aircraft_code, status) VALUES
('DL789', '2023-08-26 09:00:00', '2023-08-26 11:30:00', 'CDG', 'JFK', 'A319', 'Arrived'),
('UA345', '2023-08-26 10:00:00', '2023-08-26 12:30:00', 'JFK', 'LHR', 'B763', 'Cancelled');

-- Добавление дополнительных данных в таблицу 'ticket_flights'
INSERT INTO ticket_flights (ticket_no, flight_id, fare_conditions, amount) VALUES
('TKT003', 3, 'Business', 300.00),
('TKT004', 4, 'Economy', 250.00),
('TKT005', 4, 'Economy', 200.00);
