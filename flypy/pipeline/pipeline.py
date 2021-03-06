# -*- coding: utf-8 -*-

"""
Pipeline that determines phase ordering and execution.
"""

from __future__ import print_function, division, absolute_import

import dis
import types
import pykit.ir

#===------------------------------------------------------------------===
# Pipeline
#===------------------------------------------------------------------===

def run_pipeline(func, env, passes):
    """
    Run a sequence of transforms (given as functions or modules) on the
    AIR function.
    """
    env['flypy.state.crnt_func'] = func
    for transform in passes:
        func, env = apply_transform(transform, func, env)
        env['flypy.state.crnt_func'] = func
    return func, env


def apply_transform(transform, func, env):
    if isinstance(transform, types.ModuleType):
        result = transform.run(func, env)
    else:
        result = transform(func, env)

    result = _check_transform_result(transform, func, env, result)
    return result or (func, env)


def _check_transform_result(transform, func, env, result):
    if result is not None and not isinstance(result, tuple):
        if isinstance(result, pykit.ir.Function):
            return result, env

        if isinstance(transform, types.ModuleType):
            transform = transform.run
        transform = transform.__module__ + '.' + transform.__name__
        raise ValueError(
            "Expected (func, env) result in %r, got %s" % (transform, result))

    return result