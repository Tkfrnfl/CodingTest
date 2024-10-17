SELECT BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME,DATE_FORMAT(BOOK.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK
JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE BOOK.CATEGORY ='경제'
ORDER BY BOOK.PUBLISHED_DATE ASC