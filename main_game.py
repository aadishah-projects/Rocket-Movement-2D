import pygame
import sys
from rocket import Rocket
import game_functions as gf
def run_game():
    pygame.init
    # for display
    screen = pygame.display.set_mode((1200,800))
    rocket = Rocket(screen)
    pygame.display.set_caption("Rocket Motion")
    bg_color = (230,230,230)
    # Loop
    while True:
        # check exit events:
        gf.check_events(rocket)
        screen.fill(bg_color)
        rocket.blitme()
        pygame.display.flip()
        rocket.update()
run_game()
