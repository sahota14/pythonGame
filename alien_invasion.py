import sys
import pygame
form settings imports Settings


def run_game():
    # initialize pygame module and create a screen
    pygame.init()
    ai_settings + Settings()
    screen = pygame.display.set_mode((ai_Settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("python game")

    # set background colour
    bg_color = (230,230,230)


    # exit game loop, watch for keyboard actions

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    screen.fill(ai_settings.bg_color)

    pygame.display.flip()


run_game()