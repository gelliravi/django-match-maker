function getURLParameter(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
}


function post_request(lat, lng) {
    var filter = getURLParameter('filter');
    $.post(
        '/places/'
        ,{
            lat: lat
            ,lng: lng
            ,filter: filter
        }
        ,function(data) {
            $('#placeList').html(data);
        }
    );
}


function fallback() {
    post_request('', '');
}


function success(position) {
    post_request(position.coords.latitude, position.coords.longitude);
}
