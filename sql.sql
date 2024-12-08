DELIMITER $$

CREATE PROCEDURE DemoProcedure()
BEGIN
    DECLARE name VARCHAR(50);
    DECLARE age INT;

    SET name = 'John Doe';
    SET age = 30;

    SELECT name AS Name, age AS Age;
END$$
DELIMITER ;

CALL DemoProcedure();


-- إنشاء مستخدم جديد باسم aboud مع كلمة مرور 500201
-- CREATE USER 'aboud'@'localhost' IDENTIFIED BY '500201';

-- إعطاء جميع الصلاحيات للمستخدم aboud على جميع قواعد البيانات
-- GRANT ALL PRIVILEGES ON *.* TO 'aboud'@'localhost';

-- إنشاء قاعدة بيانات جديدة باسم DBAboud
-- CREATE DATABASE DBAboud;

-- استخدام قاعدة البيانات التي تم إنشاؤها
-- USE DBAboud;

-- إنشاء جدول باسم pet يحتوي على الأعمدة id, age, name
-- CREATE TABLE pet (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     age INT NOT NULL,
--     name VARCHAR(100) NOT NULL
-- );

-- إدخال بيانات في الجدول pet
-- INSERT INTO pet (age, name) VALUES 
-- (17, 'Buddy'),
-- (19, 'Max'),
-- (20, 'Charlie'),
-- (18, 'Milo'),
-- (25, 'Rocky');





-- DROP DATABASE 
-- 	SQLA;
-- CREATE DATABASE 
-- 	SQLA;

-- USE aboud;

-- SET GLOBAL local_infile = 1;

-- CREATE TABLE IF NOT EXISTS 
-- 	pet (id 
-- INT PRIMARY KEY,
-- 	age
-- INT,
-- 	name 
-- VARCHAR(255)
-- 	);
-- USE aboud;
-- LOAD DATA LOCAL INFILE 
-- 	'C:\Users\Mohammed\OneDrive\Desktop\Code\info.CSV'
-- INTO TABLE
-- 	pet
-- FIELDS TERMINATED BY 
-- 	','
-- LINES TERMINATED BY 
-- 	'\n'
-- IGNORE 1 ROWS
-- 	(id, age, name);

-- SHOW DATABASES;
-- SHOW TABLES;
-- DESCRIBE pet;
-- SELECT * FROM pet;
-- SHOW VARIABLES LIKE 'local_infile';
-- SHOW VARIABLES LIKE 'load_data';
-- INSERT INTO
-- 	pet (name)
-- VALUE 
-- 	("Shosho");
-- SELECT * FROM pet;
