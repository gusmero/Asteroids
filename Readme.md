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
```


### Managing package command 
```sh
# update pip package
 python -m pip install --upgrade pip
# update app's package
 python -m pip install -r requirements.txt

```


# Game Play


# Problem encoutered
### pylint build error code 30
