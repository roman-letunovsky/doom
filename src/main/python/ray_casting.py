import pygame
from settings import *
from map import world_map
from pygame import Surface
from pygame import Rect


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(sc, player_pos, player_angle, texture: Surface):
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
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                # texture = world_map[tile_v]
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        xh = 0
        depth_h = 0
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                # texture = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c, c // 2, c // 3)
        pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

        # wall_column = texture.subsurface(Rect(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT))
        # wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        # sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT * proj_height // 2))

        cur_angle += DELTA_ANGLE
