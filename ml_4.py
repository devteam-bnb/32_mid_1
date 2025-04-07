import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Experience': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Salary': [30,35,38,43,47,50,55,58,62,66,68,70]
})

X = df[['Experience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

print("Train MSE:", mean_squared_error(y_train, y_train_pred))
print("Test MSE:", mean_squared_error(y_test, y_test_pred))
print("R2 Score:", r2_score(y_test, y_test_pred))

plt.scatter(X_train, y_train, color='blue', label='Train Actual')
plt.plot(X_train, y_train_pred, color='red', label='Train Predicted')
plt.title("Train Data - Regression")
plt.legend()
plt.grid(True)
plt.show()

plt.scatter(X_test, y_test, color='green', label='Test Actual')
plt.plot(X_test, y_test_pred, color='orange', label='Test Predicted')
plt.title("Test Data - Regression")
plt.legend()
plt.grid(True)
plt.show()