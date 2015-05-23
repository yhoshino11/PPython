#!/bin/env python

"""
This is This is mymodule.py's documentation string.
This module is a sample of how to create normal module.
"""

SPAM = "spam"


def ham(arg):
    print(arg)


class Egg:
    pass


if __name__ == '__main__':
    ham(Egg())
