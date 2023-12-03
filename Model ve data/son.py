#learning_rate=100 , n_estimators=100 , max_depht=5,subsample=0.9,colsample_bytree=0.9 ,gamma=0.9 

import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,mean_squared_error,confusion_matrix
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
import pickle


#load dataset
#2.1. Veri Yukleme
df = pd.read_csv('Churn_Modelling.csv')
df['Geography'] = df['Geography'].apply(lambda x: {'France': 1, 'Germany': 2, 'Spain': 3}[x])
df['Gender'] = df['Gender'].apply(lambda x: {'Female': 1, 'Male': 2}[x])


X = df.drop(columns=['Exited','Surname','RowNumber','CustomerId'])
Y = df['Exited']



print(X)

x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size=0.33, random_state=42)
scaler=StandardScaler()
xg = XGBClassifier()
xg.fit(x_train, y_train)

y_pred = xg.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)



# Eğitilmiş modeli kaydetme
with open('xgboost.pkl', 'wb') as file:
    pickle.dump(xg, file)

# Eğitilmiş modeli dosyadan yükleme
with open('xgboost.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
