CREATE TABLE users (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT
);

INSERT INTO users (username) VALUES
  ('Alice'),
  ('Bob'),
  (NULL),
  ('Charlie'),
  (NULL);

UPDATE users
SET username = 'anonymous'
WHERE username IS NULL;

SELECT * FROM users;
