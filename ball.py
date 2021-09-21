import pygame, random

class Ball:
	position = pygame.Vector2()
	velocity = pygame.Vector2()
	velocity.xy = random.choice([-1, 1])*5, random.choice([-1, 1])*5
	rect = pygame.Rect(position, (35,35))
