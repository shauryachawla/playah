// set up a new XMLHttpRequest variable
var request = false;
try {
    request = new XMLHttpRequest();
} catch (trymicrosoft) {
    try {
        request = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (othermicrosoft) {
        try {
            request = new ActiveXObject("Microsoft.XMLHTTP");
        } catch (failed) {
            request = false;
        }
    }
}
 
if (!request)
    alert("Error initializing XMLHttpRequest!");
 
function getAlbum() {
    var artistSelect = document.getElementById("id_artist");
	var artistName = artistSelect.options[artistSelect.selectedIndex].text;
    var url = "http://localhost:8000/app/add_song/?artist_name=" + escape(artistName);
    request.open("GET", url, true);
    request.onreadystatechange = updatePage;
    request.send(null);
} 
 
// what to do when http ready state changes
function updatePage() { 
    if (request.readyState == 4) {
        if (request.status == 200) {
  
            // get response array
            var data = JSON.parse(request.responseText); 
            update_select($('select[name=album]'), data);
        }  
        // some error checking
        else if (request.status == 404) {
            alert("Request url does not exist");
        }
        else {
            alert("Error: status code is " + request.status);
        }
    }
}   
 
function update_select(select, data) {
    select.find('option').remove();
    for (var k in data) {
        select.append($('<option value="'+data[k].id+'">'+data[k].title+'</option>'));
    }
}