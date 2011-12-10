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
import urlparse
import requests


class Scanner(object):
    """Plugin based wordpress scanner module"""
    remote = None
    verbose = False
    location = None

    # Info is a shared dictionary across all plugins
    info = {
        "vulnerabilities": [],
        "recommendations": [],
    }
    plugins = []
    request_buffer = {}

    def __init__(self, location, verbose):
        """Instantiate class and load plugins"""
        self.verbose = verbose
        self.location = location
        self.remote = not os.path.exists(self.location)
        self.load_plugins()

    def log(self, s):
        """General logging"""
        print s

    def logv(self, s):
        """Verbose logging. Only logs if verbose flag is set"""
        if self.verbose:
            self.log(s)

    def load_plugins(self):
        """Load plugins from the plugins/ subdirectory"""
        self.logv("Loading plugins")
        pluginpath = os.path.join(imp.find_module("scanner")[1], "plugins/")
        pluginfiles = [fname[:-3] for fname in os.listdir(pluginpath) if \
                fname.endswith(".py")]
        if not pluginpath in sys.path:
            sys.path.append(pluginpath)

        # Import & Register
        modules = [__import__(fname) for fname in pluginfiles if not \
                fname == "prototype"]
        for mod in modules:
            if mod.Plugin.remote == self.remote:
                try:
                    self.plugins.append(mod.Plugin(self))
                except:
                    print "Could not register plugin %s" % mod
                    raise

        self.logv(self.plugins)

    def start(self):
        """Initiate the scans (the plugins, one after another)"""
        self.log("Starting %s scan of %s" % ("remote" if self.remote else \
                "local", self.location))
        for plugin in self.plugins:
            plugin.start()
        self.logv(self.info)

    def request(self, url, method="GET", data=None, headers=None):
        """HTTP requests with cache"""
        key = str((url, method, data, headers))
        if key in self.request_buffer:
            return self.request_buffer[key]

        url = urlparse.urljoin(self.location, url)
        self.logv("- Requesting %s" % url)
        if method == "GET":
            r = requests.get(url)
        elif method == "POST":
            r = requests.get(url)
        self.request_buffer[key] = r
        return r
