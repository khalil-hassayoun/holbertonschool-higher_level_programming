-- displays max temp per state from date
SELECT state, MAX(value) AS max_temp FROM temperatures 
       GROUP BY state
       ORDER BY state;
