#!/usr/bin/env python
# copyright (c) 2008-2013 Eric P. Mangold
# See LICENSE for details

from distutils.core import setup

if __name__ == '__main__':
    setup(name="ampy",
            version="1.2.4",
            description="Ampy - The pure-Python AMP library",
            author="Eric P. Mangold",
            author_email="eric@teratorn.org",
            license="MIT",
            packages=['ampy'],
            scripts=['bin/ampyclient']
            )


