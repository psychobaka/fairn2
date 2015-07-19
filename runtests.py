#! /usr/bin/env python3.4
"""
Run the unit tests by executing this script!
"""

import os
import unittest
from pathlib import Path
from _execommon import ROOTDIR




def main():
  modules = _getTestModules(ROOTDIR)
  
def _getTestModules(path):
  """
  Returns a list of "pathlib.Path" objects for all test PY files in the given path.
  :param path: "pathlib.Path" object.
  :return: List of "pathlib.Path" objects.
  """
  ret = []
  for subP in path.iterdir():
    if subP.is_dir():
      if subP.match("*/_test"):
        ret.extend(f for f in subP.iterdir() if f.is_file())
      else:
        ret.extend(_getTestModules(subP))
  return ret
  
def _moduleName(path):
  """
  Returns a string of the dotted path to the given module.
  :param path: "pathlib.Path" object.
  :return: String.
  :throws ValueError: If given path is not importable from the current ROOTDIR.
  """
  p = path.relative_to(ROOTDIR)
  if 

if __name__ == "__main__":
  