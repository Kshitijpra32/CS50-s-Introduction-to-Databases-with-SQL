SELECT title, season, air_date, topic
FROM episodes
WHERE (season = 2 OR season = 3)
AND air_date > '2003-01-01';
