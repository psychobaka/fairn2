#! /usr/bin/env python3.4
"""
Executable for the program.  Initializes data structures as necessary and enters the command line
interface.
"""

import _execommon
_execommon.init()  #Do this before anything else!

from _execommon import ROOTDIR
from defcello.execommon import showError
from pathlib import Path
import argparse
import json
import os
import shutil
import sqlite3
import sys




class App:

  db = None  #: "sqlite3.Connection" object opened to the user's database file.

  cfg = None  #: "dict" object with configuration data for this session.

  def __init__(self, cfg=ROOTDIR / 'user' / 'cfg.json')):
    """
    Initializes the operating environment.
    :param cfg: `pathlib.Path` to user config file.  May also be a "dict" object
      (useful for testing).
    """
    _initCfg(cfg)
    _initDb()

  def _initCfg(self, cfg):
    if not isinstance(cfg, dict):
      global ROOTDIR
      if not os.path.exists(cfg):
        shutil.copyfile(ROOTDIR / 'user' / 'default' / 'cfg.json', cfg)
      with open(cfg) as fd:
        cfg = json.load(fd)
    self.cfg = cfg

  def _initDb(self):
    global ROOTDIR
    assert self.cfg is not None, '"_initCfg" must be called first.  :('
    assert 'dbfile' in self.cfg, 'Configuration is missing "dbfile" entry!'
    self.db = sqlite3.connect(ROOTDIR, self.cfg['dbfile'])

@showError
def main(sysArgs=None):
  """
  Main method.
  :param sysArgs: Tuple of arguments in the format provided by "sys.argv".  If "None", will use
    "sys.argv".
  """
  parser = argparse.ArgumentParser(
    'Fair n^2',
    description='Handle those pesky finances between housemates quickly and easily with this program!',
  )

if __name__ == '__main__':
  main()
