import math
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression



data = pd.read_csv('infy.csv')
df = data[['Open Price','High Price','Low Price','Close Price']]
# print(df.columns.values)

df['open'] = df['Open Price']
df['high'] = df['High Price']
df['low'] = df['Low Price']
df['close'] = df['Close Price']
# print(df)
df['label'] = df['close'].shift(-3)
X = np.array(df[['open','high','close']])
X_lately = X[-3:]
X = X[:-3]


y = np.array(df['label'])
y = y[:-3]
# print(X.shape, y.shape)
'''
find the y_test and x_test according to test_size.. Test size could be 80%-20%, 70%-30%, 60%-40%. 
Test size should be 20, 30 and 40 perecentage
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


print("X_train, X_test, y_train, y_test",X_train.shape, X_test.shape, y_train.shape, y_test.shape)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print('confidence:', confidence)
forecast_set = clf.predict(X_lately)

print("forecast_set",forecast_set)