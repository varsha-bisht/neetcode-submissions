CREATE TYPE status AS ENUM ('active', 'inactive', 'pending');

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 18),
    status status
);

INSERT INTO users (id, name, age, status) VALUES
  (1, 'John Doe', 20, 'active');

INSERT INTO users (id, name, age, status) VALUES
  (2, 'Jane Doe', 27, 'pending');

INSERT INTO users (id, name, age, status) VALUES
  (3, 'John Smith', 28, 'active');

INSERT INTO users (id, name, age, status) VALUES
  (4, 'Jane Smith', 30, 'inactive');

SELECT * FROM users;
