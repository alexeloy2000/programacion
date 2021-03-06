# -*- coding: utf-8 -*-
"""Infidelidad - RLogistica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O9BpYRo7GHrqPqq5-vpIDDp4QaYyQ6Kb

Importamos los módulos y librerías que vamos a necesitar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import seaborn as sns

from patsy import dmatrices
from scipy import stats
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

"""Cargamos los datos en dta"""

dta = sm.datasets.fair.load_pandas().data
dta.head(10)

"""Comprobamos que no falten datos"""

dta.isnull().head(10)

"""la matriz de correlación"""

print(dta.corr())

"""la matriz de correlación de forma gráfica"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
dta.educ.hist()
plt.title('Influencia del Nivel Educativo')
plt.xlabel('Nivel Académico')
plt.ylabel('Frecuencia infidelidad')

"""Creamos una nueva variable binaria "infidelity""""

dta['infidelity'] = (dta.affairs > 0).astype(int)
print(dta.head(10))
dta.shape

"""convertir los datos y comprobacion de indices de las matrices resultado"""

from patsy import dmatrices
y, X = dmatrices('infidelity ~ rate_marriage + age +  yrs_married + children + religious+ educ + C(occupation) + C(occupation_husb) ', dta, return_type = 'dataframe')
print(X.shape)
print(y.shape)
print (X.columns)
print(y.columns)

"""convertir de vector columna en matriz 1D"""

y=np.ravel(y)
print(y)

model = LogisticRegression(fit_intercept = False, C = 1e9)
mdl = model.fit(X, y)
model.coef_

"""Ver la precisin del modelo"""

model.score(X,y)

"""32% tiene aventuras amororosas"""

y.mean()

"""ver qué peso tiene para ver matriz de coeficidntes"""

pd.DataFrame(list(zip(X.columns, np.transpose(model.coef_))))

"""Dividimos el dataset en 75% train y 25% test"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

"""Aplicamos los datos"""

predicted = model2.predict(X_test)
print (predicted)
print("Accuracy:",metrics.accuracy_score(y_test, predicted))
print("Precision:",metrics.precision_score(y_test, predicted))
cnf_matrix = metrics.confusion_matrix(y_test, predicted)
cnf_matrix

"""Creando mapa de calor"""

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

"""Prediccion"""

print(X.iloc[4])
F=X.iloc[4]
F.shape
F.values.reshape(1,-1)
model.predict_proba(F.values.reshape(1, -1))

"""obtenemos la probabilidad de infidelidad que, en este caso es de un 37%"""

F.keys();
F['age']=35; F['children']=3; F['yrs_married']=10; F['religious']=1; F['religious']=1; F['C(occupation_husb)[T.3.0]']=1
print(F.values)

# Aplicamos el modelo a este nuevo conjunto de valores y obtenmos
# la probabilidad de infidelidad que, en este caso es de un 29%

F.values.reshape(1,-1)
model.predict_proba(F.values.reshape(1, -1))