<?php
  if($_SERVER["REQUEST_METHOD"] == "POST"){
    $source = $_POST['formSource'];
    $dest = $_POST['formDestination'];
    $route = exec("AStar.py $source $dest");
  }
  $pathFile = fopen("paths.txt", "r") or die("Error opening paths.txt");
  $lotFile = fopen("lots.txt", "r") or die("Error opening lots.txt");
  $buildingFile = fopen("buildings.txt", "r") or die("Error opening buildings.txt");

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

  $locations = [];
  foreach($buildings as $building){
    $locations[] = $building[0];
  }
  foreach($lots as $lot){
    $locations[] = $lot[0];
  }
?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Truman State Nav</title>
    <link rel="stylesheet" href="app.css" media="screen and (max-width:768px)" />
    <link rel="stylesheet" href="app.css" media="screen and (min-width:769px)" />
    <script src="app.js"></script>
  </head>
  <body>
    <header>
      <form onsubmit="return validatePath(event)" action="app.php" method="post" id="userSelection">
        <fieldset>
          <div>
            <select name ="formSource" id="formSource">
              <option disabled selected value>Starting Location &#x25BC</option>
              <?php 
                foreach($locations as $location){
                  echo "<option value='{$location}'>{$location}</option>";
                }
              ?>
            </select>
          </div>
          <div>
            <select name ="formDestination" id="formDestination">
              <option disabled selected value>Destination &#x25BC</option>
              <?php 
                foreach($locations as $location){
                  echo "<option value='{$location}'>{$location}</option>";
                }
              ?>
            </select>
          </div>
          <input type="submit"/>
          <input id="mapReset" type="reset"/>
        </fieldset>
      </form>  
    </header>
    <main>
      <div class="sidebar">
      <button type="button" id="zoomin">&#x2B</h1>
        <button type="button" id="zoomout">&#x2212</h1>
      </div>
      <svg id="map" svg width="100%" viewBox="0 0 645 610" preserveAspectRatio="xMidYMid meet" >
        <rect class="background" width="645" height="610" x="0" y="0"/>
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
              $height = floatVal($building[2]) - 1;
              $shadowHeight = floatVal($building[2]) + 1;

              echo "<g class='structure";
              if($source == $building[0]){
                echo " sourceActive";
              }
              else if($dest  == $building[0]){
                echo " destinationActive";
              } 

              echo "' id='{$building[0]}'>
              <path transform='translate({$building[1]},{$shadowHeight})'
                class='buildingShadow'
                d='{$building[3]}'/>
              <path transform='translate({$building[1]},{$height})'
                class='building'
                d='{$building[3]}'/>
              </g>";
            }
    
            if($route){
              echo "<path
              class='route'
              d='{$route}'/>";
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