-- Creates a table (second_table)
-- Insert values into the table

CREATE TABLE IF NOT EXISTS second_table(
   id INT,
   name VARCHAR(256),
   score INT
);

INSERT INTO second_table(id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table(id, score) VALUES (2, 166);
INSERT INTO second_table(id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table(id, name, score) VALUES (4, "", 8);

