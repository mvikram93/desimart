Create Database desimart;

use desimart;

-- User Table
CREATE TABLE tbl_user (
    User_Id INT PRIMARY KEY,
    Password VARCHAR(255),
    Mail_Id VARCHAR(255),
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255),
    Phone_no VARCHAR(20),
    Address TEXT,
    City VARCHAR(255),
    State VARCHAR(255),
    zip_code VARCHAR(20)
);

-- Category Table
CREATE TABLE tbl_category (
    Category_ID INT PRIMARY KEY,
    Category_Name VARCHAR(255)
);

-- Product Table
CREATE TABLE tbl_product (
    Product_ID INT PRIMARY KEY,
    Product_name VARCHAR(255),
    Price DECIMAL(10, 2),
    Category_ID INT,
    FOREIGN KEY (Category_ID) REFERENCES tbl_category(Category_ID)
);

-- Order Table
-- Note: `Order` is a reserved keyword in MySQL. It's recommended to choose a different table name.
CREATE TABLE tbl_order (
    Order_Id INT PRIMARY KEY,
    Tax_Price DECIMAL(10, 2),
    Total_Price DECIMAL(10, 2),
    Order_Date_Time DATETIME,
    User_ID INT,
    FOREIGN KEY (User_ID) REFERENCES tbl_user(User_Id)
);

-- Order_Line Table
CREATE TABLE tbl_order_line (
    Product_ID INT,
    Order_ID INT,
    Quantity INT,
    PRIMARY KEY (Product_ID, Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES tbl_product(Product_ID),
    FOREIGN KEY (Order_ID) REFERENCES tbl_Order(Order_Id)
);

-- Delivery Table
CREATE TABLE tbl_delivery (
    DeliveryPerson_Id INT PRIMARY KEY,
    DeliveryPerson_Name VARCHAR(255),
    DeliveryPerson_Contact VARCHAR(20),
    Estimated_delivery DATETIME,
    Order_Id INT,
    FOREIGN KEY (Order_Id) REFERENCES tbl_Order(Order_Id)
);
