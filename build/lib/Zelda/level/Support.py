"""This module is used to import from folders and csv files."""
import pygame.image
from csv import reader
import os
from os import walk


def import_csv_layout(path: str) -> list[list[str]]:
    """
    Import terrain objects from the csv file.

    :param path: str: path to map's layer csv file
    :return terrain_map: list of lists of data, which means if the tile on the layer of the map contains something

    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path: str) -> dict[str, "pygame.image"]:
    """
    Import images from the folder.

    :param path: str: path to the folder with image.
    :return surf_dict: dictionary of pygame.image with the key of filename converted to string

    """
    surf_dict = {}
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            surf_dict[image] = pygame.image.load(full_path).convert_alpha()
    return surf_dict
