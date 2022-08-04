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


# Game Play


# Architecture
GameObject class as abstract factory of Spaceship ,Asteroids and bullet

# Problem encoutered
### pylint build error code 30
