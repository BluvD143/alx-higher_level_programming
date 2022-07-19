#!/usr/bin/python3
# 101-safe_function.py

def safe_function(fct, *args):
	"""Executes a function safely.
    try:
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
