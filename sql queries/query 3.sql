-- Query 3 --

WITH avg_runs_all AS (
    SELECT AVG(runs) AS avg_runs_all FROM etl-dataengineering-project.cricket_dataset.ipl_batting_stat
),
avg_avg_all AS (
    SELECT AVG(avg) AS avg_avg_all FROM etl-dataengineering-project.cricket_dataset.ipl_batting_stat
),
top_5_batsmen AS (
    SELECT batter, runs, avg FROM etl-dataengineering-project.cricket_dataset.ipl_batting_stat
    ORDER BY runs DESC
    LIMIT 5
)

SELECT
    t.batter AS name,
    ROUND(t.runs, 2) AS runs,
    ROUND(a.avg_runs_all, 2) AS average runs by all batsman,
    ROUND(t.avg, 2) AS average,
    ROUND(b.avg_avg_all, 2) AS average of all batsman
FROM
    top_5_batsmen t,
    avg_runs_all a,
    avg_avg_all b;