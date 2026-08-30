CREATE TABLE students (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    age INTEGER
);

INSERT INTO students (name, age)
  VALUES ('John Doe', 16),
         ('Jane Doe', 19),
         ('Alice Smith', 22),
         ('Bob Smith', 23),
         ('Alice Johnson', 26);

DELETE FROM students
WHERE age < 18 OR name LIKE 'A%';

SELECT * FROM students;
