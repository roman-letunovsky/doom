from settings import *

text_map = [
    'WWWWWWWWWWWWWWWW',
    'W......W...WWWWW',
    'W...WW...WWW..WW',
    'WWW.....WW.WWWWW',
    'W..W....W..WWWWW',
    'W..W...WWW.W...W',
    'W....W.....W...W',
    'WWWWWWWWWWWWWWWW'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
