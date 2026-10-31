INSERT INTO profiles (username, full_name, email, phone, bio, is_corporate) 
VALUES 
('Benjamin', 'Netanyahu', 'Netanyahu@remarket.com', '5551112233', 'Donanım meraklısı ve geliştirici.', 0),
('tech_store', 'Teknoloji Deposu A.Ş.', 'info@techstore.com', '5442223344', 'Kurumsal donanım tedarikçisi.', 1);

INSERT INTO listings (user_id, title, content, category, start_price, stock_count, is_active) 
VALUES 
(1, 'Ryzen 5 5600 İşlemci', 'Kutulu, faturalı, temiz kullanılmış işlemci.', 'CPU', 3500.0, 1, 1),
(2, 'RTX 3060 12GB Ekran Kartı', 'Kurumsal garantili, temiz mining görmemiş kart.', 'GPU', 7500.0, 5, 1);

INSERT INTO bids (listing_id, user_id, amount) 
VALUES 
(1, 2, 3700.0); 

INSERT INTO messages (sender_id, receiver_id, content) 
VALUES 
(1, 2, 'Merhaba, ürünün garantisi devam ediyor mu?');