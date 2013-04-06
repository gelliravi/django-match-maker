function disable_button() {
    $('.btn-primary').prop('disabled', true);
    $('.btn-primary').val('Checking permissions...');
}


function enable_button() {
    $('.btn-primary').prop('disabled', false);
    $('.btn-primary').val('Check-in');
}


function set_token(token) {
    if (!token) {
        FB.getLoginStatus(function(response) {
            if (response.status === 'connected') {
                $('#id_access_token').val(response.authResponse.accessToken);
                enable_button();
            }
        });
    } else {
        $('#id_access_token').val(token);
        enable_button();
    }
}


function has_permission() {
    FB.api('/me/permissions', function (response) {
        var perms = response.data[0];
        if (perms.publish_stream) {
            return true;
        }
        return false;
    });
}


window.fbAsyncInit = function() {
    $(':checkbox').click(function() {
        is_checked = $('#id_post_to_facebook').prop('checked');
        disable_button();
        if (is_checked) {
            if (!$('#id_access_token').val()) {
                FB.login(function(response) {
                    if (response.status === 'connected') {
                        set_token();
                    }
                }, {scope: 'publish_stream'});
            } else {
                enable_button();
            }
        } else {
            enable_button();
        }
    });
};
