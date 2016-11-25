#!/usr/bin/env python
"""bsorgt.py
"""

__version__ = "1.0b"
__date__ = "2016-10-29"

import sys


def main():
    """main function
    """

    if " !!!" in sys.argv[1]:
        print("Result: p=0.9 --> WUT")

if __name__ == '__main__':
    main()
