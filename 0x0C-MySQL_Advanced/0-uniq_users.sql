--script that creates a table users following these requirements:
--these attributes: id, email, name
--If the table already exists, your script should not fail
--The script can be executed on any database

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
