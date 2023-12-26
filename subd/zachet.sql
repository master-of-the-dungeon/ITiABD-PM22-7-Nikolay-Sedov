-- Скидки
SELECT np._name, p.brand, s.quantity, p.price, 
       (p.price * s.quantity * (1 - s.discount)) AS cost_with_discount
FROM sale s
JOIN product p ON s.code_product = p.code_product
JOIN name_product np ON p.code_name = np.code_name
WHERE s.discount > 0;

-- Москва
SELECT 
    np._name AS ProductName,
    COUNT(*) AS NumberOfSales
FROM sale s
JOIN product p ON s.code_product = p.code_product
JOIN name_product np ON p.code_name = np.code_name
JOIN storage st ON s.number_storage = st.number_storage
WHERE 
    st.city = 'Москва' AND
    s.discount > 0
GROUP BY np._name;


