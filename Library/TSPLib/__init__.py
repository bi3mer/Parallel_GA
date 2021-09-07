# -*- coding: utf-8 -*-

"""Top-level package for TSPLIB 95."""

__author__ = """Robert Grant"""
__email__ = 'rhgrant10@gmail.com'
__version__ = '0.7.1'


from . import loaders  # noqa: F401


# new style
parse = loaders.parse
load = loaders.load
read = loaders.read


