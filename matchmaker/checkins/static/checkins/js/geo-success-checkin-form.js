function update_latlng(lat, lng) {
    $('#id_lat').val(lat);
    $('#id_lng').val(lng);
}

function success(position) {
    update_latlng(position.coords.latitude, position.coords.longitude);
    $('.btn-primary').prop('disabled', false);
    $('.btn-primary').val('Check-in');
}
