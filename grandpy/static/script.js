
$(document).ready(function(){
            
    $("#form").submit(function(e){
        event.preventDefault(); //prevent default action

        textinlivebox = $("#livebox").val();
        
        $.ajax({
            method:"post",
            url:"/livesearch",
            data:{text:textinlivebox},
            success: function(res){
                $("#result_query").html(res["query"]);
                $("#result_name").html(res["ginfos"]["name"]);
                $("#result_adress").html(res["ginfos"]["formatted_address"]);
                $("#result_wiki").html(res["wresult"]);
               console.log(res["wresult"]);
            }
        })
    });

})