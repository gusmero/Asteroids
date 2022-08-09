from models import Game
from models import Button
import pygame 

import sys
from models import GameObject
from utils import get_random_position, load_sprite, print_text
from models import Asteroid, Spaceship

class SpaceRocks:
    

    #costructor
    def __init__(self):
        self.game= Game()
        
#########################################################################

    # scheduling process
    def main_loop(self):
        while True:
            self.game.message="Press some key"
            self._draw()
            for event in pygame.event.get():
                if pygame.KEYDOWN==event.type:
                    self.game.message=""
                    self.game.repopulate_game()
                    while self.game.spaceship and not self.game.asteroids==[]:
                        self._handle_input()
                        self._process_game_logic()
                        self._draw()

 #########################################################################

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif (
                self.game.spaceship
                and event.type == pygame.KEYDOWN
                and event.key == pygame.K_SPACE
            ):
                self.game.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        if self.game.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.game.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.game.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.game.spaceship.accelerate()



    ######################
    def _process_game_logic(self):

        # move game's object
        for game_object in self.game._get_game_objects():
            game_object.move(self.game.screen)

        # bullet asteroid collision
        for bullet in self.game.bullets[:]:
            for asteroid in self.game.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.game.asteroids.remove(asteroid)
                    self.game.bullets.remove(bullet)
                    asteroid.split()
                    break

        # 
        for bullet in self.game.bullets[:]:
            if not self.game.screen.get_rect().collidepoint(bullet.position):
                self.game.bullets.remove(bullet)

        # THE END OF GAME'S RULES
        #win
        if not self.game.asteroids and self.game.spaceship:
            self.game.message = "You won!"
        #lose
        if self.game.spaceship:
            for asteroid in self.game.asteroids:
                if asteroid.collides_with(self.game.spaceship):
                    self.game.spaceship = None
                    self.game.message = "You lost!"
                    break


    ###############
    def _draw(self):
        self.game.screen.blit(self.game.background, (0, 0))
        for game_object in self.game._get_game_objects():
            game_object.draw(self.game.screen)

        if self.game.message:
            print_text(self.game.screen, self.game.message, self.game.font)

        pygame.display.flip()
        self.game.clock.tick(60)

#####################################################################
# USEFUL METHOD

 