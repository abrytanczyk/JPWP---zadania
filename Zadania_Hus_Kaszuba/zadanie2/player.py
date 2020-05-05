import pygame
from random import randint
import time
from math import sqrt

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

class Player:
    def __init__(self, x, y, radius, color, id):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.score = 0
        self.velocity = 15 * sqrt(1 / self.radius)
        self.id = id
        self.is_active = True
        self.circle = ((self.x, self.y), self.radius)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(round(self.x, 0)), int(round(self.y, 0))), int(round(self.radius, 0)))

    def move(self, resolution):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x < resolution[0] - self.radius:
            if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.x += 0.707 * self.velocity
            else:
                self.x += self.velocity

        if keys[pygame.K_LEFT] and self.x > self.radius:
            if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                self.x -= 0.707 * self.velocity
            else:
                self.x -= self.velocity

        if keys[pygame.K_UP] and self.y > self.radius:
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.y -= 0.707 * self.velocity
            else:
                self.y -= self.velocity

        if keys[pygame.K_DOWN] and self.y < resolution[1] - self.radius:
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.y += 0.707 * self.velocity
            else:
                self.y += self.velocity

        self.update()

    def grow(self, r, screen_height):  # method for growing after eating bubble / other player
        self.score += r / 2
        if self.radius < screen_height / 2: # plyaer can't be larger than the screen
            self.radius += r / 2
        self.update()

    def respawn(self, resolution):
        self.x = randint(10, resolution[0] - 10)
        self.y = randint(10, resolution[1] - 10)
        time.sleep(0.02)
        self.radius = 5
        self.score = self.radius - 5
        self.update()

    def update(self):
        self.velocity = 20 * sqrt(1 / self.radius)
        self.circle = ((int(round(self.x, 0)), int(round(self.y, 0))), self.radius)
