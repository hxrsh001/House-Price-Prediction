create database house_db;
use house_db;

CREATE TABLE houses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    avg_income FLOAT,
    house_age FLOAT,
    num_rooms INT,
    price FLOAT
);

INSERT INTO houses (avg_income, house_age, num_rooms, price)
VALUES
(1000, 10.2, 3, 10000),
(200, 2.5, 4, 7000),
(300, 3.0, 5, 15000),
(400, 4.0, 1, 11000),
(500, 5.5, 2, 13000),
(600, 6.0, 3, 16000),
(700, 7.0, 4, 18000),
(800, 8.0, 5, 20000),
(900, 9.0, 4, 23000),
(1100, 11.0, 6, 26000),
(1200, 12.0, 7, 29000),
(750, 7.5, 3, 19000),
(650, 6.5, 2, 17000),
(950, 9.5, 5, 24000),
(1300, 13.0, 6, 32000);

