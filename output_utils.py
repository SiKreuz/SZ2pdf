import sys


def e_print(*args, **kwargs):
    print('ERROR:', *args, file=sys.stderr, **kwargs)
