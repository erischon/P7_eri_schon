$(document).ready(function(){
            
    $("#form").submit(function(e){

        textinlivebox = $("#livebox").val();

        $.ajaxSetup({ cache: false });
        $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:textinlivebox},
            success: function(res){
               response(res);
            }
        })
    });

})

function response(res) {
    $("#result_query").html("votre question : ", res["query"]);
    $("#result_name").html(res["ginfos"]["name"]);
    $("#result_address").html(res["ginfos"]["formatted_address"]);
    $("#result_wiki").html(res["wtext"]);
}
