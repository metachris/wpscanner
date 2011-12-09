"""Plugin to find the used wordpress version"""


class Plugin(object):
    runlevel = 0
    remote = True

    def __init__(self, scanner):
        self.scanner = scanner

    def start(self):
        print "- Start wp-version"
