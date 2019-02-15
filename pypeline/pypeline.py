# -*- coding: utf-8 -*-

"""Pypeline implements railway oriented programming methods to 
   build a pipeline of functions with error handling"""

class Either:
    """
    Implementation of Either monad, from Haskell.
    """
    def __init__(self, response):
        self.response = response

    def is_success(self):
        pass
    
    def is_failure(self):
        pass

class Success(Either):
    """Success either path"""
    def is_failure(self):
        return False

class Failure(Either):
    """Failure either path"""

    def is_failure(self):
        return True