#!/usr/bin/env python
# encoding: utf-8

"""
Wordpress scanner with simple plugins for various tasks.

Plugins are simple .py files in /scanner/plugins/
"""

__author__ = "Chris Hager"
__version__ = "0.1"
__email__ = "chris@metachris.org"

import sys
import os
import os.path
import imp


class Scanner(object):
    """Plugin based wordpress scanner module"""
    def __init__(self, location, verbose):
        self.location = location
        self.verbose = verbose
        self.load_plugins()

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

    def load_plugins(self):
        self.logv("Loading plugins")
        pluginpath = os.path.join(imp.find_module("scanner")[1], "plugins/")
        pluginfiles = [fname[:-3] for fname in os.listdir(pluginpath) if \
                fname.endswith(".py")]
        if not pluginpath in sys.path:
            sys.path.append(pluginpath)

        # Import
        self.plugins = [__import__(fname) for fname in pluginfiles]

        # Register imnported modules
        for plugin in self.plugins:
            try:
                plugin.register()
            except:
                print "Could not register plugin %s" % mod
                raise
