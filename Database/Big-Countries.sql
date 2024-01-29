SELECT
    name,
    population,
    area
FROM
    World
WHERE 
    Area >= 3000000

union

SELECT
    name,
    population,
    area
FROM
    World
WHERE 
    population >= 25000000
