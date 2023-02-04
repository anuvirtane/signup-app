CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE courses (id SERIAL PRIMARY KEY, day_minus_two DATE, day_minus_one DATE, day_zero DATE, day_ten DATE, day_eleven DATE);
CREATE TABLE participations (id SERIAL PRIMARY KEY, course_id INTEGER REFERENCES courses, user_id INTEGER REFERENCES users, arrival TIMESTAMP, departure TIMESTAMP);

INSERT INTO courses (day_minus_two, day_minus_one, day_zero, day_ten, day_eleven) VALUES ('2023-04-03', '2023-04-04', '2023-04-05', '2023-04-15', '2023-04-16');
INSERT INTO courses (day_minus_two, day_minus_one, day_zero, day_ten, day_eleven) VALUES ('2023-12-25', '2023-12-26', '2023-12-27', '2024-01-06', '2024-01-07');
INSERT INTO users (username, password) VALUES ('testuser', '1234');