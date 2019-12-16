import os
from inspect import getsourcefile


def abspath(path):
    modpath = os.path.abspath(getsourcefile(lambda: 0))
    return os.path.join(os.path.dirname(modpath), path)
