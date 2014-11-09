# testing/engines.py
# Copyright (C) 2005-2014 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
"""
.. dialect:: postgresql+psycopg2cffi
    :name: psycopg2cffi
    :dbapi: psycopg2cffi
    :connectstring: \
postgresql+psycopg2cffi://user:password@host:port/dbname\
[?key=value&key=value...]
    :url: http://pypi.python.org/pypi/psycopg2cffi/

`psycopg2cffi` is an adaptation of `psycopg2`, using CFFI for the C
layer. This makes it suitable for use in e.g. PyPy. Documentation
is as per `psycopg2`.

.. seealso::

    :mod:`sqlalchemy.dialects.postgresql.psycopg2`

"""
from .psycopg2 import PGDialect_psycopg2


class PGDialect_psycopg2cffi(PGDialect_psycopg2):
    driver = 'psycopg2cffi'

    @classmethod
    def dbapi(cls):
        return __import__('psycopg2cffi')

    @classmethod
    def _psycopg2_extensions(cls):
        root = __import__('psycopg2cffi', fromlist=['extensions'])
        return root.extensions

    @classmethod
    def _psycopg2_extras(cls):
        root = __import__('psycopg2cffi', fromlist=['extras'])
        return root.extras


dialect = PGDialect_psycopg2cffi
