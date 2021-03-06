import socket
from _thread import *
from player import Player
from ball import Ball
from game import Game, update_game_state
import pickle
import pygame

w, h = 788, 444
players = [Player(50, 414, 30, (255, 0, 0), 30, w / 2 - 30, pygame.K_a, pygame.K_d, pygame.K_w),
           Player(w - 50, 414, 30, (0, 255, 0), w / 2 + 30, w - 30, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)]
ball = Ball(200, 250, 0, 0, 20)
game = Game()

'''
    Utwórz serwer przypisany do adresu 127.0.0.1 i portu 5555 obsługujący dwóch klientów.
    Po połączeniu z klientem wyślij tablicę obiektów [Player(gracza), Player(przeciwnika), Ball, Game].
    Odbieraj cyklicznie wysyłane przez klientów współrzędne postaci (tablica [x,y]), użyj ich do aktualizacji obiektów Player, Ball, Game oraz
    odeślij do klienta wspołrzędne postaci przeciwnika i aktualne obiekty Ball oraz Game w formie tablicy [x,y,Ball,Game].
    
    Player.x, Player.y przechowują współrzędne graczy.
    
    Aby zaktualizować obiekty Ball i Game wykonujemy funkcje:
        ball.move(players[0], players[1], game, w)
        update_game_state(ball, players[0], players[1], game, w)
    Uwaga! Aktualizacje obiektu Ball należy wykonywać tylko w jednym z wątków.
    
    Wysyłane i odbierane obiekty należy obsługiwać przy pomocy modułu pickle.
'''

server = '127.0.0.1'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((server, port))
s.listen(4)


def threaded_client(conn, playerid):
    opponentid = 0
    if playerid == 0:
        opponentid = 1

    data = [players[playerid], players[opponentid], ball, game]
    conn.send(pickle.dumps(data))

    while True:
        newData = conn.recv(2048)
        newData = pickle.loads(newData)
        players[playerid].x = newData[0]
        players[playerid].y = newData[1]

        sData = pickle.dumps([players[opponentid].x, players[opponentid].y, ball, game])
        conn.send(sData)



def threaded_server():
    ball.move(players[0], players[1], game, w)
    update_game_state(ball, players[0], players[1], game, w)


start_new_thread(threaded_server, ())
playerid = 0
while True:
    conn, addr = s.accept()
    start_new_thread(threaded_client, (conn, playerid))
    playerid += 1

