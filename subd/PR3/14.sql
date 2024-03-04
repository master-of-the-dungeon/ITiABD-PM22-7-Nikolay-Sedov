SELECT
    model,
    COUNT(CASE WHEN seat_class = 'Бизнес' THEN 1 END) AS business_class_seats,
    COUNT(CASE WHEN seat_class = 'Эконом' THEN 1 END) AS economy_class_seats,
    COUNT(CASE WHEN seat_class = 'Комфорт' THEN 1 END) AS comfort_class_seats
FROM
    airplane_seats
GROUP BY
    model;
