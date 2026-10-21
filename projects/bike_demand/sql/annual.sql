SELECT yr + 2011 AS year, COUNT(*) AS days, SUM(cnt) AS rentals,
       ROUND(AVG(cnt), 2) AS mean_daily_rentals,
       ROUND(100.0 * SUM(casual) / SUM(cnt), 2) AS casual_share_pct
FROM daily_rentals GROUP BY yr ORDER BY yr;
