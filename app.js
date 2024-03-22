window.onload = function(){
  var mapWidth = localStorage.getItem("mapWidth");
  var map = document.getElementById("map");
  if(mapWidth){
    map.setAttribute("width", mapWidth);
  }
};

document.addEventListener('DOMContentLoaded', function() {
  updateOnClick();
  updateOnChange();
  handleZoom();
  handleReset();
});

function updateOnClick(){
  const buildings = document.querySelectorAll('.structure');
  buildings.forEach(buildings => {
    buildings.addEventListener('click', function(){
      var clicked = document.getElementById(this.id);
      var formSource = document.getElementById("formSource");
      var formDestination = document.getElementById("formDestination");     

      var source = document.querySelectorAll('.sourceActive');
      var destination = document.querySelectorAll('.destinationActive');  

      if(source.length == 0 && destination.length == 0){
        clicked.classList.toggle("sourceActive");
        formSource.selectedIndex = findStructureIndex(formSource, this.id);
      }
      else if(destination.length == 0){
        if(clicked == source[0]){
          clicked.classList.toggle("sourceActive");
          formSource.selectedIndex = 0;
        }
        else{
          clicked.classList.toggle("destinationActive");
          formDestination.selectedIndex = findStructureIndex(formDestination, this.id);
        }
      }
      else{
        if(clicked == source[0]){
          clicked.classList.toggle("sourceActive");
          destination[0].classList.toggle("destinationActive");  
          formSource.selectedIndex = 0;
          formDestination.selectedIndex = 0;
        }
        else if(clicked == destination[0]){
          clicked.classList.toggle("destinationActive");
          formDestination.selectedIndex = 0;
        }
        else{
          alert("Only select 2 locations");
        }
      }
    });
  });
}

function updateOnChange(){
  const formSource = document.getElementById("formSource");
  formSource.addEventListener("change", function(){
    var currentSource = document.querySelectorAll('.sourceActive');
    if(currentSource.length > 0){
      currentSource[0].classList.toggle("sourceActive");
    }

    const newSource = document.getElementById(formSource.value);
    newSource.classList.toggle("sourceActive");
  });

  const formDestination = document.getElementById("formDestination");
  formDestination.addEventListener("change", function(){
    var currentDestination = document.querySelectorAll('.destinationActive');
    if(currentDestination.length > 0){
      currentDestination[0].classList.toggle("destinationActive");
    }

    const newDestination = document.getElementById(formDestination.value);
    newDestination.classList.toggle("destinationActive");
  });
}

function handleZoom(){
  var map = document.getElementById("map");

  const zoomIn = document.getElementById("zoomin");
  zoomIn.addEventListener("click", function(){
    var bounds = map.getBoundingClientRect();
    width = bounds.width * 1.1;
    map.setAttribute("width", width)
    localStorage.setItem("mapWidth", width);
  });

  const zoomOut = document.getElementById("zoomout");
  zoomOut.addEventListener("click", function(){
    var bounds = map.getBoundingClientRect();
    width = bounds.width / 1.1;
    map.setAttribute("width", width)
    localStorage.setItem("mapWidth", width);
  });
}

function handleReset(){
  const reset = document.getElementById("mapReset");
  reset.addEventListener("click", function(){
    var source = document.querySelector('.sourceActive');
    if(source){
      source.classList.toggle("sourceActive");
    }

    var dest = document.querySelector('.destinationActive');
    if(dest){
      dest.classList.toggle("destinationActive");
    }

    var route = document.querySelector(".route");
    if(route){
      route.setAttribute("display", "none");
    }
  });
}

function findStructureIndex(selectBox, structureID){
  for(var i = 0; i < selectBox.length; i++){
    if(selectBox.options[i].value == structureID){
      return i;
    }
  }
}