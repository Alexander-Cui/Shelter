
var location;
// document.addEventListener("onDocumentReady", getLocation)
function getStorageLocation(){
  // if (localStorage.getItem("location")){
  //   location = JSON.parse(localStorage.getItem("location"));
  // }
  // else{
  //   console.log("calling get location");
    location = getLocation();
  // }
}
getLocation();
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition); // passes position into function showPosition
  } 
  // else { 
  //   var x = document.getElementById("demo");
  //   x.innerHTML = "Geolocation is not supported by this browser.";
  // }
}

function showPosition(position) {
  let locationObject = {
    lat: position.coords.latitude,
    lng: position.coords.longitude
  }
  localStorage.setItem("location", JSON.stringify(locationObject));
  console.log(`location: ${JSON.stringify(locationObject)}`)

  getDistances(locationObject)

  return locationObject
}

function getDistances(location){
  console.log("here")
  let shelters = document.querySelectorAll(".card-body");
  console.log(shelters)
  let locations = []
  for (let i=0; i<shelters.length;i++){
    let lat = shelters[i].getElementsByClassName("lat")[0].innerHTML;
    let lng = shelters[i].getElementsByClassName("lng")[0].innerHTML;
    
    locations.push(
      {
        lat:lat,
        lng:lng
      }
    )

  } 

  callDistanceMatrix(location, locations)

}


async function callDistanceMatrix(origin, destinations){

    // let outputFormat = "json";
    // let params = {};
    // let parameters = toQuery(params);

    // let response = await fetch(`https://maps.googleapis.com/maps/api/distancematrix/${outputFormat}?${parameters}`,{

    // });
    console.log("i have been called");

    var origin1 = 'Greenwich, England';
    console.log(`this is origin: ${origin.lat} ${origin.lng}`)
    destinations = destinations.map( destination => {
      return new google.maps.LatLng(destination.lat, destination.lng)
    });

    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix(
    {
        origins: [{lat:45.4979085,lng:-73.6369607}],
        destinations: destinations,
        travelMode: 'WALKING',
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

