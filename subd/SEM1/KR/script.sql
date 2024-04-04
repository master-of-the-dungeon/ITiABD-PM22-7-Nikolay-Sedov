--1. Создаем таблицу name_product (наименование товаров)

CREATE TABLE name_product 
(code_name integer Not Null Primary Key,
_name text);

--2. Заполняем таблицу name_product (наименование товаров)

INSERT INTO name_product VALUES 
(1, 'Телевизор'),
(2, 'Смартфон'),
(3, 'Ноутбук');

--3. Создаем таблицу product (товар)

CREATE TABLE product
(code_product integer Not Null Primary Key, code_name integer, brand text, price numeric, country text,
 date_production date, category integer, guarantee integer);
 
--4. Заполняем таблицу product (товар)

INSERT INTO product VALUES
(1,	1,	'Рубин',		45000,	'Китай',	'2015-10-02',	3,	3),
(2,	1,	'Звезда',		15000,	'Россия',	'2016-04-09',	2,	4),
(3,	1,	'Фотон',		23000,	'Китай',	'2016-06-12',	2,	2),
(4,	1,	'Радуга',		17500,	'Япония',	'2017-01-12',	1,	5),
(5,	3,	'Электроника',		22000,	'Россия',	'2015-12-15',	3,	4),
(6,	3,	'Байт',			45000,	'Япония',	'2017-02-17',	1,	4),
(7,	2,	'Искра',		15000,	'Китай',	'2015-08-01',	3,	3),
(8,	2,	'Молния',		8500,	'Россия',	'2016-10-15',	2,	3),
(9,	3,	'Самсунг',		25500,	'Китай',	'2017-11-16',	3,	5);
 
 
--5. Создаем таблицу sale (продажа)
 
CREATE TABLE sale 
(date_time_sale timestamp not null, 
code_worker integer, 
number_storage integer,
code_product integer,
quantity integer,
discount real,
PRIMARY KEY (date_time_sale, code_worker)
);

--6. Заполняем таблицу sale (продажа)

INSERT INTO sale VALUES 
('2017-03-21',	4,	10,	4,	22,	0.12),
('2017-03-21',	1,	20,	1,	10,	0.1),
('2017-04-15',	3,	10,	4,	15,	0.05),
('2016-12-25',	3,	40,	5,	9,	0.1),
('2017-05-17',	2,	10,	6,	12,	0.15),
('2016-12-25',	5,	30,	8,	20,	0),
('2015-11-18',	1,	10,	7,	5,	0); 
 

--7. Создаем таблицу storage (склад)

CREATE TABLE storage
(number_storage integer Not Null Primary Key, telephone text, city text, boss text);

--8. Заполняем таблицу storage (склад)

Insert INTO storage VALUES
(10,  	'953-01-89',	'Москва', 	'Иванов П.П.'),
(20,	'712-22-22',	'Тверь',	'Гривко Л.К.'),
(30,	'901-70-44',	'Москва',	'Соломоник К.Ф.'),
(40,	'359-00-14',	'Омск',		'Андреев П.Н.'); 

 --9. Создаем таблицу worker (сотрудник)

CREATE TABLE worker
(code_worker integer Not Null Primary Key, surname text, name_ text, birth_date date,
address text, telephone text, title text, code_firm integer);


--10. Заполняем таблицу worker (сотрудник)

INSERT INTO worker VALUES
(1,		'Дроздов',	 'Юрий',	'1990-02-10',	'Тверь, ул. Садовая, д.5',	'433-76-87',	'Менеджер',			200),
(2,		'Соловьева', 	'Юлия',		'1988-12-12',	'Москва, ул. Мира, д.5',	'43-65-64',	'Нач. отдела',		100),
(3,		'Чижиков',	'Игорь',	'1989-12-13',	'Омск, ул, Королева, 6',	'876-54-67',	'Старший менеджер',	300),
(4,		'Скворцов',	'Олег',		'1979-05-13',	'Москва, Ул. Свободы, 2',	'5445-67-98',	'Менеджер',			100),
(5,		'Уткина',	'Ева',		'1989-02-17',	'Тверь, ул. Гагарина, 8',	'56-85-96',	'Менеджер',			200);
 

--11. Создаем таблицу firm (фирма)

CREATE TABLE firm (code_firm integer Not Null Primary Key, name_company text, city text, telephone text);

--12. Заполняем таблицу firm (фирма)

INSERT INTO firm values 
(100,	'Мир',		'Москва',	'(095) 152-4001'),
(200,	'Эльдорадо',	'Тверь',	'(095) 923-2906'),
(300,	'Электроника',	'Омск',		'(095) 978-1693');

--13. Создаем таблицу storage_goods (хранение товаров)

CREATE TABLE storage_goods
(code_product integer Not Null, number_storage integer Not Null, quantity integer, PRIMARY KEY (code_product, number_storage));

--14. Заполняем таблицу storage_goods (хранение_товаров)

INSERT INTO storage_goods VALUES
(1,	20,	15),
(2,	20,	270),
(3,	40,	350),
(4,	10,	150),
(5,	40,	0),
(6,	10,	36),
(7,	10,	360),
(8,	30,	410),
(1,	40,	75),
(6,	20,	14);


--DROP SCHEMA public CASCADE;
