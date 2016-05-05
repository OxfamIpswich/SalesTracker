DROP TABLE IF EXISTS category;
CREATE TABLE IF NOT EXISTS category
(
	id INT  PRIMARY KEY,
	parent_id INT,
	name VARCHAR(255) NOT NULL,
	code VARCHAR(3) 
);

DROP TABLE IF EXISTS reading;
CREATE TABLE IF NOT EXISTS reading
(
	id INT  PRIMARY KEY,
	datasource_id INT NOT NULL,
	start DATETIME NOT NULL,
	end DATETIME NOT NULL
);

DROP TABLE IF EXISTS actual;
CREATE TABLE IF NOT EXISTS actual
(
	id  PRIMARY KEY,
	category_id INT NOT NULL,
	reading_id INT NOT NULL,
	qty INT DEFAULT 0,
	ammount DECIMAL(12,2) DEFAULT 0.00,
	currency CHAR(3) NOT NULL
);

DROP TABLE IF EXISTS region;
CREATE TABLE IF NOT EXISTS region
(
	id INT  PRIMARY KEY,
	parent_id INT,
	code VARCHAR(4),
	name VARCHAR(50)
);

DROP TABLE IF EXISTS shop;
CREATE TABLE IF NOT EXISTS shop
(
	id INT  PRIMARY KEY,
	region_id INT NOT NULL,
	code VARCHAR(5),
	name VARCHAR(50)
);

DROP TABLE IF EXISTS datasource_type;
CREATE TABLE IF NOT EXISTS datasource_type
(
	id INT PRIMARY KEY,
	name VARCHAR(20)
);

DROP TABLE IF EXISTS datasource;
CREATE TABLE IF NOT EXISTS datasource
(
	id INT  PRIMARY KEY,
	shop_id INT NOT NULL,
	datasource_type_id INT NOT NULL,
	name VARCHAR(20)
);

DROP TABLE IF EXISTS datasource_type_category;
CREATE TABLE IF NOT EXISTS datasource_type_category
(
	datasource_type_id INT,
	category_id INT,
	PRIMARY KEY ( datasource_type_id, category_id )
);
