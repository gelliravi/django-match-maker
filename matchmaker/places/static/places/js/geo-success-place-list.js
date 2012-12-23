function success(position) {
    $.post('/places/', {lat: position.coords.latitude, lng: position.coords.longitude}, function(data) {
        $('#placeList').html(data); 
    });
}
