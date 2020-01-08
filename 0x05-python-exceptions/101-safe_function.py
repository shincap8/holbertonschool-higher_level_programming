#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(args[0], args[1]))
    except (TypeError, ZeroDivisionError, IndexError) as err:
        print ("Exception: {}".format(err), file=sys.stderr)
        return None
