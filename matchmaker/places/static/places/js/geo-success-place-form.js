function update_latlng(lat, lng) {
    $('#id_lat').val(lat);
    $('#id_lng').val(lng);
}

function SubmitControl(controlDiv, map) {

  // Set CSS styles for the DIV containing the control
  // Setting padding to 5 px will offset the control
  // from the edge of the map.
  controlDiv.style.padding = '5px';

  // Set CSS for the control border.
  var controlUI = document.createElement('div');
  controlUI.style.backgroundColor = 'white';
  controlUI.style.borderStyle = 'solid';
  controlUI.style.borderWidth = '2px';
  controlUI.style.cursor = 'pointer';
  controlUI.style.textAlign = 'center';
  controlUI.title = 'Click to select this position.';
  controlDiv.appendChild(controlUI);

  // Set CSS for the control interior.
  var controlText = document.createElement('div');
  controlText.style.fontFamily = 'Arial,sans-serif';
  controlText.style.fontSize = '12px';
  controlText.style.paddingLeft = '4px';
  controlText.style.paddingRight = '4px';
  controlText.innerHTML = '<strong>Select this position</strong>';
  controlUI.appendChild(controlText);

  google.maps.event.addDomListener(controlUI, 'click', function() {
      $('#mapCanvas').hide();
  });
}

function show_map(position) {
    var lat = $('#id_lat').val();
    var lng = $('#id_lng').val();
    var latlng = new google.maps.LatLng(lat, lng);
    var myOptions = {
        zoom: 19
        ,center: latlng
        ,mapTypeControl: true
        ,navigationControlOptions: {
            style: google.maps.NavigationControlStyle.SMALL
        }
        ,mapTypeId: google.maps.MapTypeId.ROADMAP
        ,streetViewControl: false
        ,zoomControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        }
        ,mapTypeControlOptions: {
            position: google.maps.ControlPosition.LEFT_CENTER
        }
    };

    var mapcanvas = document.getElementById("mapCanvas")
    var map = new google.maps.Map(mapcanvas, myOptions);

    var submitControlDiv = document.createElement('div');
    var submitControl = new SubmitControl(submitControlDiv, map);
    submitControlDiv.index = 1;
    map.controls[google.maps.ControlPosition.LEFT_CENTER].push(submitControlDiv);

    var marker = new google.maps.Marker({
        position: latlng
        ,draggable: true
        ,map: map
        ,title:"You are here!"
    });

    google.maps.event.addListener(marker,'dragend',function(){
        update_latlng(marker.position.lat(), marker.position.lng());
    });

    $('body').scrollTop(0);
    $('#mapCanvas').show();
    google.maps.event.trigger(map, 'resize');
    map.setCenter(latlng);
}

function success(position) {
    update_latlng(position.coords.latitude, position.coords.longitude);

    var $btn = $('#btnPickPosition')
    $btn.html('Pick position');
    $btn.click(function() {
        show_map();
    });

    $('.btn-primary').prop('disabled', false);
    $('.btn-primary').val('Create  place');
}
