import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randint(0,5,size=(150, 4)), columns=list('ABCD'))
#print(df.head(5))
df['qty'] = df.apply(lambda row: (row.A + row.B + row.C) - row.D, axis = 1)
print(df.head(5))
print(df.shape)
#
df.loc[df['qty']<0,'qty'] = 0
Y = df['qty']
X = df.drop('qty', axis=1)
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=4)

# KNN Classifier
k_range = range(1,20)
scores = {}
scores_list = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    scores[k] = metrics.accuracy_score(y_test, y_pred)
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

#vPlot data Accuracy
plt.plot(k_range, scores_list)
plt.xlabel("Value of K for KNN")
plt.ylabel("Testing Accuracy")


