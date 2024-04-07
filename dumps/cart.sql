INSERT INTO shop.cart (id, user_id, created_at, updated_at) VALUES(1, 1, '2021-10-01 09:30:00', '2021-10-01 09:30:00');
INSERT INTO shop.cart (id, user_id, created_at, updated_at) VALUES (2, 2, '2021-10-02 14:15:00', '2021-10-01 09:30:00');
INSERT INTO shop.cart (id, user_id, created_at, updated_at) VALUES (3, 3, '2021-10-03 11:45:00', '2021-10-01 09:30:00');
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.cart', 'id'), (SELECT MAX(id) FROM shop.cart));