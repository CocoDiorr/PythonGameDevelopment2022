import os
import unittest
from unittest.mock import MagicMock, patch, mock_open
from Zelda.companion.Companion import Companion
import ipsedixit

class TestCompanionTradeButton(unittest.TestCase):
    def setUp(self):
        self.comp1 = MagicMock()
        self.comp2 = MagicMock()
        self.comp2.generator = MagicMock() 
        self.comp2.locale = 'jp'
        self.name = "101"
        ipsedixit.Generator = MagicMock()
        
    def test_01_correct_work(self):
        self.comp2.player.dust = 200
        open_text = 'q q q q q q q'
        with patch('Zelda.companion.Companion.open', mock_open(read_data=open_text)) as m:
            Companion.trade_button(self.comp1, self.comp2, self.name)
        assert ipsedixit.Generator.call_args.args == (open_text,)
        assert self.comp2.player.dust == 200 - int(self.name)

    def test_02_not_enough(self):
        self.comp2.player.dust = 50
        Companion.trade_button(self.comp1, self.comp2, self.name)

    def test_03_equal(self):
        self.comp2.player.dust = int(self.name)
        open_text = 'q q q q q q q'
        with patch('Zelda.companion.Companion.open', mock_open(read_data=open_text)) as m:
            Companion.trade_button(self.comp1, self.comp2, self.name)
        assert self.comp2.player.dust == 0
    
    def test_04_file_not_found(self):
        self.comp2.player.dust = 200
        open_text = 'q q q q q q q'
        with patch('Zelda.companion.Companion.open', mock_open(read_data=open_text)) as m:
            m.side_effect = FileNotFoundError()
            self.assertRaises(FileNotFoundError, Companion.trade_button, self.comp1, self.comp2, self.name)
