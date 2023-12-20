
SELECT 
    np._name,
    p.brand
FROM 
    product p
JOIN 
    name_product np ON p.code_name = np.code_name
JOIN 
    storage_goods sg ON p.code_product = sg.code_product
WHERE 
    sg.number_storage IN (10, 20, 30);
