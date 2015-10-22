#! /usr/bin/env python3.5
"""
Run the unit tests by executing this script!
"""

import _execommon
_execommon.init()  #Do this before anything else!
from _execommon import ROOTDIR
from pyyaul.base.execommon import showError
from pyyaul.base.unittest import runTestsIn




@showError
def main():
  runTestsIn(ROOTDIR)

if __name__ == '__main__':
  main()
