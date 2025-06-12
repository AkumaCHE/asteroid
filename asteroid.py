from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.x = x
        #self.y = y
        #self.radius = radius
        #self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #print("this was a small asteroid")
            return
        else:
            asteroid_split_rotation = random.uniform(20,50)
            print(self.velocity)
            split_a = pygame.math.Vector2.rotate(self.velocity, asteroid_split_rotation) 
            split_b = pygame.math.Vector2.rotate(self.velocity, - asteroid_split_rotation) 
            #print(f"split a: {split_a}")
            #print(f"split b: {split_b}")
            new_asteroid_a = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS) 
            new_asteroid_b = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_a.velocity = split_a * 1.2
            new_asteroid_b.velocity = split_b * 1.2


