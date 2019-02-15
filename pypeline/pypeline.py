# -*- coding: utf-8 -*-

"""Pypeline implements railway oriented programming methods to 
   build a pipeline of functions with error handling"""

import functools

class Either:
    """
    Implementation of Either monad, from Haskell.
    """
    def __init__(self, value):
        self.value = value

    def is_failure(self):
        raise NotImplementedError()
    
    def is_success(self):
        return not self.is_failure()


class Success(Either):
    """Success: equivalent to Right either variant"""
    def __init__(self, value): 
        self.value = value

    def is_failure(self):
        return False

class Failure(Either):
    """Failure: equivalent to Left either variant"""
    def __init__(self, error_name, method, error_msg=""):
        super(Failure, self).__init__(None)
        self.error_name = error_name
        self.error_msg = error_msg
        self.method = method

    def is_failure(self):
        return True

    @staticmethod
    def from_failure(args, method, exception):
        error_name = type(exception).__name__
        error_msg = exception.args[0] if exception.args else str(exception)
        return Failure(error_name, method.__name__, error_msg)

def either_data(args):
    assert args
    
    for idx, arg in enumerate(args):
        if isinstance(arg, Either):
            return idx, arg

    raise ValueError("Input must be of type Either")

def stage(method):
    """ Use this decorator for every stage executing a procedure of a pipeline """

    @functools.wraps(method)
    def wrapper(*args, **kwds):
        try:
            idx, data = either_data(args)

            # bypass in case of failure input
            if data.is_failure():
                return data

            args = list(args[0:idx]) + [data.value] + list(args[idx+1:])

            return Success(method(*args, **kwds))

        except Exception as exception:
            # We want to capture exceptions silently in pipeline stages
            return Failure.from_failure(args, method, exception)

    return wrapper

def compose_pipeline(*procedures):
    """
    Builds the pipeline of procedures or stages    
    """

    def compose(either):
        return functools.reduce(
            lambda either, op: op(either), procedures, either)

    return compose

    