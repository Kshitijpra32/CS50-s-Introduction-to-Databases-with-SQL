DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS donuts;
DROP TABLE IF EXISTS order1;
DROP TABLE IF EXISTS customer;


CREATE TABLE ingredients(
    id int primary key,
    name char(50),
    price_per_unit int,
    unit int
);

CREATE TABLE donuts(
    id int primary key,
    name char(50),
    gluten_free boolean ,
    price int
);

CREATE TABLE customer(
    id int primary key,
    first_name char(50),
    last_name char(50)
);

CREATE TABLE order1(
    id int primary key,
    customer_id int,
    order_number int,
    order_date datetime,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);
