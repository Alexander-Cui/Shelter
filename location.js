function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition); // passes position into function showPosition
    } else { 
      var x = document.getElementById("demo");
      x.innerHTML = "Geolocation is not supported by this browser.";
    }
  }
  
  function showPosition(position) {
      var x = document.getElementById("demo");
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
  }
  
  async function callDistanceMatrix(){
  
      // let outputFormat = "json";
      // let params = {};
      // let parameters = toQuery(params);
  
      // let response = await fetch(`https://maps.googleapis.com/maps/api/distancematrix/${outputFormat}?${parameters}`,{
  
      // });
      console.log("i have been called");
      var origin1 = new google.maps.LatLng(55.930385, -3.118425);
      var origin2 = 'Greenwich, England';
      var destinationA = 'Stockholm, Sweden';
      var destinationB = new google.maps.LatLng(50.087692, 14.421150);
  
      var service = new google.maps.DistanceMatrixService();
      service.getDistanceMatrix(
      {
          origins: [origin1, origin2],
          destinations: [destinationA, destinationB],
          travelMode: 'DRIVING',
          // transitOptions: TransitOptions,
          // drivingOptions: DrivingOptions,
          // unitSystem: UnitSystem,
          // avoidHighways: Boolean,
          // avoidTolls: Boolean,
      }, callback);
  
  }
  function callback(response, status) {
      console.log(response);
      // See Parsing the Results for
      // the basics of a callback function.
    }
  
  function toQuery(params){
  
      return Object.keys(params).map(key => key + '=' + params[key]).join('&');
  }