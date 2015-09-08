"""
Common program initialization code.
"""

from pathlib import Path
import os
import sys




ROOTDIR = Path(os.path.dirname(__file__))  #: "pathlib.Path" object to the root directory.



def init():
  """
  Initializes the project's execution environment.
  """
  #Make sure root directory is in the system path.
  for s in (ROOTDIR, ROOTDIR / "lib" / "pydefcello"):
    s = str(s)
    if s not in sys.path:
      sys.path.append(s)
