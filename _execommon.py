"""
Common program initialization code.
"""

from pathlib import Path
import os
import sys




DEFAULTCONFIGPATH = None
ROOTDIR = Path(os.path.dirname(__file__))  #: "pathlib.Path" object to the root directory.

def init(**kargs):
    global DEFAULTCONFIGPATH
    """
    Initializes the project's execution environment.
    :param kargs: Any number of keyword arguments with values to use for this
    module's global constants.
    """
    if DEFAULTCONFIGPATH is None:
        DEFAULTCONFIGPATH = kargs.get(
            "DEFAULTCONFIGPATH",
            ROOTDIR / 'user' / 'default' / 'cfg.json',
        )
    for path in (ROOTDIR, ROOTDIR / "lib" / "PyYAUL"):
        path = str(path)
        if path not in sys.path:
            sys.path.append(path)

def _initCfg(self, cfg):
    """
    Initializes the user configuration file.
    :param cfg: `pathlib.Path` or `str` to user configuration file.  If it does
      not exist, will create one by copying the default configuration file 
    """
    if not isinstance(cfg, dict):
        global ROOTDIR
        if not os.path.exists(cfg):
            shutil.copyfile(DEFAULTCONFIGPATH, cfg)
        with open(cfg) as fd:
            cfg = json.load(fd)
    self.cfg = cfg
