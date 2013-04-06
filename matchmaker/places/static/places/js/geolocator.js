function error(msg) {
    if (msg.hasOwnProperty('code')) {
        if (msg.code == 1) {
            fallback()
        }
    } else {
        console.log(msg);
    }
}

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
} else {
    error('Geolocation not supported')
}
