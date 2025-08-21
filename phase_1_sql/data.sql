-- insertion of data in different tables of Lib_Mangement_system

-- Insert Libraries
INSERT INTO Library (name, campus_location, contact_email, phone_number)
VALUES
('Central Library', 'Main Campus', 'central@univ.edu', '1234567890'),
('Science Library', 'Science Block', 'science@univ.edu', '1234567891'),
('Arts Library', 'Arts Block', 'arts@univ.edu', '1234567892');

-- Insert Books (15 Books, distributed across 3 libraries)
INSERT INTO Book (title, isbn, publication_date, total_copies, available_copies, library_id)
VALUES
('Physics for Beginners', 'ISBN001', '2015-06-10', 10, 8, 1),
('Advanced Chemistry', 'ISBN002', '2016-08-12', 12, 10, 1),
('Biology 101', 'ISBN003', '2017-03-05', 8, 6, 1),
('Modern Art', 'ISBN004', '2018-09-15', 6, 5, 2),
('History of Europe', 'ISBN005', '2014-02-20', 7, 6, 2),
('Artificial Intelligence', 'ISBN006', '2020-07-22', 15, 12, 3),
('Machine Learning', 'ISBN007', '2021-01-10', 20, 18, 3),
('Data Science Handbook', 'ISBN008', '2019-10-05', 10, 9, 3),
('Psychology Basics', 'ISBN009', '2013-11-11', 5, 4, 2),
('Cultural Studies', 'ISBN010', '2012-12-01', 6, 5, 2),
('Creative Writing', 'ISBN011', '2015-05-18', 8, 7, 1),
('World War II', 'ISBN012', '2011-04-04', 9, 7, 2),
('Digital Transformation', 'ISBN013', '2022-06-06', 12, 11, 3),
('Fantasy Tales', 'ISBN014', '2019-09-09', 14, 13, 1),
('Neuroscience Explained', 'ISBN015', '2018-08-08', 10, 8, 1);

-- Insert Authors
INSERT INTO Author (first_name, last_name, birth_date, nationality, biography)
VALUES
('John', 'Smith', '1970-05-15', 'American', 'Author of science fiction books'),
('Emily', 'Brown', '1980-03-10', 'British', 'Writes historical novels'),
('Michael', 'Johnson', '1965-09-20', 'Canadian', 'Specializes in science and research'),
('Sophia', 'Davis', '1978-12-02', 'Australian', 'Writes art and culture books'),
('David', 'Wilson', '1985-07-25', 'Indian', 'Technology and computing expert'),
('Emma', 'Clark', '1990-08-18', 'American', 'Writes fantasy novels'),
('James', 'Anderson', '1972-11-30', 'British', 'Research papers in biology'),
('Olivia', 'Martin', '1988-01-05', 'Canadian', 'Writes psychology books');

-- Map Books to Authors
INSERT INTO Book_Author (book_id, author_id) VALUES
(1, 1), (2, 1), (3, 7),
(4, 4), (5, 2),
(6, 5), (7, 5), (8, 5),
(9, 8), (10, 4),
(11, 6), (12, 2),
(13, 5), (14, 6), (15, 8);

-- Insert Categories
INSERT INTO Category (name, description)
VALUES
('Science', 'Books related to science and research'),
('Arts', 'Books about arts and culture'),
('Technology', 'Books about technology and computing'),
('Fiction', 'Fiction and novels'),
('History', 'Historical books');


-- Map Books to Categories
INSERT INTO Book_Category (book_id, category_id) VALUES
(1, 1), (2, 1), (3, 1),
(4, 2), (5, 5),
(6, 3), (7, 3), (8, 3),
(9, 1), (10, 2),
(11, 4), (12, 5),
(13, 3), (14, 4), (15, 1);

-- Insert Members (20 members: mix of students and faculty)
INSERT INTO Member (first_name, last_name, email, phone, member_type, registration_date)
VALUES
('Alice', 'Walker', 'alice@example.com', '9876543210', 'Student', '2024-01-10'),
('Bob', 'Miller', 'bob@example.com', '9876543211', 'Faculty', '2024-02-15'),
('Charlie', 'Harris', 'charlie@example.com', '9876543212', 'Student', '2024-03-01'),
('Diana', 'Lewis', 'diana@example.com', '9876543213', 'Faculty', '2024-03-20'),
('Ethan', 'Young', 'ethan@example.com', '9876543214', 'Student', '2024-04-05'),
('Fiona', 'Allen', 'fiona@example.com', '9876543215', 'Faculty', '2024-05-12'),
('George', 'King', 'george@example.com', '9876543216', 'Student', '2024-06-10'),
('Hannah', 'Scott', 'hannah@example.com', '9876543217', 'Faculty', '2024-07-01'),
('Ian', 'Adams', 'ian@example.com', '9876543218', 'Student', '2024-07-15'),
('Julia', 'Nelson', 'julia@example.com', '9876543219', 'Faculty', '2024-08-05'),
('Kevin', 'Carter', 'kevin@example.com', '9876543220', 'Student', '2024-08-18'),
('Laura', 'Mitchell', 'laura@example.com', '9876543221', 'Faculty', '2024-09-02'),
('Mike', 'Perez', 'mike@example.com', '9876543222', 'Student', '2024-09-20'),
('Nina', 'Roberts', 'nina@example.com', '9876543223', 'Faculty', '2024-10-10'),
('Oscar', 'Turner', 'oscar@example.com', '9876543224', 'Student', '2024-10-25'),
('Paula', 'Phillips', 'paula@example.com', '9876543225', 'Faculty', '2024-11-12'),
('Quinn', 'Evans', 'quinn@example.com', '9876543226', 'Student', '2024-11-30'),
('Ryan', 'Collins', 'ryan@example.com', '9876543227', 'Faculty', '2024-12-15'),
('Sophia', 'Stewart', 'sophia@example.com', '9876543228', 'Student', '2024-12-25'),
('Tom', 'Morris', 'tom@example.com', '9876543229', 'Faculty', '2025-01-05');

-- Insert Borrowings (25 records)
INSERT INTO Borrowing (member_id, book_id, borrow_date, due_date, return_date, late_fee)
VALUES
(1, 1, '2025-07-01', '2025-07-15', '2025-07-14', 0),
(2, 2, '2025-07-02', '2025-07-16', NULL, 0),
(3, 3, '2025-07-03', '2025-07-17', '2025-07-20', 5.00),
(4, 4, '2025-07-04', '2025-07-18', NULL, 0),
(5, 5, '2025-07-05', '2025-07-19', '2025-07-18', 0),
(6, 6, '2025-07-06', '2025-07-20', '2025-07-25', 10.00),
(7, 7, '2025-07-07', '2025-07-21', NULL, 0),
(8, 8, '2025-07-08', '2025-07-22', '2025-07-22', 0),
(9, 9, '2025-07-09', '2025-07-23', '2025-07-30', 14.00),
(10, 10, '2025-07-10', '2025-07-24', NULL, 0),
(11, 11, '2025-07-11', '2025-07-25', '2025-07-27', 4.00),
(12, 12, '2025-07-12', '2025-07-26', '2025-07-26', 0),
(13, 13, '2025-07-13', '2025-07-27', '2025-07-30', 6.00),
(14, 14, '2025-07-14', '2025-07-28', NULL, 0),
(15, 15, '2025-07-15', '2025-07-29', NULL, 0),
(16, 1, '2025-07-16', '2025-07-30', '2025-08-02', 6.00),
(17, 2, '2025-07-17', '2025-07-31', '2025-07-31', 0),
(18, 3, '2025-07-18', '2025-08-01', NULL, 0),
(19, 4, '2025-07-19', '2025-08-02', NULL, 0),
(20, 5, '2025-07-20', '2025-08-03', NULL, 0),
(1, 6, '2025-07-21', '2025-08-04', NULL, 0),
(2, 7, '2025-07-22', '2025-08-05', NULL, 0),
(3, 8, '2025-07-23', '2025-08-06', NULL, 0),
(4, 9, '2025-07-24', '2025-08-07', NULL, 0),
(5, 10, '2025-07-25', '2025-08-08', NULL, 0);

-- Insert Reviews (12 records)
INSERT INTO Review (book_id, member_id, rating, comment)
VALUES
(1, 1, 4, 'Great introduction to physics'),
(2, 2, 5, 'Excellent chemistry content'),
(3, 3, 3, 'Good but too detailed'),
(4, 4, 4, 'Loved the art examples'),
(5, 5, 5, 'Very informative'),
(6, 6, 4, 'AI concepts explained well'),
(7, 7, 5, 'Best book for ML beginners'),
(8, 8, 4, 'Comprehensive coverage'),
(9, 9, 3, 'Basic psychology concepts'),
(10, 10, 4, 'Cultural insights were great'),
(11, 11, 5, 'Awesome creative writing tips'),
(12, 12, 4, 'Well-written history book');