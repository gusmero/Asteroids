from pygame.math import Vector2
from pygame.transform import rotozoom
import sys
import pygame
from pygame.math import Vector2
from utils import get_random_position, load_sprite, print_text

#for loading sprite
from utils import get_random_velocity, load_sound, load_sprite, wrap_position
UP = Vector2(0, -1)


class Game:
    MIN_ASTEROID_DISTANCE = 250
    def __init__(self) -> None:
        self._init_pygame()
        self.menu_mode=False
        self.screen = pygame.display.set_mode((800, 600))
        self.background=load_sprite("startMenu", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""

        self.asteroids = []
        self.bullets = []
        self.game_object=[]
        self.spaceship = None
        self.buttons = None
        #initiliazation
        self.in_menu_mode()
    
    def in_menu_mode(self):
        self.menu_mode=True
        self.screen = pygame.display.set_mode((800, 600))
        self.background=load_sprite("startMenu", False)
        self.buttons = Button((400,300))

        self._set_game_object()

    def in_play_mode(self):
        self.menu_mode=False
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""

        self.asteroids = []
        self.bullets = []
        self.spaceship = None
        self.buttons = Button((400,300))

        self.populate_game()
        self._set_game_object()
        

    # pygame initialization
    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks") 


    def _set_game_object(self):
        if self.menu_mode:
            self.game_object=[self.buttons]
        else:
            self.game_object=[*self.asteroids, *self.bullets]
            if self.spaceship:
                self.game_objects.append(self.spaceship)    


   # retriving game's object
    def _get_game_objects(self):
        self.game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            self.game_objects.append(self.spaceship)
        # game_objects.append(self.buttons)
        return self.game_objects

    def populate_game(self):
        self.spaceship=Spaceship((400, 300), self.bullets.append)
        for _ in range(1):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break
            self.asteroids.append(Asteroid(position, self.asteroids.append))


class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius



#########################################################################

class Spaceship(GameObject):

    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.laser_sound = load_sound("laser")
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)
        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)
        self.laser_sound.play()


##############################################################################
class Asteroid(GameObject):
    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size

        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)

        super().__init__(
            position, sprite, get_random_velocity(1, 3)
        )

    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)

##################################################################################
class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("bullet"), velocity)

    def move(self, surface):
        self.position = self.position + self.velocity


###################################################################################
class Button(GameObject):
    def __init__(self,position ):
        velocity =Vector2(0, 0)
        super().__init__(position, load_sprite("button"),velocity )
      
