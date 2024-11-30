import pygame
import sys
def check_events(rocket):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                if event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = False