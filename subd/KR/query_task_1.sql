
SELECT f.name_company, w.address, w.surname, w.title, np._name, p.brand, p.price, p.date_production, p.country
FROM firm f
JOIN worker w ON f.code_firm = w.code_firm
JOIN sale s ON w.code_worker = s.code_worker
JOIN product p ON s.code_product = p.code_product
JOIN name_product np ON p.code_name = np.code_name
WHERE 
    (p.country = 'Россия' AND EXTRACT(YEAR FROM p.date_production) IN (2016, 2017) AND (p.price < 10000 OR p.price > 30000))
    OR 
    (f.city IN ('Москва', 'Омск') AND w.title IN ('Менеджер', 'Старший менеджер') AND p.country != 'Россия')
ORDER BY f.name_company ASC, p.price DESC;
