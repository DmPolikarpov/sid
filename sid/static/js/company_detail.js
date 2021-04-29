/*hide the content of the tabs, activate the first tab and show the first tab's content*/
$(document).ready(function() {
    $("#content div").hide();
    $("#tabs li:first").attr("id","current");
    $("#content div:first").fadeIn();
    $(".profile").fadeIn();
    $(".logo").fadeIn();
/*processing a tab click action*/
    $('#tabs a').click(function(e) {
        e.preventDefault();
        $("#content div").hide();
        $("#tabs li").attr("id","");
        $(this).parent().attr("id","current");
        $('#' + $(this).attr('title')).fadeIn();
        $(".profile").fadeIn();
        $(".logo").fadeIn();
        $(".canvas").fadeIn();
        $(".script").fadeIn();
        $("#tab2 div").fadeIn();
        $("#tab3 div").fadeIn();
    });
});





