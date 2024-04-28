const ZOOM_RATIO = 1.2;
const WIDTH_HEIGHT_RATIO = 1117/1093;

//Default view is "map", or the digital view. "Earth" provides the satellite view
var view = "map";

//Automatic modifications and event listeners to proceed with upon loading of the webpage
document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("load", loadPosition);
  handleView();
  handleZoom();
  window.addEventListener("beforeunload", storePosition);
});

  /**
 * To store the vertical and horizontal scroll position of the page upon 
 * unloading of the webpage. This allows identical positioning to be maintained
 * when returning to app.php
 */
  function storePosition(){
    var scrollX = document.documentElement.scrollLeft;
    var scrollY = document.documentElement.scrollTop;
  
    //Save position to be accessed by app.php
    localStorage.setItem('scrollX', scrollX);
    localStorage.setItem('scrollY', scrollY);
  }
  
    /**
 * To load the vertical and horizontal scroll position of the page upon 
 * DOM loading of the webpage. This allows identical positioning to be maintained when 
 * navigating from app.php
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
 * Coordinate initial zoom level with that of the app.php file upon navigation, 
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
  var main = document.getElementById("result");
  const changeView = document.getElementById("changeView");

  //Set view to satellite if it was stored by app.php
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