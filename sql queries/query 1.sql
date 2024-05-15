-- Query 1 --

SELECT 
    teamFullName,
    matchesPlayed,
    matchesWon,
    matchesLost,
    points,
    nrr,
    IF((14 - matchesPlayed + matchesWon) < 8, 'Yes', 'No') AS eliminated_or_not,
    IF((14 - matchesPlayed + matchesWon) < 8, 0, GREATEST(0, 8 - matchesWon)) AS number_of_wins_required
FROM 
    etl-dataengineering-project.cricket_dataset.ipl_points_table
ORDER BY 
    points DESC, nrr DESC;