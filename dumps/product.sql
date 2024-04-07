INSERT INTO shop.products (id, name, price, description, image, category_id) VALUES (1, 'iPhone 15', 120000, 'Смартфон Apple iPhone 15', 'iphone15.jpg', 2);
INSERT INTO shop.products (id, name, price, description, image, category_id) VALUES (2, 'MacBook', 150000, 'Ноутбук Apple MacBook', 'macbook.jpg', 1);
INSERT INTO shop.products (id, name, price, description, image, category_id) VALUES (3, 'MacBook Pro', 195000, 'Ноутбук Apple MacBook Pro', 'macbook_pro.jpg', 1);
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.products', 'id'), (SELECT MAX(id) FROM shop.products));