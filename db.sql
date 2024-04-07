Create Database desimart;

use desimart;

-- User Table
CREATE TABLE tbl_user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    password VARCHAR(255),
    mail_id VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_no VARCHAR(20),
    address TEXT,
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(20)
);

-- Category Table
CREATE TABLE tbl_category (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255)
);

-- Product Table
CREATE TABLE tbl_product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255),
    price DECIMAL(10, 2),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES tbl_category(category_id)
);

-- Order Table
-- Note: `Order` is a reserved keyword in MySQL. It's recommended to choose a different table name.
CREATE TABLE tbl_order (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    tax_price DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    order_date_time DATETIME,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES tbl_user(user_id)
);

-- Order_Line Table
CREATE TABLE tbl_order_line (a
    product_id INT,
    order_id INT,
    quantity INT,
    Price float DEFAULT NULL,
    total_amount float DEFAULT NULL,
    PRIMARY KEY (product_id, order_id),
    FOREIGN KEY (product_id) REFERENCES tbl_product(product_id),
    FOREIGN KEY (order_id) REFERENCES tbl_Order(order_id)
);

-- Delivery Table
CREATE TABLE tbl_delivery (
    deliveryperson_id INT PRIMARY KEY AUTO_INCREMENT,
    deliveryperson_name VARCHAR(255),
    deliveryperson_contact VARCHAR(20),
    estimated_delivery DATETIME,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES tbl_Order(order_id)
);
