$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        getSQL();
    });
});


// call Flask API endpoint
function getSQL() {
    var group = $("#group").val();
    var team = $("#team1").val();
 
    // check if inputs are valid

    // create the payload
    var payload = {
        "group": group,
        "team": team
    }
    console.log(payload)
    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/getSQL",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            renderTable(returnedData);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

function renderTable(inp_data) {
    // init html string
    let html = "";

    // destroy datatable
    $('#sql_table').DataTable().clear().destroy();

    // loop through all rows
    inp_data.forEach(function(row) {
        html += "<tr>";

        // loop through each cell (order matters)
        html += `<td>${row.index}</td>`;
        html += `<td>${row.match}</td>`;
        html += `<td>${row.s1_key}</td>`;
        html += `<td>${row.s2_key}</td>`;
        html += `<td>${row.group}</td>`;
        html += `<td>${row.stage}</td>`;
        html += `<td>${row.squad1}</td>`;
        html += `<td>${row.s1_perc}</td>`;
        html += `<td>${row.squad1_seed}</td>`;
        html += `<td>${row.squad2}</td>`;
        html += `<td>${row.s2_perc}</td>`;
        html += `<td>${row.squad2_seed}</td>`;
        html += `<td>${row.s1_prob}</td>`;        
        html += `<td>${row.s1_wins}</td>`;
        html += `<td>${row.simulation}</td>`; 
        html += `<td>${row.match_winner}</td>`;

        // close the row
        html += "</tr>";
    });

    // shove the html in our elements
    console.log(html);
    $("#sql_table tbody").html("");
    $("#sql_table tbody").append(html);

    // remake data table
    $('#sql_table').DataTable();
}