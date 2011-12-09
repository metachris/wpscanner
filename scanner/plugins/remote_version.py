"""Plugin to find the used wordpress version of a remote installation"""

from prototype import Prototype

HASH_MD5 = 0
CONTAINS = 1

# Identifiers for wordpress versions can either be specific file hashes, or
# strings that have to be contained in a file.
VERSIONS = {
    "3.2.1": [
        ("/wp-content/themes/twentyeleven/style.css", HASH_MD5,
                "3e63c08553696a1dedb24b22ef6783c3"),
    ],
    "3.2": [
        ("/wp-content/themes/twentyeleven/style.css", HASH_MD5,
                "e29eb31a625e50da2458e6f2aa10a3e2"),
    ],
    "3.1": [
        ("/wp-includes/css/admin-bar.css", HASH_MD5,
                "181250fab3a7e2549a7e7fa21c2e6079"),
    ],
    "3.0": [
        ("/wp-content/themes/twentyten/style.css", HASH_MD5,
                "6211e2ac1463bf99e98f28ab63e47c54"),
    ],
}


class Plugin(Prototype):
    runlevel = 0
    remote = True

    def start(self):
        self.log("Trying to find out the exact wordpress version...")
        versions = VERSIONS.keys()
        versions.sort(reverse=True)
        for v in versions:
            for identifyer in VERSIONS[v]:
                self.logv("- Checking for %s..." % v)
                url, id_type, token = identifyer
                r = self.request(url)
