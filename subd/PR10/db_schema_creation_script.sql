
-- 1. Создание новой базы данных (Этот шаг должен быть выполнен отдельно, если у вас нет прав суперпользователя)
-- CREATE DATABASE mydatabase;

-- Подключение к новой базе данных не включено в SQL-скрипт, это должно быть выполнено через ваш клиент базы данных
-- \c mydatabase

-- 2. Создание схемы, названной так же, как и пользователь (Замените 'username' на ваше имя пользователя)
CREATE SCHEMA IF NOT EXISTS username;

-- 3. Создание схемы my_app
CREATE SCHEMA IF NOT EXISTS my_app;

-- 4. Создание нескольких таблиц в обоих схемах
-- В схеме пользователя
CREATE TABLE IF NOT EXISTS username.courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
    -- другие поля...
);

CREATE TABLE IF NOT EXISTS username.students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    -- другие поля...
);

-- В схеме my_app
CREATE TABLE IF NOT EXISTS my_app.courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
    -- другие поля...
);

CREATE TABLE IF NOT EXISTS my_app.students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    -- другие поля...
);

-- 5. Получение описания созданных схем и список всех таблиц в них
-- Для выполнения в psql, не включено в SQL-скрипт:
-- \dn+
-- \dt username.*
-- \dt my_app.*

-- 6. Установка пути поиска так, чтобы при подключении к БД таблицы из обоих схем были доступны по неквалифицированному имени
SET search_path TO username, my_app;

-- 7. Проверка правильности настройки пути поиска (выполнение в psql или через клиент базы данных)
-- SELECT * FROM courses;
