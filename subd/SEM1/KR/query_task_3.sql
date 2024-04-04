
SELECT 
    np._name,
    p.brand,
    p.price AS original_price,
    CASE
        WHEN p.country = 'Россия' AND EXTRACT(YEAR FROM p.date_production) = 2015 THEN p.price * 0.70
        WHEN EXTRACT(YEAR FROM p.date_production) = 2016 THEN p.price * 0.85
        WHEN p.country != 'Россия' AND EXTRACT(YEAR FROM p.date_production) = 2017 THEN p.price * 1.05
        ELSE p.price
    END AS adjusted_price
FROM 
    product p
JOIN 
    name_product np ON p.code_name = np.code_name;
