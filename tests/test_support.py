import os
import unittest
from unittest.mock import MagicMock, patch, mock_open
from level.Support import import_csv_layout, import_folder
import pygame

import time

class TestImportCSVLayout(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join("a", "b", "c")
        self.csv = "1,2,3\n4,5,6\n"
        self.map = [['1','2','3'],['4','5','6']]

    def test_01_correct_work(self):
        with patch('level.Support.open', mock_open(read_data=self.csv)) as open_mock:
            map = import_csv_layout(self.path)
        assert map == self.map
    
    def test_02_file_not_found(self):
        with patch('level.Support.open', mock_open(read_data=self.csv)) as open_mock:
            open_mock.side_effect = FileNotFoundError
            self.assertRaises(FileNotFoundError, import_csv_layout, self.path)


class MyStr:
    def __init__(self, s):
        self.s = s

    def convert_alpha(self):
        self.s += '_a'
        return self.s


def MyReader(path):
    with open(path) as f:
        return MyStr(f.read())

class TestImportFolder(unittest.TestCase):
    def setUp(self):
        os.mkdir(os.path.join('tests', 'extra'))
        with open(os.path.join('tests', 'extra', 'qwe.png'), 'w') as f:
            f.write('PNG1')
        with open(os.path.join('tests', 'extra', 'asd.png'), 'w') as f:
            f.write('PNG2')
        pygame.image.load = MyReader
        self.path = os.path.join('tests', 'extra')

    def tearDown(self):
        time.sleep(1)
        os.remove(os.path.join('tests', 'extra', 'qwe.png'))
        os.remove(os.path.join('tests', 'extra', 'asd.png'))
        os.rmdir(os.path.join('tests', 'extra'))

    def test_01_correct_work(self):
        surf_list = import_folder(self.path)
        assert surf_list == {'qwe.png': 'PNG1_a', 'asd.png': 'PNG2_a'}
    
    def test_02_wrong_path(self):
        surf_list = import_folder(self.path + 'q')
        assert surf_list == {}

    def test_03_nested_folders(self):
        os.mkdir(os.path.join('tests', 'extra', 'extra2'))
        with open(os.path.join('tests', 'extra', 'extra2', 'zxc.png'), 'w') as f:
            f.write('PNG3')
        self.assertRaises(FileNotFoundError, import_folder, self.path)
        os.remove(os.path.join('tests', 'extra', 'extra2', 'zxc.png'))
        os.rmdir(os.path.join('tests', 'extra', 'extra2'))