
-- Создание представления passengers
CREATE VIEW passengers AS 
SELECT * FROM tickets LIMIT 50;

-- Запрос для вывода пар пассажиров с номерами билетов, отличающимися не более чем на 1
SELECT p1.passenger_name AS passenger1, p2.passenger_name AS passenger2
FROM passengers p1, passengers p2
WHERE ABS(p1.ticket_no - p2.ticket_no) = 1 AND p1.passenger_name != p2.passenger_name;
