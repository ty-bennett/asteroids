from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event
import pygame
import random


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:             
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rand_ang = random.uniform(20, 50)
        a1_vec = self.velocity.rotate(rand_ang)
        a2_vec = self.velocity.rotate(-rand_ang)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_rad)
        a.velocity = a1_vec * 1.2
        a = Asteroid(self.position.x, self.position.y, new_rad)
        a.velocity = a2_vec * 1.2