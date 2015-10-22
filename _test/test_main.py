"""
Test module for `main`.
"""

import unittest
from unittest import TestCase
from pymongo import MongoClient




class Test_App(TestCase):

    def setUp(self):
        from main import App
        self.cls = App

    def test_default(self):
        app = self.cls()
        self.assertIsInstance(app, self.cls)
        self.assertIsInstance(app.db, MongoClient)
        self.assertIsInstance(app.cfg, dict)
        
    def test_customCfg(self):
        cfg = {'testing': (1, 2, 3)}
        app = self.cls(cfg)
        self.assertIs(app.cfg, cfg)
