import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = pygame.image.load('v462-n-130-textureidea_1.jpg').convert()

    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, p_player_pos, p_player_angle):
        ray_casting(self.sc, p_player_pos, p_player_angle, self.texture)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.circle(self.sc_map , RED, (int(map_x), int(map_y)), 5)
        pygame.draw.line(self.sc_map , YELLOW, (map_x, map_y), (map_x + WIDTH * math.cos(player.angle),
                                                 map_y + WIDTH * math.sin(player.angle)), 2)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map , GREEN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
