-- Descriptive association, not a causal effect or demand forecast.
SELECT yr + 2011 AS year, weathersit AS weather_code, COUNT(*) AS days,
       ROUND(AVG(cnt), 2) AS mean_daily_rentals
FROM daily_rentals
GROUP BY yr, weathersit ORDER BY yr, weathersit;
