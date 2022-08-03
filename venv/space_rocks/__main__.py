from game import SpaceRocks


#  create a __main__.py file in your space_rocks folder. 
# This file will take care of creating a new instance of 
# your game and starting it by running main_loop()
if __name__ == "__main__":
    space_rocks = SpaceRocks()
    space_rocks.main_loop()