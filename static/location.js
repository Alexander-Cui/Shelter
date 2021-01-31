
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

var present = document.getElementById("load");
if(present){
  getLocation();
}
else{
  console.log("not",present)
}

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
    let name = shelters[i].getElementsByClassName("name")[0].innerHTML;
    console.log(name)
    locations.push(
      {
        name:name,
        lat:lat,
        lng:lng
      }
    )

  } 

  callDistanceMatrix(location, locations)

}

function compare(a, b) {
  if (a.duration < b.duration) {
    return -1;
  }
  if (a.duration > b.duration) {
    return 1;
  }
  // a must be equal to b
  return 0;
}

async function callDistanceMatrix(origin, destinationList){
    let destinations = destinationList.map( destination => {
      return new google.maps.LatLng(destination.lat, destination.lng)
    });

    async function callback(response, status) {


      let shelterInfo = response.rows[0]['elements'].map((distance,idx) =>{
        let info = {
          name:destinationList[idx].name,
          distance:distance.distance.text,
          duration:distance.duration.text,
        }
        return info
      })
      shelterInfo.sort(compare)
      console.log(JSON.stringify(shelterInfo))
      
      let r = fetch("/",{
        method:'POST',
        headers:{
          'Content-Type': 'application/json',
        },
        body:JSON.stringify(shelterInfo)
      }).then(()=> {
      console.log("here")
      window.location.href = "/distance" })
      console.log(r)
      
    }
    var service = new google.maps.DistanceMatrixService();
    service.getDistanceMatrix(
    {
        origins: [{lat:45.4979085,lng:-73.6369607}],
        destinations: destinations,
        travelMode: 'WALKING',
    }, callback);

}

async function sendDistancesAndTimes(){



}

function toQuery(params){

    return Object.keys(params).map(key => key + '=' + params[key]).join('&');
}

