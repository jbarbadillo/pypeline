# -*- coding: utf-8 -*-

"""Pypeline implements railway oriented programming methods to 
   build a pipeline of functions with error handling"""

class Either:
    """
    Implementation of Either monad, from Haskell.
    """
    def __init__(self, response):
        self.response = response


class Success(Either):
    """Success either path"""
    def is_failure(self):
        return False
    
    def is_success(self):
        return True

class Failure(Either):
    """Failure either path"""

    def is_failure(self):
        return True
    
    def is_success(self):
        return False

    def from_failure():
        pass