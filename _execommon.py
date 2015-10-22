"""
Common program initialization code.
"""

from pathlib import Path
from pymongo import MongoClient
import json
import os
import shutil
import sys




#: `pathlib.Path` object to the root directory.
ROOTDIR = Path(os.path.dirname(__file__))

#: `pathlib.Path` object to the config directory.
DEFAULTCONFIGPATH = ROOTDIR / 'user' / 'default' / 'cfg.json'

#: `pathlib.Path` object to the config directory.
USERCONFIGPATH = ROOTDIR / 'user' / 'cfg.json'

#: `dict` object with user configuration information.
USERCONFIG = None

#: Database controller.  For now, this will always be a `pymongo.MongoClient`
#: object.
DB = None

def init(cfg=True, db=True, **kargs):
    global DEFAULTCONFIGPATH, USERCONFIGPATH
    """
    Initializes the project's execution environment.
    :param cfg: If `True`, will call `initCfg`.
    :param db: If `True`, will call `initDB`.
    :param kargs: Any number of keyword arguments with values to use for this
      module's global constants.
    :return: `None`.
    """
    DEFAULTCONFIGPATH = kargs.get("DEFAULTCONFIGPATH", DEFAULTCONFIGPATH)
    USERCONFIGPATH = kargs.get("USERCONFIGPATH", USERCONFIGPATH)
    for path in (ROOTDIR, ROOTDIR / "lib" / "PyYAUL"):
        path = str(path)
        if path not in sys.path:
            sys.path.append(path)
    if initCfg:
        initCfg()
    if initDB:
        initDB()

def initCfg(userCfg=None, defaultCfg=None):
    """
    Initializes the user configuration file.
    :param userCfg: `pathlib.Path` to user configuration file.  If `None`, will
      use the value of global `USERCONFIGPATH`.  If it does not exist, will
      create one by copying the default configuration file.  May also be a
      `dict` object, which will cause the user's configuration file to be
      ignored.
    :param defaultCfg: `pathlib.Path` to default configuration file.  If `None`,
      will use the value of global `DEFAULTCONFIGPATH`.  If it does not exist,
      will create one by copying the default configuration file.
    :return: `dict` object.
    """
    global USERCONFIG
    if userCfg is None:
        userCfg = USERCONFIGPATH
    if defaultCfg is None:
        defaultCfg = DEFAULTCONFIGPATH
    if not isinstance(userCfg, dict):
        userCfg.parent.mkdir(parents=True, exist_ok=True)
        if not userCfg.exists():
            defaultCfg.parent.mkdir(parents=True, exist_ok=True)
            defaultCfg.touch()
            shutil.copyfile(str(defaultCfg), str(userCfg))
        with userCfg.open() as fd:
            userCfg = json.load(fd)
    if USERCONFIG is None:  #Only set the global once.
        USERCONFIG = userCfg
    return userCfg
    
def initDB(cfg=None):
    """
    Initializes the session's database.  Information should be specified in
    `USERCONFIG` under the keys "db/type" (defaults to `'MongoDB'`) and
    "db/addr" (defaults to `'mongodb://localhost:27017/'`).
    :param cfg: `dict` with user config information.  If `None`, will use
      `USERCONFIG`.
    :return: DB interface object.  For now, this will always be a
      `pymongo.MongoClient` object.
    """
    global DB
    if cfg is None:
        assert USERCONFIG is not None, '`initCfg` must be called first.'
        cfg = USERCONFIG
    dbCfg = cfg.get('db', {})
    dbType = dbCfg.get('type', 'MongoDB')
    assert dbType == 'MongoDB', 'I\'m sorry, only `"MongoDB"` is supported at this time.  ;_;'
    addr = dbCfg.get('addr', 'mongodb://localhost:27017/')
    if dbType == 'MongoDB':
        db = MongoClient(addr)
    else:
        raise ValueError('DB type {!r} is not yet supported.  ;_;'.format(dbType))
    if DB is None:  #Only set the global once.
        DB = db
    return db
