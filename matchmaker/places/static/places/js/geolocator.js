function update_latlng(lat, lng) {
    $('#id_lat').val(lat);
    $('#id_lng').val(lng);
}

function success(position) {
    update_latlng(position.coords.latitude, position.coords.longitude);

    var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    var myOptions = {
        zoom: 15,
        center: latlng,
        mapTypeControl: true,
        navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var mapcanvas = document.getElementById("mapCanvas")
    var map = new google.maps.Map(mapcanvas, myOptions);

    var marker = new google.maps.Marker({
        position: latlng,
        draggable: true,
        map: map,
        title:"You are here! (at least within a "+position.coords.accuracy+" meter radius)"
    });

    google.maps.event.addListener(marker,'dragend',function(){
        update_latlng(marker.position.lat(), marker.position.lng());
    });
}


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
