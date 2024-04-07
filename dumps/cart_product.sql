INSERT INTO shop.cart_product (id, quantity, cart_id, product_id) VALUES (1, 3, 2, 1);
INSERT INTO shop.cart_product (id, quantity, cart_id, product_id) VALUES (2, 7, 2, 2);
INSERT INTO shop.cart_product (id, quantity, cart_id, product_id) VALUES (3, 3, 1, 3);
SELECT pg_catalog.setval(pg_get_serial_sequence('shop.cart_product', 'id'), (SELECT MAX(id) FROM shop.cart_product));