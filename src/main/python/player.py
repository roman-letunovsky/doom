from settings import *
import pygame
import math


class Player:
    def __init__(self, p_player_pos: float, p_player_angle: float):
        self.x, self.y = p_player_pos
        self.angle = p_player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a
            # print('W')
        if keys[pygame.K_s]:
            self.x += -PLAYER_SPEED * cos_a
            self.y += -PLAYER_SPEED * sin_a
            # print('S')
        if keys[pygame.K_a]:
            self.x += PLAYER_SPEED * sin_a
            self.y += -PLAYER_SPEED * cos_a
            # print('A')
        if keys[pygame.K_d]:
            self.x += -PLAYER_SPEED * sin_a
            self.y += PLAYER_SPEED * cos_a
            # print('D')
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
