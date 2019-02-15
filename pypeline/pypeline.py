# -*- coding: utf-8 -*-

"""Pypeline implements railway oriented programming methods to 
   build a pipeline of functions with error handling"""

import functools

class Either:
    """
    Implementation of Either monad, from Haskell.
    """
    pass


class Success(Either):
    """Success: equivalent to Right either variant"""
    def __init__(self, value): 
        self.value = value

    def is_failure(self):
        return False
    
    def is_success(self):
        return True

class Failure(Either):
    """Failure: equivalent to Left either variant"""
    def __init__(self, error_name, error_msg, method):
        self.error_name = error_name
        self.error_msg = error_msg
        self.method = method

    def is_failure(self):
        return True
    
    def is_success(self):
        return False

    @staticmethod
    def from_failure(args, procedure, exception):
        error_name = type(exception).__name__
        error_msg = exception.args[0] if exception.args else str(exception)
        return Failure(error_name, error_msg, procedure.__name__)

def either_data(args):
    assert args
    
    for idx, arg in enumerate(args):
        if isinstance(arg, Either):
            return idx, arg

    raise ValueError("Input must be of type Either")

def Stage(procedure):
    """ Use this decorator for every stage executing a procedure of a pipeline """
    @functools.wraps(procedure)
    def wrapper(*args, **kwds):
        try:
            idx, data = either_data(args)

            # bypass in case of failure input
            if data.is_failure():
                return data

            args = list(args[0:idx]) + [data.value] + list(args[idx+1:])

            return Success(procedure(*args, **kwds))

        except Exception as exception:
            # We want to capture exceptions silently in pipeline stages
            return Failure.from_failure(args, procedure, exception)

    return wrapper

def compose_pipeline(*procedures):
    """
    Builds the pipeline of procedures or stages    
    """

    def compose(either):
        return functools.reduce(
            lambda either, op: op(either), procedures, either)

    return compose


    