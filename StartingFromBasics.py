# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from sklearn.datasets import load_boston
boston=load_boston()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

dataset=pd.DataFrame(boston.data,columns=boston.feature_names)
dataset['target']=boston.target

