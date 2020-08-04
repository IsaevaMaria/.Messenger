function update_chat() {
	$.ajax('/get_messages/' + $('#chat_id').attr("value"), {
		success: function(data) {
			$('#messages').remove();
			let messages_str = "";
			data.messages.forEach(function(item, i, arr) {
				messages_str += "<p>" + item.text + ' - ' + item.date + "</p>";
			});
			messages_str = "<div id='messages'>" + messages_str + "</div>";
			console.log(messages_str);
			$('#messages_box').append(messages_str);
		}
	});
}

$(document).ready(function() {
	setInterval(update_chat, 500);

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