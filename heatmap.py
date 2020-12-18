from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from IPython.display import display, Markdown
from math import pi
import seaborn as sns

df = pd.read_csv('nbastats2018-2019.csv')

cols_to_include = {'PER': 'Player Efficiency Rating',
                    'OWS': 'Offensive Win Shares',
                    'DWS': 'Defensive Win Shares',
                    'WS' : 'Win Shares',
                    'BPM': 'Box Plus Minus',
                    'VORP' : 'Value over Replacement Player'}

# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna('columns') # drop columns with NaN
    df = df[[ col for col in df.columns if df[col].nunique() > 1 and col in cols_to_include]]
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for Advanced Metrics', fontsize=15)
    plt.show()
nRowsRead = 1000 # specify 'None' if want to read whole file
df1 = pd.read_csv('nbastats2018-2019.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'nbastats2018-2019.csv'
nRow, nCol = df1.shape

fig = plotCorrelationMatrix(df1, 8)
