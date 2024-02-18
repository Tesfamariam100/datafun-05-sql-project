-- Query to get the count of books by genre
SELECT book_genre, COUNT(*) AS total_books FROM books GROUP BY book_genre;

-- Query to get the count of authors by country
SELECT author_country, COUNT(*) AS total_authors FROM authors GROUP BY author_country;
