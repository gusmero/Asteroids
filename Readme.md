## python enviroment set up

python enviroment tutorial
A Python virtual environment is a folder structure that gives you everything you need to run a lightweight yet isolated Python environment. When you create a new virtual environment using the venv module, Python creates a self-contained folder structure and copies or symlinks the Python executable files into that folder structure.
[Tutorial python enviroment](https://realpython.com/python-virtual-environments-a-primer/)
```s
venv\
│
├── Include\
│
├── Lib\
│   │
│   └── site-packages\
│       │
│       ├── _distutils_hack\
│       │
│       ├── pip\
│       │
│       ├── pip-22.0.4.dist-info\
│       
│
│
├── Scripts\
│   ├── Activate.ps1
│   ├── activate
│   ├── activate.bat
│   ├── deactivate.bat
│   ├── pip.exe
│   ├── pip3.10.exe
│   ├── pip3.exe
│   ├── python.exe
│   └── pythonw.exe
│
└── pyvenv.cfg
```
* The **pyvenv.cfg** is a configuration file which stores information about the virtual environment such as Python interpreter(wich version) and which site-packages directory the current Python session will use. 
* **Include** is an initially empty folder that Python uses to include C header files for packages you might install that depend on C extensions.
* **Script** contains the executable files of your virtual environment. Most notable are the Python interpreter (python.exe), the pip executable (pip.exe), and the activation script for your virtual environment, which comes in a couple of different flavors to allow you to work with different shells.
* **Lib** contains the site-packages\ folder, which is one of the main reasons for creating your virtual environment. This folder is where you’ll install external packages that you want to use within your virtual environment. You can see them also with  ```sh python -m pip list```.

You want to achieve an isolated environment so that any external packages you install won’t conflict with global site-packages. What venv does to make this possible is to reproduce the folder structure that a standard Python installation creates.

This structure accounts for the location of the copy or **symlink**(Symbolic link) of the Python binary and the site-packages directory, where Python installs external packages


Asteroids tutorial
[Tutorial Asteroids game](https://realpython.com/asteroids-game-python/#:~:text=%20Build%20an%20Asteroids%20Game%20With%20Python%20and,window%20that%20you%20can%20close%20by...%20More%20)





### Enviroment creation
```sh
# create a visrtual enviroment
 python -m venv venv
# activate visrtual enviroment
 venv\Scripts\activate
# deactivate virtual enviroment
 deactivate
# installing package inside python virtual enviroment
 python -m pip install <package-name>
# show all package installed
 python -m pip list
#python version
 python --version
# print folder structure
 gci -Directory | select parent, name | sort parent
 tree venv /F
  ```
    
```sh
Package           Version
----------------- -------
astroid           2.11.7
#Makes ANSI escape character sequences (for producing colored terminal text and cursor positioning) work under MS Windows.
colorama          0.4.5
dill              0.3.5.1
isort             5.10.1
lazy-object-proxy 1.7.1
mccabe            0.7.0
pip               22.2.1
# When writing desktop application, finding the right location to store user data and configuration varies per platform. Even for single-platform apps, there may by plenty of nuances in figuring out the right location.
platformdirs      2.5.2
# pygame is a free and open-source cross-platform library for the development of multimedia applications like video games using Python. It uses the Simple DirectMedia Layer library and several other popular libraries to abstract the most common functions, making writing these programs a more intuitive task. 
pygame            2.1.2
# Pylint is a static code analyser for Python 2 or 3 .Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored. Pylint can infer actual values from your code using its internal code representation (astroid)
pylint            2.14.5
setuptools        58.1.0
tomli             2.0.1
tomlkit           0.11.1
wrapt             1.14.1
# python eviroment
python            3.10.2
```

### Some command routine
```sh
# visual studio code script policy
 Set-ExecutionPolicy -ExecutionPolicy ByPass -Scope Process
# activate python virtual enviroment
 venv\Scripts\activate
# command for run application
 python ./venv/space_rocks
# running test 
 python -m unittest discover -s "./venv/space_rocks/test" -p "test_*.py" -v # Verbose testing
# pylint analisys
 pylint ./venv/space_rocks/
  pylint ./venv/space_rocks/ --output-format=json:somefile.json,colorized
```


### Managing package command 
```sh
# update pip package
 python -m pip install --upgrade pip
# update app's package
 python -m pip install -r requirements.txt

```
# Architecture
The choice of **MVC** should be pretty obvious where a graphical game is concerned. The primary Model will be discussed later under the heading The Game Model. The primary **View** will be a PyGame window displaying graphics on the monitor. The primary **Controller** will be the keyboard, supported by PyGame's internal pygame.event module.

![Data Model](/readme_img/ClassDiagram.JPG)

#### The Game Model

**Game**
Game is mainly a container object. It contains the Players and the Maps. It might also do things like Start() and Finish() and keep track of whose turn it is.

**Player**
A Player object represents the actual human (or computer) that is playing the game. Common attributes are Player.score and Player.color. Don't confuse it with Charactor. Pac Man is a Charactor, the person holding the joystick is a Player.

**Charactor**
A Charactor is something controlled by a player that moves around the Map. Synonyms might be "Unit" or "Avatar". It is intentionally spelled "Charactor" to avoid any ambiguity with Character which can also mean "a single letter" (also, you cannot create a table in PostgreSQL named "Character"). Common Charactor attributes are Charactor.health and Charactor.speed.

In our example, "little man" will be our sole Charactor.

**Map**
A Map is an area that Charactors can move around in. There are generally two kinds of maps, discrete ones that have Sectors, and continuous ones that have Locations. A chess board is an example of a discrete map. The screen in Scorched Earth, or a level in Super Mario are examples of continuous Maps.

In our example, the Map will be a discrete Map having a simple list of nine sectors.

**Sector**
A Sector is part of a Map. It is adjacent to other sectors of the map, and might have a list of any such neighbors. No Charactor can be in between Sectors. If a Charactor is in a Sector, it is in that sector entirely, and not in any other Sector (I'm speaking functionally here. It can look like it is in between Sectors, but that is an issue for the View, not the Model)

In our example, we will allow no diagonal moves, only up, down, left and right. Each allowable move will be defined by the list of neighbors for a particular Sector, with the middle Sector having all four.

**Location**
We won't get into Locations of a continuous Map, as they don't apply to our example.

**Item**
You'll notice that Item is not explicitly connected to anything. This is left up to the developer. You could have a design constraint that Items must be contained by Charactors (perhaps in an intermidiate "Inventory" object), or maybe it makes more sense for your game to keep a list of a bunch of Items in the Game object. Some games might call for Sectors having Items lying around inside them

# Architecture
GameObject class as abstract factory of Spaceship ,Asteroids and bullet

# Problem encoutered
### pylint build error code 30
