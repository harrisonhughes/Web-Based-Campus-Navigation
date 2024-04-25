<?php
  if(isset($_GET['building'])){
    $building = $_GET['building'] . '.txt';
    $buildingFile = fopen($building, "r") or die("Error opening {$building}");

    $classrooms = [];
    while(!feof($buildingFile)){
      $classrooms[] = explode('/', fgets($buildingFile));
    }

    $javascriptOutput = json_encode($classrooms);
    echo $javascriptOutput;

    exit();
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
    if($building[0] == 1){
      $locations[] = $building[1];
    }
  }
  foreach($lots as $lot){
    $locations[] = $lot[0];
  }
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
                <option disabled selected value>Location</option>
                <?php 
                foreach($locations as $location){
                    echo "<option value='{$location}'>{$location}</option>";
                }
                ?>
              </select>
            </div>
          </div>
          <div id="destination" class="destinationHide">
            <div id="destinationSelect">
              <select name ="formDestination" id="formDestination">
                <option disabled selected value>Location</option>
                <?php 
                foreach($locations as $location){
                  echo "<option value='{$location}'>{$location}</option>";
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
        <button type="button" id="changeView">[ ]</h1>
      </div>
      <img id="picture" src="Earth.png">
      <svg id="map" svg width="100%" viewBox="0 0 1093 1117" preserveAspectRatio="xMidYMid meet" >
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
              foreach($blocks as $block){
                if($block[0][0] != '#'){
                  echo "<path transform='translate({$block[0]},{$block[1]})'
                  class='blockOutline'
                  d='{$block[2]}'/>";
                }
              }

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
              "<g title='{$lot[0]}' class='structure";
              
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
              if($building[0] == 1){
                $structure = 'structure';
                $class = 'building';
                $classShadow = 'buildingShadow';
              }
              else{
                $structure = 'dummyStructure';
                $class = 'dummy';
                $classShadow = 'dummyShadow';
              }

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
            fclose($paths);
            fclose($lots);
            fclose($buildings);
        ?>
      </svg>
    </main>
    <footer>
    </footer>
  </body>
</html>