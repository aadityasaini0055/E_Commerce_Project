-- ============================================================
--  E-Commerce Analytics  —  MySQL Schema
--  Run: mysql -u root -p ecommerce_analytics < database/schema.sql
-- ============================================================

CREATE TABLE IF NOT EXISTS products (
    id           INT PRIMARY KEY,
    title        VARCHAR(255),
    price        DECIMAL(10, 2),
    category     VARCHAR(100),
    rating       DECIMAL(3, 1),
    rating_count INT,
    source_api   VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS users (
    id       INT PRIMARY KEY,
    username VARCHAR(100),
    email    VARCHAR(255),
    phone    VARCHAR(50),
    city     VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders (
    id             INT PRIMARY KEY,
    user_id        INT,
    total_price    DECIMAL(10, 2),
    products_count INT,
    source_api     VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS etl_logs (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    run_time   DATETIME DEFAULT NOW(),
    table_name VARCHAR(100),
    status     VARCHAR(50),
    records    INT
);
