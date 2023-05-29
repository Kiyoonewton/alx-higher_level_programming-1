#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        uks = fct(*args)
    except BaseException as e:
        uks = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return uks
