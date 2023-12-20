
CREATE TABLE Employee (
    code_employee integer NOT NULL PRIMARY KEY,
    surname text,
    first_name text,
    middle_name text,
    address text,
    code_firm integer,
    FOREIGN KEY (code_firm) REFERENCES firm (code_firm) ON DELETE CASCADE ON UPDATE SET NULL
);

INSERT INTO Employee (code_employee, surname, first_name, middle_name, address, code_firm) VALUES
(1, 'Иванов', 'Иван', 'Иванович', 'Адрес 1', 100),
(2, 'Петров', 'Петр', 'Петрович', 'Адрес 2', 200),
(3, 'Сидоров', 'Сидор', 'Сидорович', 'Адрес 3', 300),
(4, 'Алексеев', 'Алексей', 'Алексеевич', 'Адрес 4', 100),
(5, 'Николаев', 'Николай', 'Николаевич', 'Адрес 5', 200);

SELECT * FROM Employee