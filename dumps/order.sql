INSERT INTO shop.orders (id, user_id, address, created_at, status) VALUES (1, 2,'ул. Примерная, 123', '2021-10-01', 'RETURN');
INSERT INTO shop.orders (id, user_id, address, created_at, status) VALUES (2, 3, 'ул. Тестовая, 456', '2021-10-02', 'PROCESSING');
INSERT INTO shop.orders (id, user_id, address, created_at, status) VALUES (3, 4, 'ул. Примерная, 123', '2021-10-03', 'NEW');
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.orders', 'id'), (SELECT MAX(id) FROM shop.orders));