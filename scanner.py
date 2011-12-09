#!/usr/bin/env python
# encoding: utf-8

"""
Scanner module
"""

__author__ = "Chris Hager"
__version__ = "0.1"
__email__ = "chris@metachris.org"

import os


class Scanner(object):
    def __init__(self, location, verbose):
        self.location = location
        self.verbose = verbose

    def log(self, s):
        """General logging"""
        print s

    def logv(self, s):
        """Verbose logging. Only logs if verbose flag is set"""
        if self.verbose:
            self.log(s)

    def scan(self):
        if os.path.exists(self.location):
            self.scan_local(self.location)
        else:
            self.scan_remote(self.location)

    def scan_local(self, directory):
        """Scans a local wordpress installation"""
        self.log("Scan local directory: %s" % directory)

    def scan_remote(self, url):
        """Scans a remote wordpress installation"""
        self.log("Scan remote location: %s" % url)
