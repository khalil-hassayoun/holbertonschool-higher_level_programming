-- lists all cities of california found in database
SELECT id, name FROM cities
       WHERE state_id IN (SELECT id
       FROM states
       WHERE name = 'California')
