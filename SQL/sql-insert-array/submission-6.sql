CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

INSERT INTO products (id, name)
VALUES (1, 'Apple'),
       (2, 'Banana'),
       (3, 'Orange');

SELECT * FROM products;
