var current_page = 1;

function prepare_to_update() {
    for(let i = 0; i < 10; i++) {
        $('#delete_message_' + i).hide();
        $('.message_' + i).remove();
    }
}

function update_chat() {

	$.ajax('/get_messages/' + $('#chat_id').attr("value") + "/" + current_page, {
		success: function(data) {
			prepare_to_update();
			data.messages.forEach(function(item, i, arr) {
				$("#message_" + i).append("<p class='message_" + i + "'>" + item.text + ' - ' + item.date + "</p>");
				$('#delete_message_' + i).attr("value", item.id);
				$('#delete_message_' + i).show();
			});
		}
	});

}

$(document).ready(function() {

    for (let i = 0; i < 10; i++) {
            $('#messages').append("<div id='message_" + i + "'><button id='delete_message_" + i + "' value=-1>Удалить</button></div>");
            $('#delete_message_' + i).hide();
			$('#delete_message_' + i).on('click', function(){
			    let message_id = $('#delete_message_' + i).attr("value");
			    $('#delete_message_' + i).hide();
			    $.ajax('/delete_message', {
			        data: {'message_id': message_id},
			        type: 'delete'
			    });
			});
    }

    update_chat();
	setInterval(update_chat, 500);
	$('#next').on('click', function() {
	    if (current_page > 1) { current_page--; }
	});
	$('#previous').on('click', function() {
	    current_page++;
	});
	$("#send_message").on("submit", function(event) {
		$.ajax('/send/' + $('#chat_id').attr("value"), {
			data : {
				text: $("#text_input").val()
			},
			type: 'post',
			success: function(data) {
				if (data.error) {
					$('#error').text(data.error);
				}
			}
		});
		event.preventDefault();
	});
});