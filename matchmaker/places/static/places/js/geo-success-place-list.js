function getURLParameter(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
}


function get_request(lat, lng) {
    var filter = getURLParameter('filter');
    $.get(
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
    get_request('', '');
}


function success(position) {
    get_request(position.coords.latitude, position.coords.longitude);
}
