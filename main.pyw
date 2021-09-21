import pygame
import math
import sys
import time
import utils
from ball import Ball
from player import Player, Player2

screenX, screenY = 950, 600

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("assets/sprite/icon.png"))
clock = pygame.time.Clock()
white = (255, 255, 255)
pygame.init()
score_limit = 10

#objects
ball = Ball()
ball.rect.x = screenX/1.5-50
ball.rect.y = screenY/1.5-50

player1 = Player()
player1.rect.y = screenY/1.5-player1.rect.h

player2 = Player2()
player2.rect.x = screenX/1-player2.rect.w
player2.rect.y = screenY/1.5-player2.rect.h
score1, score2 = 0, 0
win1, win2 = False, False

def bounce_phyiscs():
	global score1, score2
	tolerance = 10
	ball.rect.x += ball.velocity.x
	ball.rect.y += ball.velocity.y

	if ball.rect.left <= 0:
		score2 += 1
		ball.velocity.x *= -1
		ball.rect.x = screenX/1.5-50
		ball.rect.y = screenY/1.5-50

	if ball.rect.right >= screenX:
		score1 += 1
		ball.velocity.x *= -1
		ball.rect.x = screenX/1.5-50
		ball.rect.y = screenY/1.5-50

	elif ball.rect.bottom >= screenY or ball.rect.top <= 0:
		ball.velocity.y *= -1

	elif ball.rect.colliderect(player1):
		if abs(player1.rect.top - ball.rect.bottom) < tolerance and ball.velocity.y > 0:
			ball.velocity.y *= -1
		elif abs(player1.rect.bottom - ball.rect.top) < tolerance and ball.velocity.y < 0:
			ball.velocity.y *= -1
		elif abs(player1.rect.right - ball.rect.left) < tolerance and ball.velocity.x < 0:
			ball.velocity.x *= -1
		elif abs(player1.rect.left - ball.rect.right) < tolerance and ball.velocity.x > 0:
			ball.velocity.x *= -1

	elif ball.rect.colliderect(player2):
		if abs(player2.rect.top - ball.rect.bottom) < tolerance and ball.velocity.y > 0:
			ball.velocity.y *= -1
		elif abs(player2.rect.bottom - ball.rect.top) < tolerance and ball.velocity.y < 0:
			ball.velocity.y *= -1
		elif abs(player2.rect.right - ball.rect.left) < tolerance and ball.velocity.x < 0:
			ball.velocity.x *= -1
		elif abs(player2.rect.left - ball.rect.right) < tolerance and ball.velocity.x > 0:
			ball.velocity.x *= -1

def main(scene=0):
	font_90 = pygame.font.Font("assets/fonts/font.ttf", 90)
	font_small = pygame.font.Font("assets/fonts/font.ttf", 30)

	while scene == 0:  # Title
		screen.fill((0, 0, 0))
		startText = font_small.render("BULIEME", False, (255, 255, 255))
		screen.blit(startText, (screenX/2 - startText.get_width()/2, screenY/2 - startText.get_height()/2))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.time.wait(utils.sec2mil(2))
		scene = 1

	while scene == 1:  # Menu
		play_size = (150, 50)
		play_pos = (screenX/2 - play_size[0]/2, screenY/2 - play_size[1]/2 + 150)
		play = pygame.Rect(play_pos, play_size)
		play_text = font_small.render("PLAY", False, (0, 0, 0))
		title = font_90.render("Pong!", False, white)

		screen.fill((0, 0, 0))
		mposx, mposy = pygame.mouse.get_pos()
		play_hover = play.collidepoint((mposx, mposy))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and play_hover:
				scene = 2

		screen.blit(title, (screenX/2 - title.get_width()/2, screenY/2 - title.get_height()/2 + math.sin(time.time()*5)*1 - 150))
		pygame.draw.rect(screen, white, play)
		screen.blit(play_text, (play_pos[0]+play_size[0]/5, play_pos[1]+play_size[1]/5))
		pygame.display.update()

	while scene == 2:
		screen.fill((0, 0, 0))
		global score1, score2
		player1.rect.x += player1.velocity.x
		player1.rect.y += player1.velocity.y

		player2.rect.x += player2.velocity.x
		player2.rect.y += player2.velocity.y

		if player1.rect.top <= 0:
			player1.velocity.y = 0
		elif player1.rect.bottom >= screenY:
			player1.velocity.y = 0

		if player2.rect.top <= 0:
			player2.velocity.y = 0
		elif player2.rect.bottom >= screenY:
			player2.velocity.y = 0
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_w:
					player1.velocity.y = -5
				elif event.key == pygame.K_s:
					player1.velocity.y = 5

				if event.key == pygame.K_UP:
					player2.velocity.y = -5
				elif event.key == pygame.K_DOWN:
					player2.velocity.y = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					player1.velocity.y = 0
				elif event.key == pygame.K_s:
					player1.velocity.y = 0

				if event.key == pygame.K_UP:
					player2.velocity.y = 0
				elif event.key == pygame.K_DOWN:
					player2.velocity.y = 0

		if score1 > score_limit:
			win1, win2 = True, False
			scene = 3
		elif score2 > score_limit:
			win1, win2 = False, True
			scene = 3

		pygame.draw.rect(screen, white, player2)
		pygame.draw.rect(screen, white, player1)
		bounce_phyiscs()
		pygame.draw.rect(screen, white, ball.rect)
		scoreb = font_small.render(str(min(score1, score_limit))+" : "+str(min(score2, score_limit)), False, white)
		screen.blit(scoreb, (screenX/2-scoreb.get_width()/2, 0))
		pygame.display.update()
		clock.tick(60)

	while scene == 3:
		screen.fill((0, 0, 0))
		#win1, win2 = True, False
		#score1, score2 = 0, 0
		MENU_size = (150, 50)
		MENU_pos = (screenX/2 - MENU_size[0]/2, screenY/2 - MENU_size[1]/2 + 100)
		MENU = pygame.Rect(MENU_pos, MENU_size)
		MENU_text = font_small.render("MENU", False, (0, 0, 0))

		MENU_hover = MENU.collidepoint(pygame.mouse.get_pos())

		playagain_size = (290, 50)
		playagain_pos = (screenX/2 - playagain_size[0]/2, screenY/2 - playagain_size[1]/2 + 190)
		playagain = pygame.Rect(playagain_pos, playagain_size)
		playagain_text = font_small.render("PLAY AGAIN", False, (0, 0, 0))

		playagain_hover = playagain.collidepoint(pygame.mouse.get_pos())

		scoreb = font_small.render(str(min(score1, score_limit))+" : "+str(min(score2, score_limit)), False, white)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN and MENU_hover:
				score1, score2 = 0, 0
				main(1)
			elif event.type == pygame.MOUSEBUTTONDOWN and playagain_hover:
				score1, score2 = 0, 0
				main(2)
		
		if win1:
			winner = font_small.render("Player1 win!", False, white)
		elif win2:
			winner = font_small.render("Player2 win!", False, white)

		screen.blit(winner, (screenX/2 - winner.get_width()/2, screenY/2 - winner.get_height()/2-100))
		screen.blit(scoreb, (screenX/2 - scoreb.get_width()/2, screenY/2 - scoreb.get_height()/2-50))
		pygame.draw.rect(screen, white, MENU)
		screen.blit(MENU_text, (MENU_pos[0]+MENU_size[0]/5, MENU_pos[1]+MENU_size[0]/13))
		pygame.draw.rect(screen, white, playagain)
		screen.blit(playagain_text, (playagain_pos[0]+playagain_size[0]/9, playagain_pos[1]+playagain_size[0]/23))
		pygame.display.update()
if __name__ == '__main__':
	main()
