$(document).ready(function() {

	$("#send_message").on("submit", function(event) {

		$.ajax({
			data : {
				text: $("#text_input").val()
			},
			type: 'POST',
			url: '/send'
		})
		.done(function(data) {

			if (data.error) {
				$('#error').text(data.error);
				$('#send_text').text("");
			}
			else {
				$('#error').text("");
				$('#send_text').text(data.text);
			}

		});

		event.preventDefault();

	});

});