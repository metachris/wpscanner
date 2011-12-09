Wordpress Tools - A collection of tools for checking wordpress installations (remote and local)
to make the setup more secure as well as to discover vulnerabilities.

Checks
======
* Wordpress version (info about deprecation, link to newest, etc)
* Themes and plugins
* admin user (dictionary attack)
* get user from entries and check pwd with dictionary


Out of scope currently
----------------------
* Check other software installed
* Nmap: check for services on other ports
* Social engineering (info collection: domain reg, dns, etc)


wp-check-local checks
---------------------
* /var/www/<wp_install>: permissions (no write, users, etc)
* wp-admin accessible? permissions? renamed?
* unique db, users?


Related
=======
* http://code.google.com/p/wpscan (http://code.google.com/p/wpscan/source/browse/#svn%2Ftrunk%2Fdata)


References
----------
* http://news.ycombinator.com/item?id=3332764