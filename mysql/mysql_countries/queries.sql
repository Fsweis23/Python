SELECT name, language, percentage FROM countries
JOIN languages ON languages.country_id = countries.id
ORDER BY percentage desc

SELECT c.name, COUNT(cities.id) FROM countries c
JOIN cities ON cities.country_id = c.id
GROUP BY c.id
ORDER BY COUNT(cities.id) desc

SELECT cities.name, cities.population 
FROM cities 
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'mexico' AND cities.population > 500000
ORDER BY cities.population desc

SELECT countries.name, languages.percentage 
FROM countries
JOIN languages ON countries.code = languages.country_code 
WHERE languages.percentage > 89
ORDER BY languages.percentage desc

SELECT name, surface_area, population 
FROM countries 
WHERE surface_area < 501 AND population > 100000

SELECT name, government_form, capital, life_expectancy
FROM countries 
WHERE government_form = 'constitutional monarchy' AND capital > 200 AND life_expectancy > 75

SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population 
FROM cities 
JOIN countries ON cities.country_id = countries.id 
WHERE countries.name = 'argentina' AND cities.district = 'buenos aires' AND cities.population > 500000

SELECT region, COUNT(id) AS number_countries
FROM countries
GROUP BY region 
ORDER BY COUNT(id) desc