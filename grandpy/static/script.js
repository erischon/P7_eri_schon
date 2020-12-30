
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
                }
                else {
                    $("#result_name").html("Désolé je n'ai pas de réponse.");
                }

                if (res["wresult"] == true) {
                    wikiResponse(res)
                }
                else {
                    $("#result_wiki").html("Désolé je n'ai pas de réponse.");
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
    $("#result_wiki").html(res["wtext"]);
}