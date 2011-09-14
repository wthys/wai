Check whether your hostname is really pointing to your host.

Usage
-----
```
usage: waikiki [-h] [-v] hostname

Checks whether a hostname leads to this host

positional arguments:
  hostname       The hostname to check

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Be verbose
```

Why?
----

- When you want to detect that your IP has changed but your DNS record has not.
- When you want to detect that you are in a certain network.

To do
-----

- Possibly bypass local DNS servers (like a local dnsmasq)
