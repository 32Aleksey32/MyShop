INSERT INTO shop.categories (id, name) VALUES (1, 'Ноутбуки');
INSERT INTO shop.categories (id, name) VALUES (2, 'Смартфоны');
INSERT INTO shop.categories (id, name) VALUES (3, 'Планшеты');
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.categories', 'id'), (SELECT MAX(id) FROM shop.categories));