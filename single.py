import os, sys
from PIL import Image
import json


def enable_matplot():
    if os.environ.get('MATPLOT_DISABLE') is None:
        return True
    else:
        return False


if enable_matplot():
    print("loading matplot")
    import matplotlib.pyplot as plt
    from pylab import *

if __name__ == '__main__':
    print("single")
