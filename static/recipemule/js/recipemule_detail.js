$(document).ready(function(){

	$.fn.select2.defaults.set("theme", "classic");

    $('#button_toggle1').click(function(){
        $("#toggle1").toggle();
    });

    $('#button_toggle2').click(function(){
        $("#toggle2").toggle();
    });
    
	$('#button_toggle3').click(function(){
        $("#toggle3").toggle();
    });
});
