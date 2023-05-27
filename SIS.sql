
/*This table will store student information. */
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_email VARCHAR(100) UNIQUE NOT NULL
);

/* this table will store classses information. */

CREATE TABLE classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(100) NOT NULL,
    instructor_name VARCHAR(100) NOT NULL,
    class_schedule VARCHAR(200) NOT NULL
);

/* this table will store assessments information. */

CREATE TABLE assessments (
    assessment_id INT PRIMARY KEY AUTO_INCREMENT,
    assessment_name VARCHAR(100) NOT NULL,
    assessment_type VARCHAR(50) NOT NULL,
    total_marks INT NOT NULL,
    weightage DECIMAL(3,2) NOT NULL
);

/* this table will store student's marks information. */

CREATE TABLE student_classes (
    student_id INT,
    class_id INT,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

/* this table will store student's marks information. */

CREATE TABLE class_assessments (
    class_id INT,
    assessment_id INT,
    PRIMARY KEY (class_id, assessment_id),
    FOREIGN KEY (class_id) REFERENCES classes(class_id),
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);
