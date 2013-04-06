function set_token(token) {
    FB.api('/me/permissions', function (response) {
        var perms = response.data[0];
        if (perms.publish_stream) {
            $('#id_access_token').val(token);
        }
    });
}


window.fbAsyncInit = function() {
    $('.iPhoneCheckHandle').click(function() {
        if (!$('#id_access_token').val()) {
            FB.login(function(response) {
                if (response.status === 'connected') {
                    set_token(response.authResponse.authToken);
                }
            }, {scope: 'publish_stream'});
        }
    });

    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            set_token(response.authResponse.accessToken);
        }
    });
};
