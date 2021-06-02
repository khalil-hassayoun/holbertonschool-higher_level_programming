-- creates a table that can't have a null name
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

