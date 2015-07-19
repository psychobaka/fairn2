"""
Executable for the program.  Initializes data structures as necessary and enters the command line
interface.
"""

import argparse
import json
import os
import shutil
import sqlite3
import sys




ROOTDIR = __file__  #: String absolute path to the root directory.

class App:

  DB = None  #: "sqlite3.Connection" object opened to the user's database file.

  CFGFILEPATH = os.path.join(ROOTDIR, "user", "cfg.json")  #: String absolute path to the user's configuration JSON file.

  USERCFG = None  #: Object returned from decoding the user's JSON configuration file.  Should be a "dict" object.

  def __init__(cfg, ):
    """
    Initializes the operating environment.
    :param cfg: String path to user config file.  May also be a "dict" object (useful for testing).
    """
    _init_userCfg(cfg)
    _init_db()

def _init_userCfg(cfg):
  if isinstance(cfg, dict):
    global ROOTDIR, USERCFG
    if not os.path.exists(cfg):
      shutil.copyfile(os.path.join(ROOTDIR, "user", "default", "cfg.json"), cfg)
    with open(cfg) as fd:
      USERCFG = json.load(fd)

  assert "dbfile" in USERCFG, "'user/cfg.json' is missing data!"

def _init_db():
  global DB, ROOTDIR, USERCFG
  DB = sqlite3.connect(os.path.join(ROOTDIR, USERCFG["dbfile"]

def main(sysArgs=None):
  """
  Main method.
  :param sysArgs: Tuple of arguments in the format provided by "sys.argv".  If "None", will use
    "sys.argv".
  """
  parser = argparse.ArgumentParser(
    "Fair n^2",
    description="Handle those pesky finances between housemates quickly and easily with this program!",
  )

if __name__ == "__main__":
  main()