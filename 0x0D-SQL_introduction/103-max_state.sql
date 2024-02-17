-- From imported temperatures db, this script that displays the max 
  -- temperature of each state (ordered by State name)
SELECT state MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3
ORDER BY state ASC;
