INSERT INTO shop.users (id, last_login, is_superuser, username, is_staff, is_active, date_joined, last_name, first_name, middle_name, phone_number, email, password) VALUES (1, '2024-01-06 08:33:27.525849 +00:00', true, 'admin1', true, true, '2024-01-04 12:39:41.942025 +00:00', 'Осипов', 'Алексей', 'Александрович', '+79817729215', 'admin1@mail.ru', 'pbkdf2_sha256$600000$zz5xhDCZNIZhmpEwk9nKhf$mQexl+NdONja8/2OXqhKzV5VXkSNFrWX8FESXIo7r0M=');
INSERT INTO shop.users (id, username, password, first_name, last_name, middle_name, email, phone_number, is_active, date_joined, is_superuser, is_staff) VALUES (2, 'user2', 'password2', 'Иван', 'Иванов', 'Иванович', 'user2@example.com', '1234567890', true, '2024-01-04 12:41:41.942025 +00:00', false, false);
INSERT INTO shop.users (id, username, password, first_name, last_name, middle_name, email, phone_number, is_active, date_joined, is_superuser, is_staff) VALUES (3, 'user3', 'password3', 'Мария', 'Смирнова', 'Петровна', 'user3@example.com', '0987654321', true, '2024-01-04 12:40:41.942025 +00:00', false, false);
INSERT INTO shop.users (id, username, password, first_name, last_name, middle_name, email, phone_number, is_active, date_joined, is_superuser, is_staff) VALUES (4, 'user4', 'password4', 'Екатерина', 'Михайлова', 'Николаевна', 'user4@example.com', '0555555', true, '2024-01-04 12:41:41.942025 +00:00', false, false);