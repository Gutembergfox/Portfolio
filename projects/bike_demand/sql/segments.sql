-- Segment within year to avoid pooling the large 2011-to-2012 shift.
SELECT yr + 2011 AS year,
       CASE workingday WHEN 1 THEN 'working day' ELSE 'weekend/holiday' END AS day_type,
       COUNT(*) AS days,
       ROUND(AVG(cnt), 2) AS mean_daily_rentals,
       ROUND(AVG(casual), 2) AS mean_casual,
       ROUND(AVG(registered), 2) AS mean_registered,
       ROUND(100.0 * SUM(casual) / SUM(cnt), 2) AS casual_share_pct
FROM daily_rentals
GROUP BY yr, workingday ORDER BY yr, workingday;
