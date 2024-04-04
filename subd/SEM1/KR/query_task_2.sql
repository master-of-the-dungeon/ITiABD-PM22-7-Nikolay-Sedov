
SELECT sg.number_storage, COUNT(*) as total_domestic_products
FROM storage_goods sg
JOIN product p ON sg.code_product = p.code_product
WHERE p.country = 'Россия' AND p.category IN (1, 2)
GROUP BY sg.number_storage;
