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
    plugins = []
    results = {}
    remote = True  # whether wp location is remote (web) or local (dir)

    """Plugin based wordpress scanner module"""
    def __init__(self, location, verbose):
        self.verbose = verbose
        self.location = location
        if os.path.exists(self.location):
            self.remote = False

        self.load_plugins()

    def log(self, s):
        """General logging"""
        print s

    def logv(self, s):
        """Verbose logging. Only logs if verbose flag is set"""
        if self.verbose:
            self.log(s)

    def load_plugins(self):
        self.logv("Loading plugins")
        pluginpath = os.path.join(imp.find_module("scanner")[1], "plugins/")
        pluginfiles = [fname[:-3] for fname in os.listdir(pluginpath) if \
                fname.endswith(".py")]
        if not pluginpath in sys.path:
            sys.path.append(pluginpath)

        # Import & Register
        modules = [__import__(fname) for fname in pluginfiles]
        for mod in modules:
            if not mod.Plugin.remote == self.remote:
                # Skip incompatible plugins (local vs remote)
                continue
            try:
                self.plugins.append(mod.Plugin(self))
            except:
                print "Could not register plugin %s" % mod
                raise

        self.logv(self.plugins)

    def scan(self):
        """Initiate the scans (the plugins, one after another)"""
        self.log("Starting %s scan of %s" % ("remote" if self.remote else \
                "local", self.location))
        for plugin in self.plugins:
            plugin.start()
