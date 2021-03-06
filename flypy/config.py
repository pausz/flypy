# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

class Config(object):
    # Add color to printed source code
    colour = True

    # Terminal background colour ("light" or "dark")
    terminal_background = "dark"

    # Whether to enable debug compilation. This does not inline methods
    # annotated with `cjit`
    debug = False

config = Config()