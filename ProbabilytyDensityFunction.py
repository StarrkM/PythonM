# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 18:32:25 2016

@author: HKHQ5658
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

x=np.linspace(-4,4,100)

for mean, variance in [(0,0.7),(0,1),(1,1.5),(-2,0.5)]:
    plt.plot(x,mlab.normpdf(x,mean,variance))
plt.show()