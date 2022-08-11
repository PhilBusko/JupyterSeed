
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
NOTEBOOKS CONFIG
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import os, sys
from enum import Enum

import pandas as PD

LOGIC_PATH = os.path.join(__file__)
sys.path.append(LOGIC_PATH)
MODULE_PATH = os.path.dirname(LOGIC_PATH)
DATA_PATH = os.path.join(MODULE_PATH, 'data')

class RunType(Enum):
    Baseline = 0
    Cleansed = 1

#RUN_TYPE = RunType.Baseline
RUN_TYPE = RunType.Cleansed
