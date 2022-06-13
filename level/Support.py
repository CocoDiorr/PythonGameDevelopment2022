import pygame.image
from config.Config import *
from csv import reader
from os import walk


def import_csv_layout(path):
    """
    Import terrain objects from the csv file.

    :param path: str: path to map's layer csv file

    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    """
    Import images from the folder.

    :param path: str: path to the folder with image.

    """
    surf_list = {}
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            surf_list[image] = pygame.image.load(full_path).convert_alpha()
    return surf_list
