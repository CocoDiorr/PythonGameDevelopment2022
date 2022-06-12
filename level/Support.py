import pygame.image

from config.Config import *
from csv import reader
from os import walk


def import_csv_layout(path):
    """

    :param path: 

    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surf_list = {}
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            # surf_list.append(image_surf)
            surf_list[image] = pygame.image.load(full_path).convert_alpha()
    return surf_list

# print(import_folder("../map_graphics/Grass"))
# print(import_csv_layout(os.path.join("../", LEVEL_0_ENTITIES)))
