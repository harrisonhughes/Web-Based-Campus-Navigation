# Web Based Campus Navigation
## Premise
This application provides a comprehensive view of Truman State's campus both digitally, and from a satellite view; the primary functionality revolves around the pathfinding feature. This interactive application allows the selection of any two campus locations, either building or parking lot, by a traditional select option or by clicking directly on the map. After your source and destination locations are active, press 'search' to be presented with an optimal route generated on demand. Whether you want to learn how to navigate campus or are simply trying to optimize your daily routine, this application is for you! Feel free to download and extend this open source program to provide even more benefits to the students of Truman State University!

## Programs and Dependencies
Tech:   
-Local Web Server (Apache Recommended)  
-Python (3.11.0+ Recommended)  
-PHP (8.0+ Recommended)  
-JavaScript  
-CSS  
  
Dependencies:  
-SVGPathTools (Python Extension)

## Recommended Installation Steps
The easiest way to begin the process is to download a web development stack onto your local environment. MAMP is recommended, as this is the stack I used in my testing. 
### Step 1 - MAMP Installation
Navigate to https://www.mamp.info/en/downloads/ and begin downloading/installing the MAMP version specific to your platform. You will not need MAMP Pro. No special installation information is necessary - MAMP should be downloaded to the location C:\MAMP by default.

### Step 2 - Configure MAMP
Navigate to the location MAMP is downloaded and launch the application. The MAMP dashboard (The initial small initial interface that displays server status) allows for further configuration using the dropdown menus at the top of the screen, including specification of the web server (Apache recommended), PHP version (8.0+ recommended), and port information. This would be a good time to familiarize yourself with the MAMP dashboard, and to ensure that these values, while active by default, are accurate.

### Step 3 - Setting up the Environment
The MAMP web development stack is configured to run files from the folder MAMP/htdocs - naturally, this is where the application needs to be. In the command line, navigate to the htdocs folder within your MAMP parent folder. By default this will be  
  
$ cd C:\MAMP\htdocs  
  
but you may have specified an alternate location upon installation. Next, WHILE IN THE HTDOCS REPOSITORY in the CLI, run the command  
  
$ git clone https://github.com/harrisonhughes/Web-Based-Campus-Navigation.git  
  
in order to download the application itself to the correct location. By now, you should have a MAMP web development stack on your personal device, and the application files should be present in the htdocs folder of your MAMP environment. The next step is to download Python onto your personal device to ensure the pathfinding algorithm can run. I recommend navigating to  

https://www.python.org/downloads/
  
and downlaoding at least Python version 3.11.0. This should also automatically download the Python package manager 'pip' which will be needed later. 

### Step 4 - Connect the Application to MAMP
Now, in the MAMP dashboard (again, the small initial interface that displays server status), click on the MAMP heading at the top of the page, and select 'Preferences'. You should now be given the option to provide 'My favorite link', which must be selected from the htdocs folder. In this text box, write in  
  
Web-Based-Campus-Navigation/app.php  
  
thus pointing the stack directly at the application you just downloaded. Be sure to select 'OK'. You should return to the original MAMP dashboard, and select 'Start Servers' to proceed to the final step. 
  
Note: you will need the 'Apache Server' to turn green in order to proceed, but the 'MySQL Server' and 'Cloud' indicator need not be active. 

### Step 5 - Install SVGPathTools and Begin Searching
The final step is to download the Python library 'SVGPathTools' to ensure the Python file has the necessary dependencies to run. This can be accomplished most simply through the Python package manager 'pip'. This is as easy as  

$ pip install svgpathtools  
  
Now you can navigate to the MAMP webstart page and click the 'My Favorite Link' tab to begin optimizing your daily routine!


