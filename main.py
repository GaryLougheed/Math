#Header
import sys
import matrix
import stats
import matplotlib.pyplot as plt 
import numpy as np
#import pyqtgraph-0.10.0/pyqtgraph as pg
#Classes

#Functions
def mean(x):
  sum = 0
  for i in range(len(x)):
    sum += i
  sum = sum/i
  return sum

#Main
def main():
  x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
  C,S = np.cos(x),np.sin(x)
  plt.plot(x,C)
  plt.plot(x,S)

  plt.show()
#init 
if __name__ == "__main__":
  main()

