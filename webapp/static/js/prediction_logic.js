$(document).ready(function() {
    console.log("Page Loaded");

    $("#predict").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    var team1 = $("#team1").val();
    var team2 = $("#team2").val();

    // check if inputs are valid

    // create the payload
    var payload = {
        "team1": team1,
        "team2": team2
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
            let pred = returnedData.prediction;
            $("#results").text(pred);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}