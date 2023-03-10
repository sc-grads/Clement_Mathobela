CREATE TABLE customer(
customer_id INT PRIMARY KEY IDENTITY,
firstName VARCHAR(50),
lastName VARCHAR(50),
email VARCHAR(50) NOT NULL UNIQUE,
user_password VARCHAR(50)
)
GO

CREATE TABLE customer_address(
id INT PRIMARY KEY IDENTITY,
customer_id INT,
phone_number VARCHAR(15) NOT NULL,
home_address varchar(100) NOT NULL,
city VARCHAR(30)
)
GO


CREATE TABLE user_admin(
id INT PRIMARY KEY IDENTITY,
email VARCHAR UNIQUE NOT NULL,
admin_password VARCHAR(50 )NOT NULL
)
GO

CREATE TABLE product(
product_id INT PRIMARY KEY IDENTITY(1000,1),
model_name VARCHAR(50) NOT NULL,
price DECIMAL,
quantity INT,
discription VARCHAR(255)
)
GO
--
CREATE TABLE cart_items(
id INT PRIMARY KEY IDENTITY,
customer_id INT,
quantity INT,
total_amount DECIMAl,
)
GO

CREATE TABLE options(
id INT PRIMARY KEY,
color VARCHAR(20)
)

