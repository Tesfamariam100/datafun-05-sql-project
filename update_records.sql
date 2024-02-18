-- Update records in the authors table
UPDATE authors
SET author_name = ?, author_email = ?
WHERE author_id = ?;

-- Update records in the books table
UPDATE books
SET book_title = ?, book_genre = ?, book_published_date = ?
WHERE book_title = ?;
