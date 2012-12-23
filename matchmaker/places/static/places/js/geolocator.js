function error(msg) {
    var s = document.querySelector('#status');
    s.innerHTML = typeof msg == 'string' ? msg : "failed";
    s.className = 'fail';
}


if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
} else {
    error('not supported');
}
