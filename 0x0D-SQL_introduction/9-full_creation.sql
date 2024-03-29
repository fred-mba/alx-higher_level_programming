-- Creates a table second_table in the database hbtn_0c_0 in MySQL server and add multiples rows
  -- Second_table description:
  -- id INT
  -- name VARCHAR(256)
  -- score INT
-- The database name will be passed as an argument to the mysql command
-- If the table second_table already exists, the script should not fail
-- Not allowed to use the SELECT and SHOW statements
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

-- script should create these records:
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES(4, "George", 8);
