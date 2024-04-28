<?php
  //Clean form entries to prevent html script injection attacks
  function test_input($string) {
    $string = trim($string);
    $string = stripslashes($string);
    $string = htmlspecialchars($string);
    return $string;
  }
  
  $VALID_BUILDING = 1;

  /**
   * If the filename passed over from an ajax XML request exists, parse the contents
   * of the file and send it back to JavaScript as a JSON string. This means that the 
   * building that has just been selected has a file to support interior classroom
   * navigation.
   */
  if(isset($_GET['building'])){

    //Prevent PHP script injection attack from GET variable
    $cleanedFile = test_input($_GET['building']);

    //Build file location and check if it exists
    $building = 'textFiles/' . $cleanedFile . '.txt';
    if(file_exists($building)){
      $buildingFile = fopen($building, "r") or die("Error opening {$building}");

      //Make each row (individual classroom) its own array variable
      $classrooms = [];
      while(!feof($buildingFile)){
        $classrooms[] = explode('/', fgets($buildingFile));
      }
  
      //JSON encode array of classroom arrays to send back to JavaScript for client-side display
      $javascriptOutput = json_encode($classrooms);
      echo $javascriptOutput;
      fclose($buildingFile);
    }
    exit();
  }

  //Open all files containing map structure specifications
  $pathFile = fopen("textFiles/paths.txt", "r") or die("Error opening paths.txt");
  $lotFile = fopen("textFiles/lots.txt", "r") or die("Error opening lots.txt");
  $buildingFile = fopen("textFiles/buildings.txt", "r") or die("Error opening buildings.txt");
  $blockFile = fopen("textFiles/blocks.txt", "r") or die("Error opening blocks.txt");

  //Parse each row from slash-separated entries to array-based storage for easier access
  $paths = [];
  while(!feof($pathFile)){
    $paths[] = explode('/', fgets($pathFile));
  }
  $blocks = [];
  while(!feof($blockFile)){
    $blocks[] = explode('/', fgets($blockFile));
  }
  $lots = [];
  while(!feof($lotFile)){
    $lots[] = explode('/', fgets($lotFile));
  }
  $buildings = [];
  while(!feof($buildingFile)){
    $buildings[] = explode('/', fgets($buildingFile));
  }

  //Close all files; we have extracted all information 
  fclose($pathFile);
  fclose($blockFile);
  fclose($lotFile);
  fclose($buildingFile);
?>
<!DOCTYPE html>
<html id='page'>
  <head>
    <meta charset="utf-8" />
    <title>Truman State Nav</title>
    <link rel="stylesheet" href="app.css" media="screen and (max-width:768px)" />
    <link rel="stylesheet" href="app.css" media="screen and (min-width:769px)" />
    <script src="app.js"></script>
  </head>
  <body>
    <header>
      <form onsubmit="return validatePath()" action="result.php" method="post" id="userSelection">
        <fieldset>
          <div id="source">
            <h1>Source</h1>
            <div id="sourceSelect">
              <select name ="formSource" id="formSource">
                <option class='optionHeader' selected disabled>Buildings</option>
                <?php 
                  //Populate select box with all specified building names
                  foreach($buildings as $building){
                      if($building[0] == $VALID_BUILDING){
                        echo "<option value='{$building[1]}'>{$building[1]}</option>";
                      }
                  }
                  ?>
                  <option class='optionHeader' disabled>Parking Lots</option>
                  <?php 
                  //Populate select box with all lot names
                  foreach($lots as $lot){
                    echo "<option value='{$lot[0]}'>{$lot[0]}</option>";
                  }
                ?>
              </select>
            </div>
          </div>
          <div id="destination" class="destinationHide">
            <div id="destinationSelect">
              <select name ="formDestination" id="formDestination">
              <option class='optionHeader' selected disabled>Buildings</option>
                <?php 
                  //Populate select box with all specified building names
                  foreach($buildings as $building){
                      if($building[0] == $VALID_BUILDING){
                        echo "<option value='{$building[1]}'>{$building[1]}</option>";
                      }
                  }
                  ?>
                  <option class='optionHeader' disabled>Parking Lots</option>
                  <?php 
                  //Populate select box with all lot names
                  foreach($lots as $lot){
                    echo "<option value='{$lot[0]}'>{$lot[0]}</option>";
                  }
                ?>
              </select>
            </div>
            <h1>Destination</h1>
          </div>
          <div id="buttons">
            <input type="submit" id="mapSubmit" value="Search" class="hideElement"/>
            <input id="mapReset" type="reset" value="Clear" class="hideElement"/>
          </div>
        </fieldset>
      </form>  
    </header>
    <main>
      <div class="sidebar">
      <button type="button" id="zoomin">&#x2B</h1>
        <button type="button" id="zoomout">&#x2212</h1>
        <button type="button" id="changeView">&#x1F441</h1>
      </div>
      <img id="picture" src="Earth.png">
      <!--Magic Numbers to specify the total height and width of the SVG file-->
      <svg id="map" svg width="100%" viewBox="0 0 1093 1117" preserveAspectRatio="xMidYMid meet" >
        <defs>
        <linearGradient id="buildingGradient">
            <stop offset="5%" stop-color="#999999" />
            <stop offset="95%" stop-color="#CCCCCC" />
          </linearGradient>
          <linearGradient id="sourceGradient">
            <stop offset="5%" stop-color="#510c76" />
            <stop offset="95%" stop-color="#b565e0" />
          </linearGradient>
          <linearGradient id="destinationGradient">
            <stop offset="5%" stop-color="#b48f52" />
            <stop offset="95%" stop-color="#87714D" />
          </linearGradient>
          <linearGradient id="classroomGradient">
            <stop offset="5%" stop-color="#e8f0f4" />
            <stop offset="95%" stop-color="#ddeff6" />
          </linearGradient>
        </defs>
        <?php
            //Draw all map paths based on specifications from file
            foreach($paths as $path){
              //If current row doesn't begin with a comment symbol
              if($path[0][0] != '#'){
                echo "<path transform='translate({$path[1]},{$path[2]})'
                class='path'
                d='{$path[3]}'
                stroke-width='{$path[0]}'/>";
              }
            }

            //Draw all irregular map shapes based on specifications from file
            foreach($blocks as $block){
              //If current row doesn't begin with a comment symbol
              if($block[0][0] != '#'){
                echo "<path transform='translate({$block[0]},{$block[1]})'
                class='block'
                d='{$block[2]}'/>";
              }
            }

            //Draw all map lots based on specifications from file
            foreach($lots as $lot){
              echo
              "<g title='{$lot[0]}' class='structure'
               id='{$lot[0]}'>
              <path transform='translate({$lot[1]},{$lot[2]})'
              class='lot'
              d='{$lot[3]}'/>
              </g>";
            }

            //Draw all map buildings based on specifications from file
            foreach($buildings as $building){
              $SHADOW_OFFSET = 1.5;

              //Specify building height, and specify a vertical offset height to simulate a shadow
              $height = floatVal($building[3]);
              $shadowHeight = floatVal($building[3]) + $SHADOW_OFFSET;
              
              //Allow valid buildings to have interactive properties
              if($building[0] == $VALID_BUILDING){
                $structure = 'structure';
                $class = 'building';
                $classShadow = 'buildingShadow';
              }

              //Dummy buildings should have static properties
              else{
                $structure = 'dummyStructure';
                $class = 'dummy';
                $classShadow = 'dummyShadow';
              }

              //Create group to hold both building and the replica shadow building
              echo "<g class='{$structure}' 
              id='{$building[1]}'>
              <path transform='translate({$building[2]},{$shadowHeight})'
                class='{$classShadow}'
                d='{$building[4]}'/>
              <path transform='translate({$building[2]},{$height})'
                class='{$class}'
                d='{$building[4]}'/>
              </g>";
            }
        ?>
      </svg>
    </main>
    <footer>
    </footer>
  </body>
</html>