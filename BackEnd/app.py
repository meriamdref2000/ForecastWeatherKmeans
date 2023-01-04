from typing import Union

import pandas as pd
from fastapi import FastAPI
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from fastapi.middleware.cors import CORSMiddleware

data_frame = pd.read_csv('new.csv')
shape = data_frame.shape
print('\nDataFrame Shape :', shape)
all_inputs = data_frame[['hour', 'day', 'month', 'year']]
all_outputs = data_frame['clouds_all']


# Split the dataset into a training set (70%) and a test set (30%)
X_train_of_all, X_test_of_all, y_train_of_all, y_test_of_all = \
    train_test_split(all_inputs, all_outputs, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_all = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_all.fit(X_train_of_all, y_train_of_all)
# Predict the precipitation using the model on the test data
predictions_of_all = liners_regression_model_of_all.predict(X_test_of_all)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_all = 100 - mean_absolute_error(y_test_of_all, predictions_of_all)
print('Accuracy Of clouds_all Prediction Without Clustering :', round(accuracy_of_all, 2), '%.')


temperature_outputs = data_frame['temp']

# Split the dataset into a training set (70%) and a test set (30%)
X_train_of_temp, X_test_of_temp, y_train_of_temp, y_test_of_temp = \
    train_test_split(all_inputs, temperature_outputs, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_temp = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_temp.fit(X_train_of_temp, y_train_of_temp)
# Predict the precipitation using the model on the test data
predictions_of_temp = liners_regression_model_of_temp.predict(X_test_of_temp)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_temp = 100 - mean_absolute_error(y_test_of_temp, predictions_of_temp)
print('Accuracy Of Temperature Prediction:', round(accuracy_of_temp, 2), '%.')


humidity_outputs = data_frame['humidity']

# Split the dataset into a training set (70%) and a test set (30%)
X_train_of_humidity, X_test_of_humidity, y_train_of_humidity, y_test_of_humidity = \
    train_test_split(all_inputs, humidity_outputs, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_humidity = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_humidity.fit(X_train_of_humidity, y_train_of_humidity)
# Predict the precipitation using the model on the test data
predictions_of_humidity = liners_regression_model_of_humidity.predict(X_test_of_humidity)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_humidity = 100 - mean_absolute_error(y_test_of_humidity, predictions_of_humidity)
print('Accuracy Of Humidity Prediction:', round(accuracy_of_humidity, 2), '%.')


wind_outputs = data_frame['wind_speed']

# Split the dataset into a training set (80%) and a test set (20%)
X_train_of_wind, X_test_of_wind, y_train_of_wind, y_test_of_wind = \
    train_test_split(all_inputs, wind_outputs, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_wind = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_wind.fit(X_train_of_wind, y_train_of_wind)
# Predict the precipitation using the model on the test data
predictions_of_wind = liners_regression_model_of_wind.predict(X_test_of_wind)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_wind = 100 - mean_absolute_error(y_test_of_wind, predictions_of_wind)
print('Accuracy Of wind Prediction:', round(accuracy_of_wind, 2), '%.')



kmeans_model = KMeans(n_clusters=3).fit(all_inputs)
data_frame['cluster'] = kmeans_model.labels_

cluster1_data_frame = data_frame[data_frame['cluster'] == 0]
cluster2_data_frame = data_frame[data_frame['cluster'] == 1]
cluster3_data_frame = data_frame[data_frame['cluster'] == 2]

inputs_of_cluster1 = cluster1_data_frame[['hour', 'day', 'month', 'year']]
output_of_cluster2 = cluster1_data_frame['clouds_all']
# Split the dataset into a training set (70%) and a test set (30%)
X_train_of_cluster1, X_test_of_cluster1, y_train_of_cluster1, y_test_of_cluster1 = \
    train_test_split(inputs_of_cluster1, output_of_cluster2, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_cluster1 = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_cluster1.fit(X_train_of_cluster1, y_train_of_cluster1)
# Predict the precipitation using the model on the test data
predictions_of_cluster1 = liners_regression_model_of_cluster1.predict(X_test_of_cluster1)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_cluster1 = 100 - mean_absolute_error(y_test_of_cluster1, predictions_of_cluster1)
print('Accuracy Of Cluster 1:', round(accuracy_of_cluster1, 2), '%.')

inputs_of_cluster2 = cluster2_data_frame[['hour', 'day', 'month', 'year']]
output_of_cluster2 = cluster2_data_frame['clouds_all']
# Split the dataset into a training set (80%) and a test set (20%)
X_train_of_cluster2, X_test_of_cluster2, y_train_of_cluster2, y_test_of_cluster2 = \
    train_test_split(inputs_of_cluster2, output_of_cluster2, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_cluster2 = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_cluster2.fit(X_train_of_cluster2, y_train_of_cluster2)
# Predict the precipitation using the model on the test data
predictions_of_cluster2 = liners_regression_model_of_cluster2.predict(X_test_of_cluster2)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_cluster2 = 100 - mean_absolute_error(y_test_of_cluster2, predictions_of_cluster2)
print('Accuracy Of Cluster 2:', round(accuracy_of_cluster2, 2), '%.')

inputs_of_cluster3 = cluster3_data_frame[['hour', 'day', 'month', 'year']]
output_of_cluster3 = cluster3_data_frame['clouds_all']
# Split the dataset into a training set (80%) and a test set (20%)
X_train_of_cluster3, X_test_of_cluster3, y_train_of_cluster3, y_test_of_cluster3 = \
    train_test_split(inputs_of_cluster3, output_of_cluster3, test_size=0.3)
# Create a linear regression model
liners_regression_model_of_cluster3 = LinearRegression()
# Fit the model to the training data
liners_regression_model_of_cluster3.fit(X_train_of_cluster3, y_train_of_cluster3)
# Predict the precipitation using the model on the test data
predictions_of_cluster3 = liners_regression_model_of_cluster3.predict(X_test_of_cluster3)
# Calculate the model's accuracy in % using the mean absolute error
accuracy_of_cluster3 = 100 - mean_absolute_error(y_test_of_cluster3, predictions_of_cluster3)
print('Accuracy Of Cluster 3:', round(accuracy_of_cluster3, 2), '%.')

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/predict/weather/{hour}/{day}/{month}/{year}")
def predict_weather(hour: int, day: int, month: int, year: int, q: Union[str, None] = None):
    # predict the cluster then use its corresponding linear regression model to predict the all _clouds value
    cluster = kmeans_model.predict([[hour, day, month, year]])[0]
    if cluster == 0:
        prediction = liners_regression_model_of_cluster1.predict([[hour, day, month, year]])[0]
    elif cluster == 1:
        prediction = liners_regression_model_of_cluster2.predict([[hour, day, month, year]])[0]
    else:
        prediction = liners_regression_model_of_cluster3.predict([[hour, day, month, year]])[0]

    if 101 > prediction > 90:
        status = 'Rainy'
    elif 90 > prediction > 15:
        status = 'Cloudy'
    else:
        status = 'Sunny'
    return {"prediction": float(prediction), "weather": status}


@app.get("/predict/humidity/{hour}/{day}/{month}/{year}")
def predict_humidity(hour: int, day: int, month: int, year: int, q: Union[str, None] = None):
    prediction = liners_regression_model_of_humidity.predict([[hour, day, month, year]])
    return {"value": float(prediction)}


@app.get("/predict/temperature/{hour}/{day}/{month}/{year}")
def predict_temperature(hour: int, day: int, month: int, year: int, q: Union[str, None] = None):
    prediction = liners_regression_model_of_temp.predict([[hour, day, month, year]])
    return {"value": float(prediction)}


@app.get("/predict/wind/{hour}/{day}/{month}/{year}")
def predict_wind(hour: int, day: int, month: int, year: int, q: Union[str, None] = None):
    prediction = liners_regression_model_of_wind.predict([[hour, day, month, year]])
    return {"value": float(prediction)}
