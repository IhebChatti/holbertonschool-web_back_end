--script that creates a table users following these requirements:
--these attributes: id, email, name
--If the table already exists, your script should not fail
--The script can be executed on any database

CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT,
                                                  email CHAR(255) NOT NULL UNIQUE,
                                                                           name CHAR(255),
                                                                                PRIMARY KEY (id));
