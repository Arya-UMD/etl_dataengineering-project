-- Query 4 --

WITH FirstIPLPoint AS (
  SELECT *
  FROM etl-dataengineering-project.cricket_dataset.ipl_points_table
  ORDER BY points DESC  -- Assuming there's a 'points' column to sort by
  LIMIT 1
),
FirstICCRanking AS (
  SELECT *
  FROM etl-dataengineering-project.cricket_dataset.icc_odi_batsman_ranking
  ORDER BY rank
  LIMIT 1
),
FirstIPLBatting AS (
  SELECT *
  FROM etl-dataengineering-project.cricket_dataset.ipl_batting_stat
  ORDER BY runs DESC  -- Assuming there's a 'runs' column to sort by
  LIMIT 1
)

SELECT
  p.teamFullName AS ipl_team,
  p.points AS ipl_points,
  r.name AS batsman_name,
  r.rank AS icc_rank,
  b.batter AS top_scorer,
  b.runs AS highest_runs
FROM FirstIPLPoint p
CROSS JOIN FirstICCRanking r
CROSS JOIN FirstIPLBatting b;