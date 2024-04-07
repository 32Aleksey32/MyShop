INSERT INTO shop.reviews (user_id, product_id, text, rating, created_at) VALUES (1, 1, 'Отличный продукт!', 5, '2021-10-01 09:30:00');
INSERT INTO shop.reviews (user_id, product_id, text, rating, created_at) VALUES (2, 1, 'Очень доволен покупкой!', 4, '2021-10-02 14:15:00');
INSERT INTO shop.reviews (user_id, product_id, text, rating, created_at) VALUES (3, 2, 'Отличный ноутбук!', 5, '2021-10-03 11:45:00');
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.reviews', 'id'), (SELECT MAX(id) FROM shop.reviews));