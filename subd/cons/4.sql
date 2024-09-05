CREATE INDEX idx_flights_flight_id_status ON flights(flight_id) INCLUDE (status);

EXPLAIN ANALYZE SELECT flight_id, status FROM flights WHERE flight_id = 1;

-- Получение информации о текущем первичном ключе
SELECT conname, conrelid::regclass, conkey 
FROM pg_constraint 
WHERE contype = 'p' AND conrelid = 'flights'::regclass;

ALTER TABLE flights DROP CONSTRAINT flights_pkey;


CREATE UNIQUE INDEX flights_pkey_new ON flights(flight_id) INCLUDE (status);


ALTER TABLE flights ADD CONSTRAINT flights_pkey PRIMARY KEY USING INDEX flights_pkey_new;


EXPLAIN ANALYZE SELECT flight_id, status FROM flights WHERE flight_id = 1;


