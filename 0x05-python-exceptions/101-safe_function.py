#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        i = fct(*args)
    except Exception as err:
        i = None
        sys.stderr.write("Exception: {}\n".format(err))
    finally:
        return i
