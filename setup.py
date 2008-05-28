#!/usr/bin/env python
# copyright (c) 2008 Eric Mangold, All Rights Reserved
from distutils.core import setup

if __name__ == '__main__':
    setup(name="ampy",
            version="1.2.2",
            description="Ampy - The pure-Python AMP library",
            author="Eric Mangold",
            author_email="teratorn@gmail.com",
            license="MIT",
            packages=['ampy'],
            scripts=['bin/ampyclient']
            )


