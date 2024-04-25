var source = localStorage.getItem("source");
var destination = localStorage.getItem("destination");
var sourceClassroom = localStorage.getItem("sourceRoom");
var destinationClassroom = localStorage.getItem("destinationRoom");
var view = "map";

document.addEventListener('DOMContentLoaded', function() {
  handleZoom();
  fillInfo();
  handleView();
window.addEventListener('beforeunload', saveScrollPosition);
window.addEventListener('load', restoreScrollPosition);
});

  // Save the current vertical scroll position
  function saveScrollPosition() {
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
    localStorage.setItem('scrollPosition', scrollPosition);
  }
  
  // Restore the saved vertical scroll position
  function restoreScrollPosition() {
    var scrollPosition = localStorage.getItem('scrollPosition');
    if (scrollPosition !== null) {
        window.scrollTo(0, scrollPosition);
    }
  }

function handleZoom(){
  var map = document.getElementById("map");
  if(localStorage.getItem("width") != null){
    map.setAttribute("width", localStorage.getItem("width"))
  }
  var bounds = map.getBoundingClientRect();

  var picture = document.getElementById("picture");
  picture.setAttribute("width", bounds.width)

  const zoomIn = document.getElementById("zoomin");
  zoomIn.addEventListener("click", function(){
    var bounds = map.getBoundingClientRect();
    width = bounds.width * 1.1;

    map.setAttribute("width", width)
    picture.setAttribute("width", width)
    localStorage.setItem("width", width);
  });

  const zoomOut = document.getElementById("zoomout");
  zoomOut.addEventListener("click", function(){
    var bounds = map.getBoundingClientRect();
    width = bounds.width / 1.1;
    
    map.setAttribute("width", width)
    picture.setAttribute("width", width)
    localStorage.setItem("width", width);
  });
}

function handleView(){
  var main = document.getElementById("result");
  const changeView = document.getElementById("changeView");

  if(localStorage.getItem("view") != null){
    main.classList.toggle("earth");
    view = "earth";
  }

  changeView.addEventListener("click", function(){
    main.classList.toggle("earth");
    if(view == "map"){
      view = "earth";
      localStorage.setItem("view", "earth");
    }
    else{
      view = "map";
      localStorage.removeItem("view");
    }
  });
}

function fillInfo(){
  document.getElementById("sourceResult").textContent = source;
  document.getElementById("destinationResult").textContent = destination;

  if(sourceClassroom){
    displayClassrooms(source);
    document.getElementById("sourceRoomResult").textContent = sourceClassroom;
  }

  if(destinationClassroom){
    displayClassrooms(destination);
    document.getElementById("destinationRoomResult").textContent = destinationClassroom;
  }
}

function displayClassrooms(building){
  var ajax = new XMLHttpRequest();

  ajax.onreadystatechange = function(){
    var clickedBuilding = document.getElementById(building);

    if(ajax.readyState == XMLHttpRequest.DONE){
        if(ajax.status == 200){
          var classList = ajax.responseText;
          if(!classList.includes("Error")){
            classList = JSON.parse(classList);

            var buildingId = building + "Rooms";
            var buildingGroup = document.getElementById(buildingId);
            if(!buildingGroup){
              var svgMap = document.getElementById("map");
              buildingGroup = document.createElementNS("http://www.w3.org/2000/svg", "g");
              buildingGroup.id = (buildingId);

              for(var i = 0; i < classList.length; i++){
                var newRoom = document.createElementNS("http://www.w3.org/2000/svg", "path");
                if(classList[i][0] != "0"){
                  newRoom.id = classList[i][0];
                  newRoom.classList.add("classroom");
                  if(newRoom.id == sourceClassroom){
                    newRoom.classList.add("sourceClassActive");
                  }
                  else if(newRoom.id == destinationClassroom){
                    newRoom.classList.add("destinationClassActive");
                  }
                }
                else{
                  newRoom.classList.add("dummyClass");
                }
                newRoom.setAttribute("d", classList[i][3]);
                newRoom.setAttribute("transform", "translate(" + classList[i][1] + "," + classList[i][2] + ")");

                buildingGroup.appendChild(newRoom);
              }
              svgMap.insertBefore(buildingGroup, svgMap.getElementById("route"));
            }
            clickedBuilding.classList.remove("sourceActive");
            clickedBuilding.classList.remove("destinationActive");
        }
      }
    }
  };
  
  ajax.open("GET", "?building=" + building, true);
  ajax.send();
}