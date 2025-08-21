-- Books with their authors and categories
SELECT b.title, GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name)) AS authors,GROUP_CONCAT(DISTINCT c.name) AS categories
FROM Book b
JOIN Book_Author ba ON b.book_id = ba.book_id    -- use join operation between different tables
JOIN Author a ON ba.author_id = a.author_id
JOIN Book_Category bc ON b.book_id = bc.book_id
JOIN Category c ON bc.category_id = c.category_id
GROUP BY b.book_id;

-- Most borrowed books in the last 30 days
SELECT b.title, COUNT(br.borrowing_id) AS borrow_count   --use aggregate function Count
FROM Borrowing br
JOIN Book b ON br.book_id = b.book_id
WHERE br.borrow_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY b.book_id
ORDER BY borrow_count DESC
LIMIT 5;

-- Members with overdue books and calculated late fees
SELECT m.first_name, m.last_name, b.title, br.due_date,
       DATEDIFF(CURDATE(), br.due_date) AS overdue_days,
       (CASE WHEN DATEDIFF(CURDATE(), br.due_date) > 0 THEN DATEDIFF(CURDATE(), br.due_date)*2 ELSE 0 END) AS calculated_late_fee
FROM Borrowing br
JOIN Member m ON br.member_id = m.member_id
JOIN Book b ON br.book_id = b.book_id
WHERE br.return_date IS NULL AND br.due_date < CURDATE();

-- Average rating per book with author information
SELECT b.title, AVG(r.rating) AS avg_rating,GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name)) AS authors
FROM Review r
JOIN Book b ON r.book_id = b.book_id
JOIN Book_Author ba ON b.book_id = ba.book_id
JOIN Author a ON ba.author_id = a.author_id
GROUP BY b.book_id
ORDER BY avg_rating DESC;

-- Books available in each library with stock levels
SELECT l.name AS library_name, b.title, b.total_copies, b.available_copies
FROM Library l
JOIN Book b ON l.library_id = b.library_id
ORDER BY l.name, b.title;

-- Window Function: Rank most borrowed books
SELECT b.title, COUNT(br.borrowing_id) AS borrow_count,RANK() OVER (ORDER BY COUNT(br.borrowing_id) DESC) AS rank_position
FROM Borrowing br
JOIN Book b ON br.book_id = b.book_id
GROUP BY b.book_id;

-- CTE: Top 3 most active members
WITH BorrowCount AS (
    SELECT member_id, COUNT(*) AS borrow_count
    FROM Borrowing
    GROUP BY member_id
)
SELECT m.first_name, m.last_name, bc.borrow_count
FROM BorrowCount bc
JOIN Member m ON bc.member_id = m.member_id
ORDER BY bc.borrow_count DESC
LIMIT 3;

-- Transaction: Borrow a book and update available copies
START TRANSACTION;
INSERT INTO Borrowing (member_id, book_id, borrow_date, due_date, late_fee)
VALUES (1, 6, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), 0);
UPDATE Book SET available_copies = available_copies - 1 WHERE book_id = 6;
COMMIT;
