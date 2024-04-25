<?php
  $SVGTOMILES = 0.0004125;

  if(isset($_GET['building'])){
    $building = $_GET['building'] . '.txt';

    if(file_exists($building)){
      $buildingFile = fopen($building, "r") or die("Error opening {$building}");

      $classrooms = [];
      while(!feof($buildingFile)){
        $classrooms[] = explode('/', fgets($buildingFile));
      }

      $javascriptOutput = json_encode($classrooms);
      echo $javascriptOutput;
    }

    exit();
  }

  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $source =  $_POST['formSource'];
    $dest = $_POST['formDestination'];
    
    $sourceRoom = '-1';
    if(isset($_POST['classroomsource'])){
      $sourceRoom = $_POST['classroomsource'];
    }
    $destRoom = '-1';
    if(isset($_POST['classroomdestination'])){
      $destRoom = $_POST['classroomdestination'];
    }

    $json =json_decode(exec("AStar.py \"$source\" \"$dest\" $sourceRoom $destRoom"));
    $route = $json[0];
    $distance = $json[1] * $SVGTOMILES;
  }

  $pathFile = fopen("paths.txt", "r") or die("Error opening paths.txt");
  $lotFile = fopen("lots.txt", "r") or die("Error opening lots.txt");
  $buildingFile = fopen("buildings.txt", "r") or die("Error opening buildings.txt");
  $blockFile = fopen("blocks.txt", "r") or die("Error opening blocks.txt");

  $paths = [];
  while(!feof($pathFile)){
    $paths[] = explode('/', fgets($pathFile));
  }

  $lots = [];
  while(!feof($lotFile)){
    $lots[] = explode('/', fgets($lotFile));
  }

  $buildings = [];
  while(!feof($buildingFile)){
    $buildings[] = explode('/', fgets($buildingFile));
  }

  $blocks = [];
  while(!feof($blockFile)){
    $blocks[] = explode('/', fgets($blockFile));
  }

  $locations = [];
  foreach($buildings as $building){
    $locations[] = $building[1];
  }
  foreach($lots as $lot){
    $locations[] = $lot[0];
  }
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
          <h2 id="sourceResult"></h2>
          <h2 id="sourceRoomResult"></h2>
        </div>
      </div>
      <div id="destination" class="destinationResult">
        <div id="destinationSelect">
            <h2 id="destinationResult"></h2>
            <h2 id="destinationRoomResult"></h2>
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
        <button type="button" id="changeView">[ ]</h1>
      </div>
      <img id="picture" src="Earth.png">
      <svg id="map" width="100%" height="100%" viewBox="0 0 1093 1117" preserveAspectRatio="xMidYMid meet" >
        <defs>
        <linearGradient id="buildingGradient">
            <stop offset="5%" stop-color="#888888" />
            <stop offset="95%" stop-color="#BBBBBB" />
          </linearGradient>
        <linearGradient id="buildingShadowGradient">
            <stop offset="5%" stop-color="#555555" />
            <stop offset="95%" stop-color="#888888" />
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
        <rect class="background" width="1093" height="1117" x="0" y="0"/>
        <?php
            foreach($paths as $path){
              if($path[0][0] != '#'){
                $strokeOutline = floatVal($path[0]) + 0.4;
                echo "<path transform='translate({$path[1]},{$path[2]})'
                class='pathOutline'
                d='{$path[3]}'
                stroke-width='{$strokeOutline}'/>";
              }
            }

            foreach($paths as $path){
              if($path[0][0] != '#'){
                echo "<path transform='translate({$path[1]},{$path[2]})'
                class='path'
                d='{$path[3]}'
                stroke-width='{$path[0]}'/>";
              }
            }
        
            foreach($blocks as $block){
              if($block[0][0] != '#'){
                echo "<path transform='translate({$block[0]},{$block[1]})'
                class='block'
                d='{$block[2]}'/>";
              }
            }

            $locations = [];

            foreach($lots as $lot){
              echo
              "<g class='structure";
              
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
              $height = floatVal($building[3]);
              $shadowHeight = floatVal($building[3]) + 1.5;

              if($building[0] != 0){
                echo "<g class='structure";
                if($source == $building[1] && $sourceRoom == -1){
                  echo " sourceActive";
                }
                else if($dest == $building[1] && $destRoom == -1){
                  echo " destinationActive";
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
    
            if($route){
              echo "<path
              id='motionPath'
              class='route'
              d='{$route}'/>";

              $time = round($distance * 25, 0);
              if($time < 5){
                $time = 5;
              }

              $CIRCLES_PER_SECOND = 8;
              $numCircles = $CIRCLES_PER_SECOND * $time; 
              for ($i = 0; $i < $numCircles; $i++) {
                $delay = $i / $CIRCLES_PER_SECOND;
                
                echo "<circle r='3' class='routeBubbles'>
                        <animateMotion dur='{$time}s' repeatCount='indefinite' begin='{$delay}s'>
                          <mpath xlink:href='#motionPath' />
                        </animateMotion>
                      </circle>";
              }
            }

            fclose($pathFile);
            fclose($lotFile);
            fclose($buildingFile);
            fclose($blockFile);
        ?>
      </svg>
      <div id="distance">
        <h2>Distance: 
          <?php
            $unit = " Miles";
            if($distance < 0.1){
              $distance *= 5280;
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