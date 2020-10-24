import pygame
from settings import *
from map import world_map
from pygame import Surface
from pygame import Rect
from typing import Dict


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_pos, player_angle, textures: Dict[str, Surface]):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        yv = 0
        depth_v = 0
        texture_v = '1'
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        xh = 0
        depth_h = 0
        texture_h = '1'
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        # c = 255 / (1 + depth * depth * 0.00002)
        # color = (c, c // 2, c // 3)
        # pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

        wall_column = textures[texture].subsurface(
            Rect(offset * TEXTURE_SCALE[texture], 0,
                 TEXTURE_SCALE[texture], TEXTURE_HEIGHT[texture]))
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))

        cur_angle += DELTA_ANGLE
