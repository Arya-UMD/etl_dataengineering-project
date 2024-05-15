-- Query 2 --

WITH TopIPLScorers AS (
  SELECT
    batter,
    SUM(runs) AS runs_scored_in_ipl
  FROM
    etl-dataengineering-project.cricket_dataset.ipl_batting_stat
  GROUP BY
    batter
  ORDER BY
    runs_scored_in_ipl DESC
  LIMIT 10
)

SELECT
  r.rank AS odi_rank,
  ROW_NUMBER() OVER (ORDER BY t.runs_scored_in_ipl DESC) AS ipl_rank,
  t.batter AS name,
  r.country,
  t.runs_scored_in_ipl
FROM
  TopIPLScorers t
JOIN
  etl-dataengineering-project.cricket_dataset.icc_odi_batsman_ranking r
ON TRIM(LOWER(SPLIT(r.name, ' ')[OFFSET(1)])) = TRIM(LOWER(t.batter))
ORDER BY
  t.runs_scored_in_ipl DESC;