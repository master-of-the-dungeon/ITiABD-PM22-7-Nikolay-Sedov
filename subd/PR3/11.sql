SELECT DISTINCT ON (book_ref) book_ref, ticket_no
FROM tickets
ORDER BY book_ref, ticket_no;


SELECT book_ref, MIN(ticket_no) AS min_ticket_no
FROM tickets
GROUP BY book_ref;


