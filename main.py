from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        # frames tick (60) / (per 1s)
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("GAME OVER")
                sys.exit()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
