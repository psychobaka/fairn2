#! /usr/bin/env python3.4
"""
Executable for the program.  Initializes data structures as necessary and enters
the command line interface.
"""

import _execommon
_execommon.init()  #Do this before anything else!

from _execommon import ROOTDIR
from pathlib import Path
from pyyaul.base.execommon import showError
import argparse
import sqlite3




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
  
    def _initDb(self):
        global ROOTDIR
        assert self.cfg is not None, '"_initCfg" must be called first.  :('
        assert 'dbfile' in self.cfg, 'Configuration is missing "dbfile" entry!'
        self.db = sqlite3.connect(ROOTDIR, self.cfg['dbfile'])

@showError
def main(sysArgs=None):
    """
    Main method.
    :param sysArgs: Tuple of arguments in the format provided by "sys.argv".  If
        "None", will use "sys.argv".
    """
    parser = argparse.ArgumentParser(
       'Fair n^2',
       description='Handle those pesky finances between housemates quickly and easily with this program!',
    )
  
if __name__ == '__main__':
    main()
