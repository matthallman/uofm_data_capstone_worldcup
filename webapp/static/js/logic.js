$(document).ready(function() {
    console.log("Page Loaded");
    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});
// call Flask API endpoint
function makePredictions() {
    var index = $("#index").val();
    var match = $("#match").val();
    var squad_1_key = $("#squad1key").val();
    var squad_2_key = $("#squad2key").val();
    var group = $("#group").val();
    var stage = $("#stage").val();
    var squad_1 = $("#squad1").val();
    var s1% = $("#s1%").val();
    var squad_1_seed = $("#squad1seed").val();
    var squad_2 = $("#squad2").val();
    var s2% = $("#s2%").val();
    var squad_2_seed = $("#squad2seed").val();
    var s1_prob = $("#s1prob").val();
    var s1_wins = $("#s1wins").val();
    var simulation = $("#simulation").val();
    var match_winner = $("#matchwinner").val();
    // check if inputs are valid
    // create the payload
    var payload = {
        "index": index,
        "match": match,
        "squad 1 key": squad_1_key,
        "squad 2 key": squad_2_key,
        "group": group,
        "stage": stage,
        "squad 1": squad_1,
        "s1%": s1%,
        "squad 1 seed": squad_1_seed,
        "squad 2": squad_2,
        "s2%": s2%,
        "squad 2 seed": squad_2_seed,
        "s1_prob": s1_prob,
        "s1_wins": s1_wins,
        "simulation": simulation,
        "match winner": match_winner
    }
    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });
}