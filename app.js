var selectedSource = "";
var selectedDestination = "";
var sourceClassroom = "";
var destinationClassroom = "";
var view = "map"

document.addEventListener('DOMContentLoaded', function() {
  updateOnClick();
  updateOnChange();
  handleZoom();
  handleReset();
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

function dragAndDrop(){
  var text = document.getElementById("map");
  text.onmousedown = function(event) {
    let shiftX = event.clientX - text.getBoundingClientRect()
      .left;
    let shiftY = event.clientY - text.getBoundingClientRect()
      .top;
    text.style.position = 'absolute';
    document.body.append(text);
    moveAt(event.pageX, event.pageY);
    // move the text along the coordinates (pageX, pageY)
    // taking into account the initial shifts
    function moveAt(pageX, pageY) {
      text.style.left = pageX - shiftX + 'px';
      text.style.top = pageY - shiftY + 'px';
    }
    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
    }
    // move the text to the  mousemove
    document.addEventListener('mousemove', onMouseMove);
    // drop the text, remove unneeded handlers
    text.onmouseup = function() {
      document.removeEventListener('mousemove', onMouseMove);
      text.onmouseup = null;
    };
  };
  text.ondragstart = function() {
    return false;
  };
}

function handleText(){
  const textButton = document.getElementById("changeText");
  textButton.addEventListener("click", function(){
    var selectRooms = document.getElementById(selectedSource + "Rooms");
    var destinationRooms = document.getElementById(selectedDestination + "Rooms");

    if(selectRooms != null){
      var rooms = selectRooms.children;
      for(var i = 0; i < rooms.length; i += 2){
        var boundingBox = rooms[i].getBBox();
        var roomTransform = rooms[i].getAttribute("transform");
        roomTransform = roomTransform.replace('translate(', '');
        roomTransform = roomTransform.replace(')', '');
        roomCoords = roomTransform.split(',')
        var text = rooms[i + 1];

        var textBox = text.getBBox();

        text.setAttribute('x', parseFloat(roomCoords[0]) + (boundingBox.width - textBox.width) / 2);
        text.setAttribute('y', parseFloat(roomCoords[1]) + (boundingBox.height - textBox.height) / 2);
      }
    }
  });
}

function updateOnClick(){
  const buildings = document.querySelectorAll('.structure');
  buildings.forEach(buildings => {
    buildings.addEventListener('click', function(){
      var formSource = document.getElementById("formSource");
      var formDestination = document.getElementById("formDestination");     
      
      if(!selectedSource && !selectedDestination){
        formSource.selectedIndex = findStructureIndex(formSource, this.id);
        selectedSource = this.id;

        displayClasses(selectedSource, "source");
        manageHeader();
      }
      else if(!selectedSource){
        if(this.id == selectedDestination){
          formDestination.selectedIndex = 0;

          removeClasses(selectedDestination, "destination");
          manageHeader();
        }
        else{
          formSource.selectedIndex = findStructureIndex(formSource, this.id);
          selectedSource = this.id;

          displayClasses(selectedSource, "source");
          manageHeader();
        }
      }
      else if(!selectedDestination){
        if(this.id == selectedSource){
          formSource.selectedIndex = 0;

          removeClasses(selectedSource, "source")
          manageHeader();
        }
        else{
          formDestination.selectedIndex = findStructureIndex(formDestination, this.id);
          selectedDestination = this.id;

          displayClasses(selectedDestination, "destination");
          manageHeader();
        }
      }
      else{
        if(this.id == selectedDestination){
          formDestination.selectedIndex = 0;

          removeClasses(selectedDestination, "destination")
          manageHeader();
        }
        else if(this.id == selectedSource){
          formSource.selectedIndex = 0;

          removeClasses(selectedSource, "source");
          manageHeader();
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
    if(selectedSource){
      removeClasses(selectedSource, "source");
    }

    selectedSource = formSource.value;
    displayClasses(selectedSource, "source");
    manageHeader();
  });

  const formDestination = document.getElementById("formDestination");
  formDestination.addEventListener("change", function(){
    if(selectedDestination){
      removeClasses(selectedDestination, "destination")
    }

    selectedDestination = formDestination.value;
    displayClasses(selectedDestination, "destination");
    manageHeader();
  });
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
  var main = document.getElementById("page");
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

function handleReset(){
  const reset = document.getElementById("mapReset");
  reset.addEventListener("click", function(){
    if(selectedSource){
      removeClasses(selectedSource, "source");
    }
    if(selectedDestination){
      removeClasses(selectedDestination, "destination");
    }
    manageHeader();

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

function displayClasses(building, buildingType){
  var ajax = new XMLHttpRequest();

  ajax.onreadystatechange = function(){
    var clickedBuilding = document.getElementById(building);

    if(ajax.readyState == XMLHttpRequest.DONE){
        if(ajax.status == 200){
          var classList = ajax.responseText;

          if(!classList.includes("Error")){
            classList = JSON.parse(classList);
            var divBlock = document.getElementById(buildingType + "Select");

            var classroomSelect = document.createElement("select");
            var classroomId = "classroom" + buildingType;
            classroomSelect.id = classroomId;
            classroomSelect.setAttribute("name", classroomId);

            var optionList = "<option disabled selected value>Room Number</option>";
            for(var i = 0; i < classList.length; i++){
              if(classList[i][0] != '0'){
                optionList += "<option value='" + classList[i][0] + "'>" + classList[i][0] + "</option>";
              }
            }
  
            classroomSelect.innerHTML = optionList;
            divBlock.appendChild(classroomSelect);
            classroomUpdate(classroomSelect, buildingType);

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
                  classroomClick(newRoom, building);
                }
                else{
                  newRoom.classList.add("dummyClass");
                }

                newRoom.setAttribute("d", classList[i][3]);
                newRoom.setAttribute("transform", "translate(" + classList[i][1] + "," + classList[i][2] + ")");
                newRoom.setAttribute("title", classList[i][0]);
                
                buildingGroup.appendChild(newRoom);
              }
              svgMap.appendChild(buildingGroup);
            }
            else{
              for(var i = 0; i < classList.length; i++){
                var newRoom = document.createElementNS("http://www.w3.org/2000/svg", "path");
                newRoom.id = classList[i][0];             
              }
            }
            clickedBuilding.classList.add("buildingInterior");
          }
          else{
            clickedBuilding.classList.add(buildingType + "Active");
          }
      }
    }
  };
  
  ajax.open("GET", "?building=" + building, true);
  ajax.send();
}

function removeClasses(building, buildingType){
  var roomSelect = document.getElementById("classroom" + buildingType);
  if(roomSelect){
    roomSelect.remove();
    
    var roomBlock;
    if(buildingType == "source"){
      roomBlock = document.getElementById(sourceClassroom);
    }
    else{
      roomBlock = document.getElementById(destinationClassroom);
    }

    if(roomBlock){
      roomBlock.classList.remove(buildingType + "ClassActive");
    }
  }
  else{
    var clickedBuilding = document.getElementById(building);
    clickedBuilding.classList.remove(buildingType + "Active");
  }

  var roomBuildings = document.getElementById(building + "Rooms");
  if(roomBuildings){
    if(selectedSource != selectedDestination){
      roomBuildings.remove();
      document.getElementById(building).classList.remove("buildingInterior");
    }
  }

  if(buildingType == "source"){
    sourceClassroom = "";
    selectedSource = "";
  }
  else{
    destinationClassroom = "";
    selectedDestination = "";
  }

  manageHeader();
}

function manageHeader(){
  var submitButton = document.getElementById("mapSubmit");
  var clearButton = document.getElementById("mapReset");
  var destinaton = document.getElementById("destination");

  if(selectedSource && selectedDestination){
    submitButton.classList.remove("hideElement");
  }
  else if(selectedSource){
    clearButton.classList.remove("hideElement");

    destination.classList.remove("destinationHide");
    destination.classList.add("destinationTransition");

    submitButton.classList.add("hideElement");
  }
  else if(selectedDestination){
    clearButton.classList.remove("hideElement");
    submitButton.classList.add("hideElement");
    destination.classList.remove("destinationHide");
    destination.classList.add("destinationTransition");
  }
  else{
    destination.classList.add("destinationHide");
    destination.classList.remove("destinationTransition");

    clearButton.classList.add("hideElement");
  }
}

function classroomClick(classroomBlock, building){
  classroomBlock.addEventListener('click', function(){
    var buildingType = "";
    if(selectedSource == building){
      buildingType = "source"
    }
    else if(selectedDestination == building){
      buildingType = "destination";
    }
    else{
      return;
    }
    if(!sourceClassroom && !destinationClassroom){
      if(buildingType =="source"){
        classroomBlock.classList.add("sourceClassActive");
        sourceClassroom = classroomBlock.id;

        var classSelect = document.getElementById("classroomsource");
        classSelect.selectedIndex = findStructureIndex(classSelect, sourceClassroom);
      }
      else{      
        classroomBlock.classList.add("destinationClassActive");
        destinationClassroom = classroomBlock.id;

        var classSelect = document.getElementById("classroomdestination");
        classSelect.selectedIndex = findStructureIndex(classSelect, destinationClassroom);  
      }
      manageHeader();
    }
    else if(!destinationClassroom){
      if(sourceClassroom == classroomBlock.id){
        classroomBlock.classList.remove("sourceClassActive");
        sourceClassroom = "";
        
        var classSelect = document.getElementById("classroomsource");
        classSelect.selectedIndex = 0;
      }
      else if(!selectedDestination){
        selectedDestination = selectedSource;

        var destinationBuilding = document.getElementById("formDestination");
        destinationBuilding.selectedIndex = findStructureIndex(destinationBuilding, selectedDestination);

        var destinationDiv = document.getElementById("destinationSelect");
        var classroomCopy = document.getElementById("classroomsource").cloneNode(true);
        classroomCopy.id = "classroomdestination";
        classroomCopy.setAttribute("name", "classroomdestination");

        classroomCopy.selectedIndex = findStructureIndex(classroomCopy, classroomBlock.id);
        destinationDiv.appendChild(classroomCopy);

        classroomBlock.classList.add("destinationClassActive");
        destinationClassroom = classroomBlock.id;
      }
      else{
        alert("Only select 2 locations");     
      }
      manageHeader();
    }
    else if(!sourceClassroom){
      if(destinationClassroom == classroomBlock.id){
        classroomBlock.classList.remove("destinationClassActive");
        destinationClassroom = "";
        
        var classSelect = document.getElementById("classroomdestination");
        classSelect.selectedIndex = 0;
        manageHeader();
      }
      else if(!selectedSource){
        selectedSource = selectedDestination;

        var sourceBuilding = document.getElementById("formSource");
        sourceBuilding.selectedIndex = findStructureIndex(sourceBuilding, selectedSource);

        var sourceDiv = document.getElementById("sourceSelect");
        var classroomCopy = document.getElementById("classroomdestination").cloneNode(true);
        classroomCopy.id = "classroomsource";
        classroomCopy.setAttribute("name", "classroomsource");

        classroomCopy.selectedIndex = findStructureIndex(classroomCopy, classroomBlock.id);
        sourceDiv.appendChild(classroomCopy);

        classroomBlock.classList.add("sourceClassActive");
        sourceClassroom = classroomBlock.id;
      }
      else{
        alert("Only select 2 locations");     
      }
      manageHeader();
    }    
    else{
      if(sourceClassroom == classroomBlock.id){
        if(selectedSource == selectedDestination){
          var sourceBuilding = document.getElementById("formSource");
          sourceBuilding.selectedIndex = 0;
          removeClasses(selectedSource, "source");
        }
        else{
          var classSelect = document.getElementById("classroomsource");
          classSelect.selectedIndex = 0;
        }
        classroomBlock.classList.remove("sourceClassActive");
        sourceClassroom = ""; 
      }
      else if(destinationClassroom == classroomBlock.id){
        if(selectedSource == selectedDestination){
          var destinationBuilding = document.getElementById("formDestination");
          destinationBuilding.selectedIndex = 0;
          removeClasses(selectedDestination, "destination");
        }
        else{
          var classSelect = document.getElementById("classroomdestination");
          classSelect.selectedIndex = 0;
        }
        classroomBlock.classList.remove("destinationClassActive");
        destinationClassroom = ""; 
      }
      else{
        alert("Only select 2 locations");      
      }
      manageHeader();
    }
  });
}

function classroomUpdate(classroomSelect, buildingType){
  classroomSelect.addEventListener("change", function(){
    if(buildingType == "source"){
      if(sourceClassroom){
        var roomBlock = document.getElementById(sourceClassroom);
        roomBlock.classList.remove("sourceClassActive");
      }
  
      sourceClassroom = classroomSelect.value;
      var roomBlock = document.getElementById(sourceClassroom);
      roomBlock.classList.add("sourceClassActive");
    }
    else{
      if(destinationClassroom){
        var roomBlock = document.getElementById(destinationClassroom);
        roomBlock.classList.remove("destinationClassActive");
      }
  
      destinationClassroom = classroomSelect.value;
      var roomBlock = document.getElementById(destinationClassroom);
      roomBlock.classList.add("destinationClassActive");
    }
  });
}

function validatePath(){
  if(selectedDestination == selectedSource && destinationClassroom == sourceClassroom){
    alert("Source and Destination cannot be the same location");
    return false;
  }
  localStorage.setItem("source", selectedSource);
  localStorage.setItem("destination", selectedDestination);
  localStorage.setItem("sourceRoom", sourceClassroom);
  localStorage.setItem("destinationRoom", destinationClassroom);
  return true;
}
