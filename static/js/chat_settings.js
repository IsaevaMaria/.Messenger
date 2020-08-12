function rename_click_event(){
    $('#rename_form').show();
    $('#new_name').val("");
    $('#rename_chat').hide();
}

function cancel_click_event(){
    $('#rename_form').hide();
    $('#new_name').val("");
    $('#rename_chat').show();
}

$(document).ready(function(){
    $("#submit_rename").on('click', function(){
        $.ajax('/rename_chat/' + $('#chat_id').attr("value"),
        {
            data: {
                new_name: $('#new_name').val()
            },
            type: 'post',
            success: function(data) {
                $('#chat_name').html("Беседа " + $('#new_name').val());
                cancel_click_event();
            }
        });
    });
    $("#cancel").on('click', cancel_click_event);

    $("#rename_chat").on("click", rename_click_event);
});