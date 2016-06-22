"""
Import helper

Can be used in each chapter

import sys
sys.path.append("../src")
from import_helper import *
%matplotlib inline

===
import json
import matplotlib
s = json.load(open("../styles/bmh_matplotlibrc.json"))
matplotlib.rcParams.update(s)

"""

from IPython.core.pylabtools import figsize
import numpy as np
from matplotlib import pyplot as plt
import seaborn.apionly as sns
import scipy.stats as stats