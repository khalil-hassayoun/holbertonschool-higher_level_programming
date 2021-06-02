-- lists all cities in the database, using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on states.id = cities.state_id
ORDER BY cities.id ASC;
