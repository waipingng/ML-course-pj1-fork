
import numpy as np
import pandas as pd
from pred import preprocess_data
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV


df = pd.read_csv("../cleaned_data/merged_data.csv")


X = df['LocationAbbr', 'GeographicLevel', 'Sex', 'ethnicity']
y = df["Heart Disease Mortality"]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

X_train, X_test, y_train, y_test, preprocessor = preprocess_data(df)


knn_regressor = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", KNeighborsRegressor())
])

knn_search_grid = {
    "regressor__n_neighbors": [3, 5, 7, 9],
    "regressor__weights": ["uniform", "distance"],
    "regressor__p": [1, 2]
}


knn_model = GridSearchCV(
    estimator=knn_regressor,
    param_grid=knn_search_grid,
    scoring="neg_root_mean_squared_error", 
    verbose=3
)

knn_model.fit(X_train, y_train)

y_hat_train = knn_model.predict(X_train)
y_hat_test = knn_model.predict(X_test)

train_mse = mean_squared_error(y_train, y_hat_train)
test_mse = mean_squared_error(y_test, y_hat_test)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)
print("Best parameters found:", knn_model.best_params_)
