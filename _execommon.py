"""
Common program initialization code.
"""

from pathlib import Path
import os
import sys




ROOTDIR = Path(os.path.dirname(__file__))  #: "pathlib.Path" object to the root directory.

#Make sure root directory is in the system path.
s = str(ROOTDIR)
if s not in sys.path:
  sys.path.append(s)
