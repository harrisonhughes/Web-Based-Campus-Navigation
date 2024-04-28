<?php

  //Clean form entries to prevent html script injection attacks
  function test_input($string) {
    $string = trim($string);
    $string = stripslashes($string);
    $string = htmlspecialchars($string);
    return $string;
  }

  //Inidcator for a route diretly to a building instead of inside
  $NO_CLASSROOM = -1;

  //A submission from app.php has been placed
  if($_SERVER["REQUEST_METHOD"] == "POST"){

    //Prevent PHP injection when retrieving location names from app.php
    $source =  test_input($_POST['formSource']);
    $dest = test_input($_POST['formDestination']);
    
    //Initialize classroom variables from previous page if applicable
    $sourceRoom = $NO_CLASSROOM;
    if(isset($_POST['classroomsource'])){
      $sourceRoom = test_input($_POST['classroomsource']);
    }
    $destRoom = $NO_CLASSROOM;
    if(isset($_POST['classroomdestination'])){
      $destRoom = test_input($_POST['classroomdestination']);
    }

    //Call external python pathfinding algorithm with values from app.php
    $json =json_decode(exec("AStar.py \"$source\" \"$dest\" $sourceRoom $destRoom"));
    //Retrieve optimal route (svg path specification)
    $route = $json[0];

    //Retrieve path distance and convert SVG pixels to miles based on calculated conversion rate
    $SVGTOMILES = 0.0004125;
    $distance = $json[1] * $SVGTOMILES;
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

  //If the source location has a specified classroom, be sure to draw the classrooms for this building
  if($sourceRoom != $NO_CLASSROOM){

    //Retrieve file corresponding to classroom paths of source building
    $building = 'textFiles/' . $source . '.txt';
    $classroomFile = fopen($building, "r") or die("Error opening {$building}");

    //Parse each row from slash-separated entries to array-based storage for easier access
    $sourceClassrooms = [];
    while(!feof($classroomFile)){
      $sourceClassrooms[] = explode('/', fgets($classroomFile));
    }
    fclose($classroomFile);
  }

  //If the destination location has a specified classroom, be sure to draw the classrooms for this building
  //Note that we do not need to retrieve the file again if the destination building is the same as the source
  if($destRoom != $NO_CLASSROOM && $dest != $source){

    //Retrieve file corresponding to classroom paths of source building
    $building = 'textFiles/' . $dest . '.txt';
    $classroomFile = fopen($building, "r") or die("Error opening {$building}");

    //Parse each row from slash-separated entries to array-based storage for easier access
    $destClassrooms = [];
    while(!feof($classroomFile)){
      $destClassrooms[] = explode('/', fgets($classroomFile));
    }
    fclose($classroomFile);
  }

  fclose($pathFile);
  fclose($lotFile);
  fclose($buildingFile);
  fclose($blockFile);
?>
<!DOCTYPE html>
<html id='result'>
  <head>
    <meta charset="utf-8" />
    <title>Truman State Nav</title>
    <link rel="stylesheet" href="app.css" media="screen and (max-width:768px)" />
    <link rel="stylesheet" href="app.css" media="screen and (min-width:769px)" />
    <script src="result.js"></script>
  </head>
  <body>
    <header>
      <div id="source">
        <h1>Source</h1>
        <div id="sourceSelect">
          <h2 id="sourceResult"><?php echo $source;?></h2>
          <?php
              //If classroom was specified, display it in header
              if($sourceRoom != $NO_CLASSROOM){
                echo "<h2 id='sourceRoomResult'>{$sourceRoom}</h2>";
              }
            ?>
        </div>
      </div>
      <div id="destination" class="destinationResult">
        <div id="destinationSelect">
            <h2 id="destinationResult"><?php echo $dest;?></h2>
            <?php
              //If classroom was specified, display it in header
              if($destRoom != $NO_CLASSROOM){
                echo "<h2 id='destinationRoomResult'>{$destRoom}</h2>";
              }
            ?>
          </div>
          <h1>Destination</h1>
        </div>
      </div>
      <form action="app.php" method="post">
        <fieldset id="buttons">
            <input id="mapReset" type="submit" value="Clear"/>
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
      <svg id="map" width="100%" height="100%" viewBox="0 0 1093 1117" preserveAspectRatio="xMidYMid meet" >
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
              "<g class='structure";
              
              //If this lot is the source or destination, style it as such
              if($source == $lot[0]){
                echo " sourceActive";
              }
              else if($dest == $lot[0]){
                echo " destinationActive";
              } 
              
              echo "' id='{$lot[0]}'>
              <path transform='translate({$lot[1]},{$lot[2]})'
              class='lot'
              d='{$lot[3]}'/>
              </g>";
            }

            foreach($buildings as $building){
              $VALID_BUILDING = 1;
              $SHADOW_OFFSET = 1.5;

              $height = floatVal($building[3]);
              $shadowHeight = floatVal($building[3]) + $SHADOW_OFFSET;

              if($building[0] == $VALID_BUILDING){
                echo "<g class='structure";

                //If this building is the source, style it as such
                if($source == $building[1]){
                  if($sourceRoom == $NO_CLASSROOM){
                    echo " sourceActive";
                  }
                  else{
                    echo " buildingInterior";
                  }
                }

                //If this building destination, style it as such
                else if($dest == $building[1]){
                  if($destRoom == $NO_CLASSROOM){
                    echo " destinationActive";
                  }
                  else{
                    echo " buildingInterior";
                  }
                } 
              }

              echo "' id='{$building[2]}'>
              <path transform='translate({$building[2]},{$shadowHeight})'
                class='buildingShadow'
                d='{$building[4]}'/>
              <path transform='translate({$building[2]},{$height})'
                class='building'
                d='{$building[4]}'/>
              </g>";
            }

            //Draw classrooms on source building if applicable
            if(!empty($sourceClassrooms)){
              echo "<g>";
              foreach($sourceClassrooms as $classroom){
                echo "<path id={$classroom[0]} 
                        class='classroom";

                        //If current classroom is source or destination room, style as such
                        if($classroom[0] == $sourceRoom){
                          echo " sourceClassActive";
                        }
                        else if($classroom[0] == $destRoom){
                          echo " destinationClassActive";
                        }
                        echo "'d='$classroom[3]'
                        transform='translate({$classroom[1]},{$classroom[2]})'/>";
              }
              echo "</g>";
            }

            //Draw classrooms on destination building if applicable
            if(!empty($destClassrooms)){
              echo "<g>";
              foreach($destClassrooms as $classroom){
                echo "<path id={$classroom[0]} 
                        class='classroom";

                        //If current classroom is destination room, style as such
                        if($classroom[0] == $destRoom){
                          echo " destinationClassActive";
                        }
                        echo "'d='$classroom[3]'
                        transform='translate({$classroom[1]},{$classroom[2]})'/>";
              }
              echo "</g>";
            }
    
            //Display route through animation bubbles 
            if($route){
              $CIRCLES_PER_SECOND = 12;
              $TIME_FACTOR = 25; //Relative speed multiplier for route
              $MIN_ROUTE_TIME = 1;

              echo "<path
              id='motionPath'
              class='route'
              d='{$route}'/>";

              //Calculate total route time and round to create even bubble spacing
              $time = round($distance * $TIME_FACTOR,0);

              //Ensure minimum route time is met
              if($time < $MIN_ROUTE_TIME){
                $time = $MIN_ROUTE_TIME;
              }

              //Space circles by CPS factor, and begin drawing route
              $numCircles = $CIRCLES_PER_SECOND * $time; 
              for ($i = 0; $i < $numCircles; $i++) {

                //Evenly space route bubbles, and create animated path for each one
                $delay = $i / $CIRCLES_PER_SECOND;                
                echo "<circle r='2' class='routeBubbles'>
                        <animateMotion dur='{$time}s' repeatCount='indefinite' begin='{$delay}s'>
                          <mpath xlink:href='#motionPath' />
                        </animateMotion>
                      </circle>";
              }
            }
        ?>
      </svg>
      <div id="distance">
        <h2>Distance: 
          <?php
            //Display estimated distance of route based on most applicable unit of distance
            $MILES_TO_FEET = 5280;
            $unit = " Miles";
            if($distance < 0.1){
              $distance *= $MILES_TO_FEET;
              $unit = " Feet";
            }
            echo round($distance,2) . $unit; 
          ?>
        </h2>
      </div>
    </main>
    <footer>
    </footer>
  </body>
</html>