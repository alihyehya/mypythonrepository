-- Create tables
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    registered_course_id INTEGER,
    FOREIGN KEY (registered_course_id) REFERENCES courses(course_id)
);

-- Insert sample courses
INSERT INTO courses (name, description) VALUES
('Python Basics', 'Introduction to Python programming for beginners.'),
('Data Science 101', 'Learn data analysis, visualization, and basic ML.'),
('Web Development', 'Build websites using HTML, CSS, and JavaScript.'),
('Database Systems', 'Learn SQL, relational databases, and normalization.');

-- Insert sample students
INSERT INTO students (name, email, registered_course_id) VALUES
('Alice Johnson', 'alice@example.com', 1),
('Bob Smith', 'bob@example.com', 2),
('Charlie Brown', 'charlie@example.com', 3),
('Diana Prince', 'diana@example.com', 1);
