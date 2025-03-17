# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main(): 
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	# After changing a static field like containers, make sure to create all objects after the change
	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables)
	asteroidfield = AsteroidField()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill(BLACK)
		updatables.update(dt)
		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				return
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
