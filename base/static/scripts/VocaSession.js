$(document).ready(function(){
    $('.action').hover(function(){
        $(this).addClass('darken-2').removeClass('darken-4');
    }).mouseleave(function(){
        $(this).addClass('darken-4').removeClass('darken-2');
    });
    $('.add_to_list').hover(function(){
        $(this).removeClass('light-blue');
    }).mouseleave(function(){
        $(this).addClass('light-blue');
    });
    $('#logout_btn_mobile').hover(function(){
        $(this).removeClass('transparent').addClass('red');
    }).mouseleave(function(){
        $(this).removeClass('red').addClass('transparent');
    });
});