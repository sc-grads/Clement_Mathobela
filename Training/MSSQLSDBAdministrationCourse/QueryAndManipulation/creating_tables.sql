CREATE TABLE customerInfo(
customer_id int PRIMARY KEY IDENTITY(1,1),
customer_Name varchar (50) NOT NULL,
customer_Address varchar (50),
  customer_Phone varchar (15) NOT NULL,
)

INSERT INTO customerInfo VALUES('Bob','Joburg','+27 72 123 4567');
SELECT * from customerInfo
INSERT INTO customerInfo VALUES('Alice','Polokwane','+27 76 124 8567'),
('Sam','Durban','+27 71 987 0923'), ('Tom','New Castle','+23 81 625 9072'),('Kristy','Midrand','+27 82 569 1324');

CREATE TABLE orderInfo(
  order_id int PRIMARY KEY IDENTITY(100,1),
  customer_id int NOT NULL,
  order_date DATETIME,
  item_ordered varchar (50),
  FOREIGN KEY (customer_id) REFERENCES customerInfo (customer_id)
)
