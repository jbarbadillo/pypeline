#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypeline` package."""

import pytest


from pypeline.pypeline import stage, Success

@stage
def divide_by_2(number):
    if number == 0:
        raise ValueError("Value cannot be 0")
    return number / 2

@stage
def multiply_by_2(number):
    return number * 2

def pipeline(procedures):
    def build(number):
        for proc in procedures:
            number = proc(number)
        return number
    
    return build

def test_given_two_procedures_if_successful_can_get_result():
    procedures = [divide_by_2, multiply_by_2]    

    number = 4
    number = pipeline(procedures)(Success(number))

    assert number.value == 4

def test_given_two_procedures_if_first_raises_exception_then_can_get_error():
    procedures = [divide_by_2, multiply_by_2]    

    number = 0
    number = pipeline(procedures)(Success(number))

    assert number.is_failure()
    assert number.error_name == "ValueError"
    assert number.error_msg == "Value cannot be 0"
    assert number.method == "divide_by_2"