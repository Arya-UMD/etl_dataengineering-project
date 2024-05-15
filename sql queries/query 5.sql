-- Query 5 --

SELECT
  country,
  COUNT(*) AS players_count,
  ROUND((COUNT() * 100.0 / SUM(COUNT()) OVER ()), 2) AS percentage
FROM
  etl-dataengineering-project.cricket_dataset.icc_odi_batsman_ranking
GROUP BY
  country
ORDER BY
  percentage DESC;