
$(document).ready(function(){
            
    $("#form").submit(function(e){

        e.preventDefault()

        textinlivebox = $("#livebox").val();

        $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:textinlivebox},
            success: function(res){

                if (res["gresult"] == true) {
                    response(res)
                    initMap(res)
                }
                else {
                    $("#result_name").html("Désolé je n'ai pas de réponse.");
                }

                if (res["wresult"] == true) {
                    wikiResponse(res)
                }
                else {
                    $("#result_wiki").html("Désolé, je n'ai pas trouvé d'histoire intéressante à raconter...");
                }                

            }
        })
    });

})

function response(res) {
    $("#result_query").html(res["query"]);
    $("#result_name").html(res["ginfos"]["name"]);
    $("#result_address").html(res["ginfos"]["formatted_address"]);
}

function wikiResponse(res) {
    $("#result_wiki_title").html(res["wtitle"]);
    $("#result_wiki_text").html(res["wtext"]);
}

function initMap(res) {
    const target = { lat: res["gcoord_lat"], lng: res["gcoord_lng"] };

    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: target,
    });

    const marker = new google.maps.Marker({
    position: target,
    map: map,
    });
}