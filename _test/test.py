"""
Simple test module to give "runtests.py" a target.
"""

import unittest




class Basic(unittest.TestCase):

  def test_nocode(self):
    self.assertTrue(True)
