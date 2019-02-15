# -*- coding: utf-8 -*-

"""Pypeline implements railway oriented programming methods to 
   build a pipeline of functions with error handling"""

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
    def from_failure(args, method, error):
        error_name = type(error).__name__
        error_msg = error.args[0] if error.args else str(error)
        return Failure(error_name, error_msg, method.__name__)
    
