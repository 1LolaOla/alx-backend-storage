-- script that creates a table users with follwing fields

CREATE TABLE IF NOT EXISTS users(
	id INT AUTO_INCREMENT NOT NULL,
	email varchar(255) UNIQUE NOT NULL,
	name varchar(255),
	PRIMARY KEY (id)
);
