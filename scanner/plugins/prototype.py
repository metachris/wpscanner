"""Plugin prototype"""


class Prototype(object):
    runlevel = 0
    remote = True

    def __init__(self, scanner):
        self.scanner = scanner

    def start(self):
        pass

    def request(self, url, method="GET", data=None, headers=None):
        return self.scanner.request(url, method, data, headers)

    def log(self, s):
        self.scanner.log(s)

    def logv(self, s):
        self.scanner.logv(s)
