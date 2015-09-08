#! /usr/bin/env python3.4
"""
Run the unit tests by executing this script!
"""

import _execommon
_execommon.init()  #Do this before anything else!

from _execommon import ROOTDIR
from defcello.execommon import showError
from defcello.unittest import runTestsIn




@showError
def main():
  runTestsIn(ROOTDIR, ROOTDIR)

if __name__ == '__main__':
  main()
