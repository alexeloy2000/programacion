# -*- coding: utf-8 -*-
"""EjemploSVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aSuuIaoxQ67lYHxNRO_FUb9zL4xDbUOs
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs


# creamos 50 puntos 25,25 de dos tipos
X, y = make_blobs(n_samples=50, centers=2, random_state=6)

# entrenamos el modelo 
clf = svm.SVC(kernel='linear')
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)

# plot la funcion de desision
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# creamos una cuadrícula para evaluar el modelo
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot límite de decisión y márgenes
ax.contour(XX, YY, Z, colors='g', levels=[-1, 0, 1], alpha=0.8,
           linestyles=['--', '-', '--'])
# plot vectores de sooporte
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=500,
           linewidth=2, facecolors='none', edgecolors='k')
plt.show()