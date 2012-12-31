function getURLParameter(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
}

function success(position) {
    var filter = getURLParameter('filter');
    console.log(filter);
    $.post(
        '/places/'
        ,{
            lat: position.coords.latitude
            ,lng: position.coords.longitude
            ,filter: filter
        }
        ,function(data) {
            $('#placeList').html(data);
        }
    );
}
