
-- 1. Company
INSERT INTO company VALUES ('Toyota', 'Japan'), ('Mercedes', 'Germany'), ('BMW', 'Germany');

-- 2. Brand

-- Toyota
INSERT INTO brand VALUES ('Lexus', 'Toyota'), ('Subaru', 'Toyota'), ('Toyota', 'Toyota');

-- Mercedes
INSERT INTO brand VALUES ('Mercedes-Benz', 'Mercedes'), ('Dodge', 'Mercedes');

-- BMW
INSERT INTO brand VALUES ('BMW', 'BMW'), ('Rolls-Royce', 'BMW');

-- 3. Model

-- Toyota
INSERT INTO model VALUES ('Camry', 'Toyota'), ('GR86', 'Toyota');

-- Lexus
INSERT INTO model VALUES ('NX 300', 'Lexus'), ('GX 460', 'Lexus');

-- Mercedes-Benz
INSERT INTO model VALUES ('S-class', 'Mercedes-Benz'), ('Maybach', 'Mercedes-Benz');

-- BMW
INSERT INTO model VALUES ('X6', 'BMW'), ('X7', 'BMW');

-- Rolls-Royce
INSERT INTO model VALUES ('Phantom', 'Rolls-Royce'), ('Ghost', 'Rolls-Royce');

-- 4. Option

-- Camry
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('Camry', 'White', '2.5l 181hp', 'AKPP 8', 30000);
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('Camry', 'Black', '3l 250hp', 'AKPP 8', 40000);

-- GR86
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('GR86', 'Black', '3l 260hp', 'AKPP 8', 30000);

-- NX 300
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('NX 300', 'Red', '2.8l 240hp', 'AKPP 8', 40000);

-- GX 460
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('GX 460', 'Black', '3l 300hp', 'AKPP 8', 60000);

-- S-class
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('S-class', 'Black', '3l 320hp', 'AKPP 8', 100000);

-- Maybach
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('Maybach', 'Black', '3.6l 400hp', 'AKPP 8', 150000);

-- X6
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('X6', 'Blue', '3.2l 380hp', 'AKPP 8', 100000);

-- X7
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('X7', 'Black', '3.6l 400hp', 'AKPP 8', 80000);

-- Phantom
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('Phantom', 'White', '3l 340hp', 'AKPP 8', 80000);

-- Ghost
INSERT INTO option (model_name, color, engine, transmission, price) VALUES ('Ghost', 'Grey', '3l 340hp', 'AKPP 8', 90000);

-- 5. Dealer
INSERT INTO dealer (dealer_name, phone_number, address) VALUES ('John', '77777777777', 'California');
INSERT INTO dealer (dealer_name, phone_number, address) VALUES ('Bercelius', '77777777999', 'Washington');
INSERT INTO dealer (dealer_name, phone_number, address) VALUES ('Drake', '77777788999', 'Mahachkala');

-- 6. Vehicle
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-11-30 16:09:30.614060', 1, 1);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-11-30 16:09:30.614060', 1, 1);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-12-30 16:09:30.614060', 2, 1);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-08-30 18:09:30.614060', 2, 1);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-08-30 18:09:30.614060', 10, 1);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-08-30 18:09:30.614060', 11, 1);

INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2019-11-30 16:09:30.614060', 4, 2);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-12-30 16:09:30.614060', 6, 2);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-10-30 16:09:30.614060', 2, 2);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-07-30 18:09:30.614060', 3, 2);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-07-30 18:09:30.614060', 8, 2);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-07-30 18:09:30.614060', 9, 2);


INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-11-30 16:09:30.614060', 5, 3);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-06-25 16:09:30.614060', 7, 3);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2020-12-31 16:09:30.614060', 9, 3);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-05-30 18:09:30.614060', 10, 3);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-05-30 18:09:30.614060', 4, 3);
INSERT INTO vehicle (date, option_id, dealer_id) VALUES ('2021-05-30 18:09:30.614060', 5, 3);

-- 7. Customer
INSERT INTO customer (customer_name, phone_number, gender, annual_income) VALUES ('Joshua', '12345678910', 'M', 120000);
INSERT INTO customer (customer_name, phone_number, gender, annual_income) VALUES ('Elizabet', '12345678911', 'F', 120000);
INSERT INTO customer (customer_name, phone_number, gender, annual_income) VALUES ('Jacob', '12345676710', 'M', 130000);
INSERT INTO customer (customer_name, phone_number, gender, annual_income) VALUES ('Emma', '12345678999', 'F', 110000);

-- 8. Deal
INSERT INTO deal (vin, date, customer_id) VALUES (2, '2020-12-30 16:09:30.614060', 1);
INSERT INTO deal (vin, date, customer_id) VALUES (3, '2021-01-30 16:09:30.614060', 1);
INSERT INTO deal (vin, date, customer_id) VALUES (43, '2021-12-01 16:09:30.614060', 1);
INSERT INTO deal (vin, date, customer_id) VALUES (46, '2020-08-25 16:09:30.614060', 1);



INSERT INTO deal (vin, date, customer_id) VALUES (4, '2021-09-30 18:09:30.614060', 2);
INSERT INTO deal (vin, date, customer_id) VALUES (48, '2021-08-30 18:09:30.614060', 2);
INSERT INTO deal (vin, date, customer_id) VALUES (47, '2021-02-18 16:09:30.614060', 2);


INSERT INTO deal (vin, date, customer_id) VALUES (41, '2019-12-06 16:09:30.614060', 3);
INSERT INTO deal (vin, date, customer_id) VALUES (42, '2021-01-11 16:09:30.614060', 3);
INSERT INTO deal (vin, date, customer_id) VALUES (1, '2021-12-01 16:09:30.614060', 3);

INSERT INTO deal (vin, date, customer_id) VALUES (44, '2020-09-27 18:09:30.614060', 4);
INSERT INTO deal (vin, date, customer_id) VALUES (45, '2021-11-30 16:09:30.614060', 4);
INSERT INTO deal (vin, date, customer_id) VALUES (49, '2021-09-12 18:09:30.614060', 4);
INSERT INTO deal (vin, date, customer_id) VALUES (50, '2021-09-12 18:09:30.614060', 4);


