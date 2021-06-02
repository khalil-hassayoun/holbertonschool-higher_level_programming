-- displays all entries from second_table with a name
SELECT score, name FROM second_table WHERE (name IS NOT NULL AND name != '') ORDER BY score DESC;
