CREATE DATABASE pythonapp_database;

CREATE TABLE superstores_data(
	row_id SERIAL PRIMARY KEY,
	order_id VARCHAR(200),
	order_date DATE,
	ship_date DATE,
	ship_mode VARCHAR(200),
	customer_id VARCHAR(200),
	customer_name VARCHAR(200),
	segment VARCHAR(200),
	country VARCHAR(200),
	city VARCHAR(200),
	state VARCHAR(200),
	postal_code INT(1000000),
	region VARCHAR(200),
	product_id VARCHAR(200),
	category VARCHAR(200),
	sub_category VARCHAR(200),
	product_name VARCHAR(200),
	sales NUMERIC (10,2),
	quantity INT (2000),
	discount NUMERIC(10,2), 
	profit NUMERIC (10,2)	
);

SELECT * FROM superstores_data
LIMIT 10