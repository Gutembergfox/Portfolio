-- Compare mean rentals/day, not monthly totals with unequal day counts.
SELECT substr(dteday, 1, 7) AS month, COUNT(*) AS days,
       SUM(cnt) AS rentals, ROUND(AVG(cnt), 2) AS mean_daily_rentals
FROM daily_rentals
GROUP BY month ORDER BY month;
