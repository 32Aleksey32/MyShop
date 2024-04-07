INSERT INTO shop.orders (id, product_id, user_id, quantity, address, date, status) VALUES (1, 1, 2, 2, 'ул. Примерная, 123', '2021-10-01', 'RETURN');
INSERT INTO shop.orders (id, product_id, user_id, quantity, address, date, status) VALUES (2, 2, 3, 1, 'ул. Тестовая, 456', '2021-10-02', 'PROCESSING');
INSERT INTO shop.orders (id, product_id, user_id, quantity, address, date, status) VALUES (3, 1, 4, 3, 'ул. Примерная, 123', '2021-10-03', 'NEW');
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.orders', 'id'), (SELECT MAX(id) FROM shop.orders));