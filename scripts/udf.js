function icc_ranking(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.rank = values[0];
    obj.name = values[1];
    obj.country = values[2];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }


function ipl_points_table(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.matchesPlayed = values[0];
    obj.matchesWon = values[1];
    obj.matchesLost = values[2];
    obj.points = values[3];
    obj.nrr = values[4];
    obj.teamFullName = values[5].trim(); // Remove leading/trailing spaces
    var jsonString = JSON.stringify(obj);
    return jsonString;
}


function ipl_batting_stats(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.batter = values[1];
    obj.matches = values[2];
    obj.innings = values[3];
    obj.runs = values[4];
    obj.avg = values[5];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}