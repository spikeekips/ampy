# Ampy, the pure-Python AMP client and server

Ampy is an AMP library that provides a syncronous, blocking interface
for making AMP calls (client interface).

It also provides an asyncore-based asynchronous API for making
non-blocking servers and clients.

Synchronous Client Example:

from ampy import ampy

class Sum(ampy.Command):
    arguments = [('a', ampy.Integer()), ('b', ampy.Integer())]
    response = [('total', ampy.Integer())]

proxy = ampy.Proxy('localhost', 1234)
proxy.connect()
result = proxy.callRemote(Sum, a=5, b=10)
print "TOTAL:", result['total']


# Notice


This repository was forked from the original ampy BZR repository and added some several bug fixes and features.

## Detect Service Side Connection

See https://bugs.launchpad.net/ampy/+bug/1207618 .


## ListOf Argument

Not like twisted AMP, the ampy does not support the special argument type, `ListOf`. In this repository, support ListOf argument type.
