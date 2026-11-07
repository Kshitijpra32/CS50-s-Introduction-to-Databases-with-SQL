-- Find the 10 least expensive players per hit in 2001
SELECT p1.first_name, p1.last_name
FROM players p1
WHERE p1.id IN (
    SELECT players.id
    FROM players
    JOIN salaries
        ON players.id = salaries.player_id
    JOIN performances
        ON players.id = performances.player_id
        AND salaries.team_id = performances.team_id
        AND salaries.year = performances.year
    WHERE salaries.year = 2001
      AND performances.H > 0
    ORDER BY (salaries.salary * 1.0 / performances.H) ASC
    LIMIT 10
)
AND p1.id IN (
    SELECT players.id
    FROM players
    JOIN salaries
        ON players.id = salaries.player_id
    JOIN performances
        ON players.id = performances.player_id
        AND salaries.team_id = performances.team_id
        AND salaries.year = performances.year
    WHERE salaries.year = 2001
      AND performances.RBI > 0
    ORDER BY (salaries.salary * 1.0 / performances.RBI) ASC
    LIMIT 10
)
ORDER BY p1.id ASC;
