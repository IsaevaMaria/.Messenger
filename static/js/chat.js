var current_page = 1;

function update_chat() {
	$.ajax('/get_messages/' + $('#chat_id').attr("value") + "/" + current_page, {
		success: function(data) {
			$('#messages').remove();
			let messages_str = "";
			data.messages.forEach(function(item, i, arr) {
				messages_str += "<p>" + item.text + ' - ' + item.date + "</p>";
			});
			messages_str = "<div id='messages'>" + messages_str + "</div>";
			$('#messages_box').append(messages_str);
		}
	});
}

$(document).ready(function() {
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