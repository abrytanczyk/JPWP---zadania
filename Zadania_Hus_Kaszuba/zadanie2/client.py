import os
import sys

import pygame as pygame

from network import Network
from player import *

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
resolution = (1280, 720)  # changed from 2 variables to one
window = pygame.display.set_mode(resolution)
pygame.display.set_caption("BUBBLE")

NAME_FONT = pygame.font.SysFont("dejavuserif", 15)
SCOREBOARD_FONT = pygame.font.SysFont("dejavuserif", 25)
# GAME VARIABLES
players = list()
balls = list()


def redrawWindow(window, players, balls):
    window.fill((0, 0, 0))

    for player in players:
        if player.is_active:
            player.draw(window)
            text = NAME_FONT.render(str(player.id), 1, (255, 255, 255))
            window.blit(text, (player.x - text.get_width() / 2, player.y - text.get_height() / 2))

    for ball in balls:
        ball.draw(window)

    rank_players = sorted(players, key=lambda Player: Player.radius, reverse=True)
    scoreboard = SCOREBOARD_FONT.render(str("Scoreboard"), 1, (255, 255, 255))
    start_y = 35
    x = 1270 - scoreboard.get_width()
    window.blit(scoreboard, (x, 5))

    top3 = min(len(players), 3)
    for i in range(top3):
        if rank_players[i].is_active == True:
            text_score = NAME_FONT.render(
                str("ID") + ". " + str(rank_players[i].id) + " Score: " + str(rank_players[i].score), 1,
                (255, 255, 255))
            window.blit(text_score, (x, start_y + i * 20))

    pygame.display.update()


def main():
    global players, balls

    # connect to server and get data
    network = Network()
    (players, balls, my_id) = network.connect()

    clock = pygame.time.Clock()
    run = True
    while run:

        clock.tick(30) # fps = frames per second
        player = players[my_id]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # if user hits a escape key close program
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
        player.move(resolution)

        redrawWindow(window, players, balls)
        pygame.display.update()

        data = player
        (players, balls) = network.send(data)

    network.disconnect()
    pygame.quit()
    quit()


main()
