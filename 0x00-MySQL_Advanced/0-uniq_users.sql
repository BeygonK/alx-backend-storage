-- Creates users table --
-- with three attributes --
CREATE TABLE IF NOT EXISTS users(
id INTEGER AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255)
);
