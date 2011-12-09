#!/usr/bin/env python
# encoding: utf-8
"""
WordPress Scanner

Check a local or remote wordpress installation for security vulnerabilities,
best practices, etc and get recommendations.

Created by Chris Hager <chris@metachris.org>, Dez. 2011
Copyright (c) 2011 tapdom.com. All rights reserved.
"""

__author__ = "Chris Hager"
__version__ = "0.1"
__email__ = "chris@metachris.org"

import sys
import os
from optparse import OptionParser

from scanner import Scanner


def main(location, verbose=False):
    scanner = Scanner(location, verbose=verbose)
    scanner.scan()


if __name__ == '__main__':
    usage = """usage: %prog [options] wp_url_or_dir

    Example: '%prog http://www.myblog.com' or '%prog /var/www/myblog'"""
    version = "%prog " + __version__
    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-v", "--verbose", default="false",
            action="store_true", dest="verbose")
    #parser.add_option("-s", "--size", dest="size",
    #        help="Specify grid columns and rows (eg 15x10)", metavar="SIZE")
    #parser.add_option("-o", "--ouput", dest="output", choices=["grid", "csv"],
    #        default="grid", help="Type of output ('grid' or 'csv')",
    #        metavar="FORMAT")

    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.error("Please specify a wordpress location")

    main(args[0], options.verbose)
