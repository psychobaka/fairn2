"""
Simple test module to give "runtests.py" a target.
"""

import unittest
from unittest import TestCase




class TestBasic(TestCase):

  def test_nocode(self):
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
