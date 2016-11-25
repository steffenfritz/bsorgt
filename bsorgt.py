#!/usr/bin/env python
"""bsorgt.py
"""

__version__ = "1.0b"
__date__ = "2016-10-29"

import sys


def main():
    """main function
    """
    test_string = sys.argv[1]

    if " !!!" in test_string:
        print("Result: p=0.9 --> WUT")

if __name__ == '__main__':
    main()
