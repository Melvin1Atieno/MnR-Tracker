// document ready function to prevent jQuery code from running before document is finished loading
$(document).ready(function(){
    $("button").click(function(){
        $(".navbar-item").css({"display":"block"})
    });
});