import sys,csv
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ggplot import *

df=pd.read_csv(sys.argv[1])

##1
y=df['C']
x=df['A']
noisy = y + np.random.randn(y.size) 
pf1, pp, ppp, pppp, ppppp = sp.polyfit(x, noisy, 1, full =True)
f1 = sp.poly1d(pf1)
print ggplot(df, aes("x", noisy))+geom_point() + geom_line(aes(x, y = f1(x)), color = "blue")

##\3
x=df['A']
y=df['D']
noisy = y + np.random.randn(y.size) 
pf3, pp, ppp, pppp, ppppp = sp.polyfit(x, noisy, 3, full =True)
f3 = sp.poly1d(pf3)
print ggplot(df, aes("x", noisy))+geom_point() + geom_line(aes(x, y = f3(x)), color = "blue")

#5
x=df['A']
y=df['B']
noisy = y + np.random.randn(y.size)
pf5,pp, ppp, pppp, ppppp= sp.polyfit(x, noisy, 5, full =True)
f5 = sp.poly1d(pf3)
print ggplot(df, aes("x", noisy))+geom_point() + geom_line(aes(x, y = f5(x)), color = "blue")

