$(document).ready(function() {
    // Scroll to end of chatbox on page load
    $('.chatbox').scrollTop($('.chatbox')[0].scrollHeight);
    
    $('#message-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/chat/',
            data: $('#message-form').serialize(),
            success: function(response) {
                $('.chatbox').append('<div class="user-message">' + response.user_message + '</div>');
                $('.chatbox').append('<div class="bot-message">' + response.bot_response + '</div>');
                
                // Scroll to end of chatbox after new message is added
                $('.chatbox').scrollTop($('.chatbox')[0].scrollHeight);
            },
            error: function(response) {
                alert('Error sending message.');
            }
        });
        $('#message-form')[0].reset();
    });
});
