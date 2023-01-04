import pandas as pd

df = pd.read_csv('mohammedia.csv')
# Drop null values
df = df.dropna(axis=1)
# Extract the features and target variable
data = df[['dt','temp', 'humidity', 'pressure', 'wind_speed','weather_id', 'clouds_all']]
# convert dt unix epoch to day, month , yearn hour then save all columns in a new csv file new.csv
data['dt'] = pd.to_datetime(data['dt'],unit='s')
data['day'] = data['dt'].dt.day
data['month'] = data['dt'].dt.month
data['year'] = data['dt'].dt.year
data['hour'] = data['dt'].dt.hour
data.to_csv('new.csv', index=False)

