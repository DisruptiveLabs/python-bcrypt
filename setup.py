#!/usr/bin/env python
"""
py-bcrypt is an implementation the OpenBSD Blowfish password hashing
algorithm, as described in "A Future-Adaptable Password Scheme" by
Niels Provos and David Mazieres.

This system hashes passwords using a version of Bruce Schneier's
Blowfish block cipher with modifications designed to raise the cost
of off-line password cracking. The computation cost of the algorithm
is parametised, so it can be increased as computers get faster.
"""
# Copyright (c) 2006 Damien Miller <djm@mindrot.org>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# $Id$

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = "0.3.2"

if __name__ == '__main__':
    bcrypt = Extension(
        'bcrypt._bcrypt',
        sources=[
            'bcrypt/bcrypt_python.c',
            'bcrypt/blowfish.c',
            'bcrypt/bcrypt.c'
        ]
    )
    setup(
        name="python-bcrypt",
        version=VERSION,
        author="Damien Miller, maintained by @kageurufu",
        author_email="kage.urufu@gmail.com",
        url="https://github.com/DisruptiveLabs/python-bcrypt",
        description="Blowfish password hashing",
        long_description=__doc__,
        license="BSD",
        packages=['bcrypt'],
        ext_modules=[bcrypt],
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
    )
