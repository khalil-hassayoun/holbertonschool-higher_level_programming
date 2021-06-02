-- displays top 3 cities avg_tmp for given months
SELECT city, AVG(value) AS avg_temp FROM temperatures
       WHERE month=7 or month=8
       GROUP BY city
       ORDER BY avg_temp DESC
       LIMIT 3;
