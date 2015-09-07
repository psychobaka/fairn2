#! /usr/bin/env python3.4
"""
Run the unit tests by executing this script!
"""

from _execommon import ROOTDIR
from pathlib import Path
import os
import sys
import unittest




def main():
  names = _getTestModuleNames(ROOTDIR)
  loader = unittest.TestLoader()
  loader.loadTestsFromNames(names)
  
def _getTestModuleNames(path):
  """
  Returns a list of "pathlib.Path" objects for all test modules in the given
  directory path.
  :param path: "pathlib.Path" object.
  :return: List of "pathlib.Path" objects.
  """
  ret = []
  for subP in path.iterdir():
    if subP.is_dir():
      if subP.match('*/_test'):
        ret.extend(f for f in subP.iterdir() if f.is_file())
      else:
        ret.extend(_getTestModules(subP))
  return ret
  
def _moduleName(path):
  """
  Returns a string of the dotted path to the given module.
  :param path: "pathlib.Path" object pointing to the module file you want to
    look up.
  :return: String.
  :throws ValueError: If given path is not importable from the current ROOTDIR.
  """
  for syspath in sys.path:
    pathRel = path.relative_to(syspath)
    if pathRel.is_absolute():
      continue
    return ".".join(pathRel)
  else:
    raise ValueError('Given file "{}" is not within the Python\'s "sys.path" scope.')

if __name__ == '__main__':
  main()
