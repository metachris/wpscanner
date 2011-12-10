"""Plugin to find the used wordpress version of a remote installation"""

import re
import hashlib
from prototype import Prototype

HASH_MD5 = 0
CONTAINS = 1

# Identifiers for wordpress versions can either be specific file hashes, or
# regex patterns that have to be contained in a file. To use regex patterns
# replace the hash with `re.compile("your-pattern")`.
VERSIONS = {
    "3.2.1": [
        ("/wp-content/themes/twentyeleven/style.css",
                "3e63c08553696a1dedb24b22ef6783c3"),
    ],
    "3.2": [
        ("/wp-content/themes/twentyeleven/style.css",
                "e29eb31a625e50da2458e6f2aa10a3e2"),
    ],
    "3.1": [
        ("/wp-includes/css/admin-bar.css",
                "181250fab3a7e2549a7e7fa21c2e6079"),
    ],
    "3.0": [
        ("/wp-content/themes/twentyten/style.css",
                "6211e2ac1463bf99e98f28ab63e47c54"),
    ],
    "2.8.6": [
        ("/wp-content/plugins/akismet/readme.txt",
                "4d5e52da417aa0101054bd41e6243389"),
    ],
    "2.8.5": [
        ("/wp-content/plugins/akismet/readme.txt",
                "58e086dea9d24ed074fe84ba87386c69"),
    ],
    "2.8.2": [
        ("/wp-content/plugins/akismet/readme.txt",
                "48c52025b5f28731e9a0c864c189c2e7"),
    ],
    "2.7.1": [
        ("/wp-includes/js/wp-ajax-response.js",
                "0289d1c13821599764774d55516ab81a"),
    ],
    "2.7": [
        ("/wp-includes/js/thickbox/thickbox.css",
                "9c2bd2be0893adbe02a0f864526734c2"),
    ],
}


class Plugin(Prototype):
    runlevel = 0
    remote = True

    def start(self):
        self.log("Trying to find the exact wordpress version...")
        version = self.find_version()
        self.info["version"] = version
        self.log("- Wordpress version: %s" % version or "unknown")
        if not version:
            return
        elif version != self.versions[0]:
            # If this is an outdated wordpress version, tell user to update
            msg = "- This wordpress is outdated (" + \
                str(self.versions.index(version)) + " releases behind). " \
                "Update to latest Wordpress version: http://bit.ly/asd123"
            self.log(msg)
            self.info["recommendations"].append(msg)
        else:
            self.logv("- Up to date")

    def find_version(self):
        pattern_type = type(re.compile("foo"))
        self.versions = VERSIONS.keys()
        self.versions.sort(reverse=True)
        for v in self.versions:
            self.logv("- Checking for %s..." % v)
            for identifyer in VERSIONS[v]:
                url, token = identifyer
                r = self.request(url)
                if r.status_code in [200, 403]:
                    if isinstance(token, pattern_type):
                        if token.search(r.content):
                            return v
                    else:
                        md5 = hashlib.md5(r.content).hexdigest()
                        if md5 == token:
                            return v
