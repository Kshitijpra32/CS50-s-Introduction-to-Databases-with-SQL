-- 10.sql
SELECT
    english_title AS "Print Title",
    artist AS "Artist Name",
    brightness AS "Image Brightness"
FROM views
WHERE brightness > 0.6
ORDER BY brightness DESC;
