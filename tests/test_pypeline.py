#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypeline` package."""

import pytest


from pypeline.pypeline import stage, Success

@stage
def divide_by_2(number):
    return number / 2

@stage
def multiply_by_2(number):
    return number * 2

def test_given_two_procedures_can_build_pipeline():
    procedures = [divide_by_2, multiply_by_2]

    def pipeline():
        def build(number):
            for proc in procedures:
                number = proc(number)
            return number
        
        return build

    number = 4
    number = pipeline()(Success(number))

    assert number.value == 4