/**
 * Developer: Harrison Hughes, Truman State University 2024
 * This file coordinates all client-side programming functionalities for the app.php file
 */

const ZOOM_RATIO = 1.2;
const WIDTH_HEIGHT_RATIO = 1117/1093;

//To hold current user selections of the source and destination locations
var selectedSource = "";
var selectedDestination = "";
var sourceClassroom = "";
var destinationClassroom = "";

//Default view is "map", or the digital view. "Earth" provides the satellite view
var view = "map"

//Automatic modifications and event listeners to proceed with upon loading of the webpage
document.addEventListener('DOMContentLoaded', function() {
  window.addEventListener("load", loadPosition);
  handleView();
  handleZoom();

  updateOnClick();
  updateOnChange();
  handleReset();

  //Store scroll positions of page on unload to assert same view on result.php
  window.addEventListener('beforeunload', storePosition);
  });
  
  /**
 * To store the vertical and horizontal scroll position of the page upon 
 * unloading of the webpage. This allows identical positioning to be maintained
 * when sending to result.php
 */
  function storePosition(){
    var scrollX = document.documentElement.scrollLeft;
    var scrollY = document.documentElement.scrollTop;
  
    //Save position to be accessed by result.php
    localStorage.setItem('scrollX', scrollX);
    localStorage.setItem('scrollY', scrollY);
  }
  
    /**
 * To load the vertical and horizontal scroll position of the page upon 
 * DOM loading of the webpage. This allows identical positioning to be maintained when 
 * returning from result.php
 */
  function loadPosition(){
    var scrollX = localStorage.getItem('scrollX');
    var scrollY = localStorage.getItem('scrollY');
  
    //Scroll to ssaved position
    if (scrollX !== null && scrollY !== null) {
        window.scrollTo(scrollX, scrollY);
    }
  }

/**
* Updates both select box and class specifications of a location upon its click.
  This includes maintaining proper source and destination objects, ensuring 
  responsivness from select box, and preventing more than 2 active objects at a time.
*/
function updateOnClick(){
  const buildings = document.querySelectorAll('.structure');

  //Add listener for each clickable location on campus to wait for click interactions
  buildings.forEach(buildings => {
    buildings.addEventListener('click', function(){

      //We must ensure coordination with source and destination select boxes upon each click
      var formSource = document.getElementById("formSource");
      var formDestination = document.getElementById("formDestination");     
      
      //First location has been clicked
      if(!selectedSource && !selectedDestination){

        //Update select box
        formSource.selectedIndex = findStructureIndex(formSource, this.id);
        selectedSource = this.id;

        //Update appearance of location and provoke header update
        displayClasses(selectedSource, "source");
        manageHeader();
      }

      //Destination object is currently selected but not source object
      else if(!selectedSource){

        //If destination object was the location that was clicked
        if(this.id == selectedDestination){

          //Update select box
          formDestination.selectedIndex = 0;

          //Update appearance of location and provoke header update
          removeClasses(selectedDestination, "destination");
          manageHeader();
        }
        //Otherwise, we have selected a new source object
        else{
          //Update select box
          formSource.selectedIndex = findStructureIndex(formSource, this.id);
          selectedSource = this.id;

          //Update appearance of location and provoke header update
          displayClasses(selectedSource, "source");
          manageHeader();
        }
      }

      //Source object is currently selected but not destination object
      else if(!selectedDestination){

        //If source object was the location that was clicked
        if(this.id == selectedSource){

          //Update select box
          formSource.selectedIndex = 0;

          //Update appearance of location and provoke header update
          removeClasses(selectedSource, "source")
          manageHeader();
        }

        //Otherwise, we have selected a new destination object
        else{

          //Update select box
          formDestination.selectedIndex = findStructureIndex(formDestination, this.id);
          selectedDestination = this.id;

          //Update appearance of location and provoke header update
          displayClasses(selectedDestination, "destination");
          manageHeader();
        }
      }

      //Otherwise, both a source and destination object are active
      else{

        //If destination object was the location that was clicked
        if(this.id == selectedDestination){

          //Update select box
          formDestination.selectedIndex = 0;

          //Update appearance of location and provoke header update
          removeClasses(selectedDestination, "destination")
          manageHeader();
        }

        //If source object was the location that was clicked
        else if(this.id == selectedSource){

          //Update select box
          formSource.selectedIndex = 0;

          //Update appearance of location and provoke header update
          removeClasses(selectedSource, "source");
          manageHeader();
        } 

        //Otherwise, an attempt to select a 3rd location object was made
        else{
          alert("Only select 2 locations");
        }
      }
    });
  });
}

/**
* Updates both select box and class specifications of a location upon select box change.
  This includes maintaining proper source and destination objects appearances. 
*/
function updateOnChange(){

  //Find select box blocks
  const formSource = document.getElementById("formSource");
  const formDestination = document.getElementById("formDestination");

  //Listen for any change to the selection
  formSource.addEventListener("change", function(){

    //If there was previously an active source object, first remove it
    if(selectedSource){
      removeClasses(selectedSource, "source");
    }

    //Capture value of selected option
    selectedSource = formSource.value;

    //Update appearance of location and provoke header update
    displayClasses(selectedSource, "source");
    manageHeader();
  });

  //Listen for any change to the selection
  formDestination.addEventListener("change", function(){

    //If there was previously an active destination object, first remove it
    if(selectedDestination){
      removeClasses(selectedDestination, "destination")
    }

    //Capture value of selected option
    selectedDestination = formDestination.value;

    //Update appearance of location and provoke header update
    displayClasses(selectedDestination, "destination");
    manageHeader();
  });
}

/**
 * Coordinate initial zoom level with that of the result.php file upon returning, 
 * and ensure proper zoom mechanics when interacting with the zoom in and out buttons.
 * "Zoom" is simulated by altering the width of the SVG file.
 */
function handleZoom() {
  //Get the SVG file block
  var map = document.getElementById("map");

  //If a zoom level is stored locally, retrieve it and set it as the current width of the SVG file
  if (localStorage.getItem("width") != null) {
    map.setAttribute("width", localStorage.getItem("width"));
  }

  //Get width of SVG file and set the satellite picture to have an identical width 
  var bounds = map.getBoundingClientRect();
  var picture = document.getElementById("picture");
  picture.setAttribute("width", bounds.width);

  //If width is bigger than screen, shift image to the right to ensure no content is hidden
  //off the left of the screen, as this is unable to be accessed by scrolling
  var leftTranslate = bounds.width - window.innerWidth;
  if (leftTranslate > 0) {

    //Shift images to right by the difference in image and screen size
    map.style.marginLeft = leftTranslate + "px";
    picture.style.marginLeft = leftTranslate + "px";
  }

  //Listen for any click of the zoom in button
  const zoomIn = document.getElementById("zoomin");
  zoomIn.addEventListener("click", function () {

    //Calculate new width, and retrieve the current scroll focus on the screen
    bounds = map.getBoundingClientRect();
    width = bounds.width * ZOOM_RATIO;
    var focus = calculateFocus();

    //If zoom causes image to be larger than screen, shift right by the difference
    if (width > window.innerWidth) {
      leftTranslate = width - window.innerWidth;
      map.style.marginLeft = leftTranslate + "px";
      picture.style.marginLeft = leftTranslate + "px";
    }

    //Update width of images based on zoom ratio and save width locally
    map.style.width = width + "px";
    picture.style.width = width + "px";
    localStorage.setItem("width", width);

    //Refocus to horizontal center if horizontal scroll bar has just appeared
    if(bounds.width <= window.innerWidth){
      loadFocus(0.5, focus[1]);
    }

    //Else update the scroll focus to the previous point
    else{
      loadFocus(focus[0], focus[1]);
    }
  });

   //Listen for any click of the zoom out button
  const zoomOut = document.getElementById("zoomout");
  zoomOut.addEventListener("click", function () {

    //Calculate new width, and retrieve the current scroll focus on the screen
    bounds = map.getBoundingClientRect();
    width = bounds.width / ZOOM_RATIO;
    var focus = calculateFocus();

    //Update translate as images continue to need less translation to stay on screem
    leftTranslate = width - window.innerWidth;
    if (leftTranslate > 0) {
      map.style.marginLeft = leftTranslate + "px";
      picture.style.marginLeft = leftTranslate + "px";
    }

    //If images are not wider than screen, no offset is needed
    else{
      map.style.marginLeft = 0 + "px";
      picture.style.marginLeft = 0 + "px";
    }

    //Update width of images based on zoom ratio, save width locally, and load scroll focus
    map.style.width = width + "px";
    picture.style.width = width + "px";
    localStorage.setItem("width", width);

    //Refocus to horizontal center if horizontal scroll bar has just appeared
    if(bounds.width <= window.innerWidth){
      loadFocus(0.5, focus[1]);
    }

    //Else update the scroll focus to the previous point
    else{
      loadFocus(focus[0], focus[1]);
    }
  });
}

/**
 * Find the current focus of the scroll bars on the image to ensure that the 
 * same point in the file based on the scroll is focused on before and after a zoom
 * @returns an array holding the percentage of the screen that is currently scrolled
 * both vertically and horizontally
 */
function calculateFocus() {

  //Get height and width of the SVG image at its current state
  var svg = document.getElementById("map");
  var svgStyle = window.getComputedStyle(svg);
  var width = parseFloat(svgStyle.width);
  var height = width * WIDTH_HEIGHT_RATIO;

  //Get the pixel values of that have been scrolled
  var scrollX = document.documentElement.scrollLeft;
  var scrollY = document.documentElement.scrollTop;

  //Calculate the percentage of the screen scrolled by dividing the scroll by the total scroll size
  var leftPercentage = scrollX / (width - document.documentElement.clientWidth);
  var topPercentage = scrollY / (height -  document.documentElement.clientHeight);

  return [leftPercentage, topPercentage];
}

/**
 * Set the current scroll level to that of the parameters based on the
 * proportions that they specify
 * @param shiftX The proportion of the screen that the horizontal scroll bar needs to be set to
 * @param shiftY The proportion of the screen that the vertical scroll bar needs to be set to
 */
function loadFocus(shiftX, shiftY){

  //Get height and width of the SVG image at its current state
  var svg = document.getElementById("map");
  var svgStyle = window.getComputedStyle(svg);
  var width = parseFloat(svgStyle.width);
  var height = width * WIDTH_HEIGHT_RATIO;

  //Use the proportion to calculate an actual pixel value to scroll by
  var scrollX = shiftX * (width -  document.documentElement.clientWidth);
  var scrollY = shiftY * (height - document.documentElement.clientHeight);

  //Scroll to the calculated values
  window.scrollTo({
    top: scrollY,
    left: scrollX,
  });
}

/**
 * Set the current view to the stored specificaiton and interact with the view change button
 * to comply with the user requested view between digital and satellite 
 */
function handleView(){

  //Get the current page and the view change button
  var main = document.getElementById("page");
  const changeView = document.getElementById("changeView");

  //Set view to satellite if it was stored by result.php
  if(localStorage.getItem("view") != null){
    main.classList.toggle("earth");
    view = "earth";
  }

  //Listen for the button to be clicked to change the view
  changeView.addEventListener("click", function(){

    //Toggle view to change it
    main.classList.toggle("earth");

    //Change view variable and set local storage
    if(view == "map"){
      view = "earth";
      localStorage.setItem("view", "earth");
    }

    //Change view variable and remove local storage
    else{
      view = "map";
      localStorage.removeItem("view");
    }
  });
}

/**
 * Ensure all information is deleted and set to defaults when the 
 * user presses the reset button
 */
function handleReset(){

  //Find reset button and add event listener
  const reset = document.getElementById("mapReset");
  reset.addEventListener("click", function(){

    //Delete selected source display and variables if applicable
    if(selectedSource){
      removeClasses(selectedSource, "source");
    }

    //Delete selected destination display and variables if applicable
    if(selectedDestination){
      removeClasses(selectedDestination, "destination");
    }

    //Remove header modifications
    manageHeader();
  });
}

/**
 * Find the form index of the parameter option given the select box form block
 * @param selectBox The form block that holds all options 
 * @param structureID The option that we wish to find the correct index of
 * @returns the index in the form select type corresponding to the specified option
 */
function findStructureIndex(selectBox, structureID){

  //Check all elements and return when the correct index is found
  for(var i = 0; i < selectBox.length; i++){
    if(selectBox.options[i].value == structureID){
      return i;
    }
  }
  return 0;
}
/**
 * Either highlight the building if no internal classes have been designed, or display all classes
 * corresponding to the current building, adding event listeners to each. This populates the SVG
 * with more interactive locations
 * @param building Structure ID corresponding to the selected building name
 * @param buildingType Either source or destination, to coordinate display classes 
 */
function displayClasses(building, buildingType){
  const INVALID_CLASSROOM = '0';

  //Get location of interest
  var clickedBuilding = document.getElementById(building);

  //Prepare and handle ajax HTTP request to get the classroom information from the server if applicable
  var ajax = new XMLHttpRequest();
  ajax.onreadystatechange = function(){

    //Verify success of http request and retrieve information from server
    if(ajax.readyState == XMLHttpRequest.DONE){
        if(ajax.status == 200){
          var classList = ajax.responseText;

          //If file exists, we can draw the classrooms
          if(classList && !classList.includes("Error")){
            classList = JSON.parse(classList);

            //Get appropriate source or destination header block to add new select box for classrooms
            var divBlock = document.getElementById(buildingType + "Select");
            var classroomSelect = document.createElement("select");
            var classroomId = "classroom" + buildingType;
            classroomSelect.id = classroomId;
            classroomSelect.setAttribute("name", classroomId);

            //Add all classes retrieved from server and add them to select box
            var optionList = "<option class='optionHeader' disabled selected>Room</option>";
            for(var i = 0; i < classList.length; i++){
              if(classList[i][0] != INVALID_CLASSROOM){
                optionList += "<option value='" + classList[i][0] + "'>" + classList[i][0] + "</option>";
              }
            }
  
            //Append select box to correct header and add listener to the new select box
            classroomSelect.innerHTML = optionList;
            divBlock.appendChild(classroomSelect);
            classroomUpdate(classroomSelect, buildingType);

            //Check if the current classrooms are already drawn on the SVG file. If not, draw them. 
            var buildingId = building + "Rooms";
            var buildingGroup = document.getElementById(buildingId);
            if(!buildingGroup){
              
              //Get SVG block and create SVG group to hold the classrooms
              var svgMap = document.getElementById("map");
              buildingGroup = document.createElementNS("http://www.w3.org/2000/svg", "g");
              buildingGroup.id = (buildingId);

              //Draw all classrooms
              for(var i = 0; i < classList.length; i++){
                var newRoom = document.createElementNS("http://www.w3.org/2000/svg", "path");

                //Draw all specified classrooms and add listeners for user click
                if(classList[i][0] != INVALID_CLASSROOM){
                  newRoom.id = classList[i][0];
                  newRoom.classList.add("classroom");
                  classroomClick(newRoom, building);
                }
                else{
                  newRoom.classList.add("dummyClass");
                }

                //Style classrooms with file specified paths, names, and coordinates
                newRoom.setAttribute("d", classList[i][3]);
                newRoom.setAttribute("transform", "translate(" + classList[i][1] + "," + classList[i][2] + ")");
                newRoom.setAttribute("title", classList[i][0]);

                //Append classroom to group
                buildingGroup.appendChild(newRoom);
              }

              //Append group to actual SVG file
              svgMap.appendChild(buildingGroup);
            }

            //Add exterior building style for background purposes
            clickedBuilding.classList.add("buildingInterior");
          }

          //Otherwise, the location has no classroom designs and a generic style is added
          else{
            clickedBuilding.classList.add(buildingType + "Active");
          }
      }
    }
  };
  
  //Send ajax http request to retrieve the classroom data from
  ajax.open("GET", "?building=" + building, true);
  ajax.send();
}

/**
 * Remove all classroom and styles for a location after it has been deselected. 
 * @param building the structure ID that corresponds to a specific location 
 * @param buildingType destination or source to distinguish which type to search for 
 */
function removeClasses(building, buildingType){

  //Find and remove classroom select box if applicable
  var roomSelect = document.getElementById("classroom" + buildingType);
  if(roomSelect){
    roomSelect.remove();
    
    //Find classroom structure that is currently active based on type specification
    var roomBlock;
    if(buildingType == "source"){
      roomBlock = document.getElementById(sourceClassroom);
    }
    else{
      roomBlock = document.getElementById(destinationClassroom);
    }

    //Remove classroom designs to revert to default
    if(roomBlock){
      roomBlock.classList.remove(buildingType + "ClassActive");
    }
  }

  //Otherwise, the location itself was clicked; find it and remove the styles
  else{
    var clickedBuilding = document.getElementById(building);
    clickedBuilding.classList.remove(buildingType + "Active");
  }

  //If external building is deselected when classrooms are active, remove them
  var roomBuildings = document.getElementById(building + "Rooms");
  if(roomBuildings){
    //If opposite object is not also referencing this current classroom, remove the classrooms from the screen
    if(selectedSource != selectedDestination){

      //Remove classrooms and return location to default style
      roomBuildings.remove();
      document.getElementById(building).classList.remove("buildingInterior");
    }
  }

  //Set all applicable monitoring variables to null
  if(buildingType == "source"){
    sourceClassroom = "";
    selectedSource = "";
  }
  else{
    destinationClassroom = "";
    selectedDestination = "";
  }

  //Update header to appropriate view
  manageHeader();
}

/**
 * Display correct information based on the information that has been selected by the
 * user. This requires hiding and redisplaying the search, clear, and destination blocks. 
 */
function manageHeader(){
  
  //Retrieve all necessary blocks
  var submitButton = document.getElementById("mapSubmit");
  var clearButton = document.getElementById("mapReset");
  var destination = document.getElementById("destination");

  //Everything is selected
  if(selectedSource && selectedDestination){
    submitButton.classList.remove("hideElement");
  }

  //Only the source is selected
  else if(selectedSource){
    clearButton.classList.remove("hideElement");

    destination.classList.remove("destinationHide");
    destination.classList.add("destinationTransition");

    submitButton.classList.add("hideElement");
  }

  //Only the destination is selected
  else if(selectedDestination){
    clearButton.classList.remove("hideElement");
    submitButton.classList.add("hideElement");
  }

  //Nothing is selected
  else{
    destination.classList.add("destinationHide");
    destination.classList.remove("destinationTransition");

    clearButton.classList.add("hideElement");
  }
}

/**
 * Update the styles and select boxes for the classroom structures upon any user
 * click of a classroom block
 * @param classroomBlock block corresponding to the selected classroom 
 * @param building Specific building that the classroom is housed in
 */
function classroomClick(classroomBlock, building){

  //Listen for any user click of the block
  classroomBlock.addEventListener('click', function(){

    //Determine source or destination property of classroom
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

    //No classrooms have been selected as of yet
    if(!sourceClassroom && !destinationClassroom){

      if(buildingType =="source"){

        //Add source styles to this selected classroom
        classroomBlock.classList.add("sourceClassActive");
        sourceClassroom = classroomBlock.id;

        //Update select box
        var classSelect = document.getElementById("classroomsource");
        classSelect.selectedIndex = findStructureIndex(classSelect, sourceClassroom);
      }
      else{
        
        //Add destination styles to this selected classroom
        classroomBlock.classList.add("destinationClassActive");
        destinationClassroom = classroomBlock.id;

        //Update select box
        var classSelect = document.getElementById("classroomdestination");
        classSelect.selectedIndex = findStructureIndex(classSelect, destinationClassroom);  
      }
    }

    //Source classroom has been selected
    else if(!destinationClassroom){

      //If source classroom has been clicked, deselect it
      if(sourceClassroom == classroomBlock.id){

        //Remove source styles from this classroom
        classroomBlock.classList.remove("sourceClassActive");
        sourceClassroom = "";
        
        //Update select box
        var classSelect = document.getElementById("classroomsource");
        classSelect.selectedIndex = 0;
      }

      //If no exterior destination has been selected at all
      else if(!selectedDestination){

        //Update exterior destination
        selectedDestination = selectedSource;

        //Update exterior destination select box
        var destinationBuilding = document.getElementById("formDestination");
        destinationBuilding.selectedIndex = findStructureIndex(destinationBuilding, selectedDestination);

        //Copy source classroom select box and use it to create destination classroom select box
        var destinationDiv = document.getElementById("destinationSelect");
        var classroomCopy = document.getElementById("classroomsource").cloneNode(true);
        classroomCopy.id = "classroomdestination";
        classroomCopy.setAttribute("name", "classroomdestination");

        //Update select box and append it to the destination header
        classroomCopy.selectedIndex = findStructureIndex(classroomCopy, classroomBlock.id);
        destinationDiv.appendChild(classroomCopy);

        //Add destination styles to this selected classroom
        classroomBlock.classList.add("destinationClassActive");
        destinationClassroom = classroomBlock.id;
      }

      //Otherwise a source classroom and exterior destination are already active, a third location is not allowed
      else{
        alert("Only select 2 locations");     
      }
      manageHeader();
    }

    //Destination classroom has been selected
    else if(!sourceClassroom){

      //If destination classroom has been clicked, deselect it
      if(destinationClassroom == classroomBlock.id){

        //Remove source styles from this classroom
        classroomBlock.classList.remove("destinationClassActive");
        destinationClassroom = "";
        
        //Update select box and header configuration
        var classSelect = document.getElementById("classroomdestination");
        classSelect.selectedIndex = 0;
        manageHeader();
      }

      //If no exterior source has been selected at all
      else if(!selectedSource){

        //Update exterior source
        selectedSource = selectedDestination;

         //Update exterior source select box
        var sourceBuilding = document.getElementById("formSource");
        sourceBuilding.selectedIndex = findStructureIndex(sourceBuilding, selectedSource);

        //Copy destination classroom select box and use it to create source classroom select box
        var sourceDiv = document.getElementById("sourceSelect");
        var classroomCopy = document.getElementById("classroomdestination").cloneNode(true);
        classroomCopy.id = "classroomsource";
        classroomCopy.setAttribute("name", "classroomsource");

        //Update select box and append it to the source header
        classroomCopy.selectedIndex = findStructureIndex(classroomCopy, classroomBlock.id);
        sourceDiv.appendChild(classroomCopy);

        //Add source styles to this selected classroom
        classroomBlock.classList.add("sourceClassActive");
        sourceClassroom = classroomBlock.id;
      }

      //Otherwise a destination classroom and exterior source are already active, a third location is not allowed
      else{
        alert("Only select 2 locations");     
      }
      manageHeader();
    }
    
    //Otherwise both a source and destination classroom are active
    else{

      //If source classroom is clicked, deselect it
      if(sourceClassroom == classroomBlock.id){

        //If source and destination buildings are the same, remove entire building from source
        //as it will remain open due to the destination object being active with it
        if(selectedSource == selectedDestination){

          //Reset location select box and remove source affiliation with both classroom and location
          var sourceBuilding = document.getElementById("formSource");
          sourceBuilding.selectedIndex = 0;
          removeClasses(selectedSource, "source");
        }

        //Otherwise, keep the classrooms open, but reset the select box
        else{

          //Reset classroom select box
          var classSelect = document.getElementById("classroomsource");
          classSelect.selectedIndex = 0;
        }

        //Remove classroom information
        classroomBlock.classList.remove("sourceClassActive");
        sourceClassroom = ""; 
      }

      //If destination classroom is clicked, deselect it
      else if(destinationClassroom == classroomBlock.id){

        //If source and destination buildings are the same, remove entire building from destination
        //as it will remain open due to the source object being active with it
        if(selectedSource == selectedDestination){

          //Reset location select box and remove destination affiliation with both classroom and location
          var destinationBuilding = document.getElementById("formDestination");
          destinationBuilding.selectedIndex = 0;
          removeClasses(selectedDestination, "destination");
        }

        //Otherwise, keep the classrooms open, but reset the select box
        else{

          //Reset classroom select box
          var classSelect = document.getElementById("classroomdestination");
          classSelect.selectedIndex = 0;
        }

        //Remove classroom information
        classroomBlock.classList.remove("destinationClassActive");
        destinationClassroom = ""; 
      }

      //Otherwise, a third classroom selection was attempted
      else{
        alert("Only select 2 locations");      
      }
      manageHeader();
    }
  });
}

/**
 * Adds an event listener to a classroom block that ensures select box changes are 
 * coordinated with the rest of the interactive selection methods
 * @param classroomSelect Select box of the specific building type
 * @param buildingType either source or destination classroom type
 */
function classroomUpdate(classroomSelect, buildingType){

  //Listen for any change in the select box value
  classroomSelect.addEventListener("change", function(){

    //If source classroom select box is changed
    if(buildingType == "source"){

      //If there is a current source classroom, remove styles
      if(sourceClassroom){
        var roomBlock = document.getElementById(sourceClassroom);
        roomBlock.classList.remove("sourceClassActive");
      }
  
      //Update monitoring variable and styles of new selection
      sourceClassroom = classroomSelect.value;
      var roomBlock = document.getElementById(sourceClassroom);
      roomBlock.classList.add("sourceClassActive");
    }

    //If destination classroom select box is changed
    else{

      //If there is a current destination classroom, remove styles
      if(destinationClassroom){
        var roomBlock = document.getElementById(destinationClassroom);
        roomBlock.classList.remove("destinationClassActive");
      }
  
      //Update monitoring variable and styles of new selection
      destinationClassroom = classroomSelect.value;
      var roomBlock = document.getElementById(destinationClassroom);
      roomBlock.classList.add("destinationClassActive");
    }
  });
}

/**
 * Ensure that the data sent to result.php is in the correct format to 
 * proceed with the pathfinding algorithm
 * @returns True if in correct format, else False
 */
function validatePath(){

  //Need a selection for both location types
  if(!selectedDestination || !selectedSource){
    alert("Must have a selection for both source and destination");
    return false;
  }
  
  //Ensure source location is not the same as destination
  if(selectedDestination == selectedSource && destinationClassroom == sourceClassroom){
    alert("Source and Destination cannot be the same location");
    return false;
  }

  //Otherwise, store parameters for immediate access and return true
  localStorage.setItem("source", selectedSource);
  localStorage.setItem("destination", selectedDestination);
  localStorage.setItem("sourceRoom", sourceClassroom);
  localStorage.setItem("destinationRoom", destinationClassroom);
  return true;
}
