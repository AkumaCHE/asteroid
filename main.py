# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #field = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    #print(f"Screen Initialised: {pygame.display.get_init()}")
    # set_mode(size=(0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    #GAME LOOP START
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        
        #player.update(dt)
        updatable.update(dt)

        for asteroid in asteroids:
            #print(asteroid.radius)
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            
        
        # FILL SCREEN BLACK        
        pygame.Surface.fill(screen,(0,0,0))
        
        # DRAW PLAYER ON SCREEN
        #player.draw(screen)
        # Draw grouped objects
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()