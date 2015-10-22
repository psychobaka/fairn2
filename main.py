#! /usr/bin/env python3.5
"""
Executable for the program.  Initializes data structures as necessary and enters
the command line interface.
"""

import _execommon
_execommon.init()  #Do this before anything else!

from _execommon import ROOTDIR, initCfg, initDB
from pathlib import Path
from pyyaul.base.execommon import showError
import argparse




class App:
    """Class representing the "Fair'n^2" application."""

    db = None  #: "sqlite3.Connection" object opened to the user's database file.
  
    cfg = None  #: "dict" object with configuration data for this session.
  
    def __init__(self, cfg=None):
        """
        Initializes the operating environment.
        :param cfg: `dict` with configuration information, or `pathlib.Path` to
          user config file.
        """
        self.cfg = initCfg(cfg)
        self.db = initDB(self.cfg)

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
