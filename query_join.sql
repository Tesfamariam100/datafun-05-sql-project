-- Query to retrieve books with their corresponding authors
SELECT b.book_title, b.book_genre, b.book_published_date, a.author_name
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id;
