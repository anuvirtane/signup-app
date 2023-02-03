CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE courses (id SERIAL PRIMARY KEY, day_minus_two DATE, day_minus_one DATE, day_zero DATE, day_ten DATE, day_eleven DATE);
INSERT INTO courses (day_minus_two, day_minus_one, day_zero, day_ten, day_eleven) VALUES ('2023-04-03', '2023-04-04', '2023-04-05', '2023-04-15', '2023-04-16')