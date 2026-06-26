
import pandas as pd
import pymysql
import joblib

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error


# pymySQL Connector-

conn = pymysql.connect(host="localhost",user="root",database="house_db",password="harsh" ) # Replace with your local MySQL password

query = """
select 
    avg_income,
    house_age,
    num_rooms,
    price
from houses;
"""

df = pd.read_sql(query, conn)
conn.close()

print("Original Database: ")
print(df, "\n")


# Feature Scaling-
scaler = StandardScaler()
df[['avg_income', 'house_age', 'num_rooms']] = scaler.fit_transform(df[['avg_income', 'house_age', 'num_rooms']])

print("Scaled Dataset: ")
print(df, "\n")


# Split Data-
x = df[['avg_income', 'house_age', 'num_rooms']]
y = df[['price']]


# Train Test Split-
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=2)

# Model Train-
model = LinearRegression()
model.fit(x_train, y_train)

# Evaluate Model-
y_pred = model.predict(x_test)

print("\nModel Performance")
print("----------------------")
print("R² Score :", round(r2_score(y_test, y_pred), 3))
print("MAE      :", round(mean_absolute_error(y_test, y_pred), 2))


# Prediction Data-
print("\nEnter House Details- ")
income = float(input("Enter Average Income: "))
age = float(input("Enter House Age: "))
rooms = int(input("Enter Number of Rooms: "))

new_data = pd.DataFrame({
    "avg_income": [income],
    "house_age": [age],
    "num_rooms": [rooms]
})

# Scale new data-
new_data_scaled = scaler.transform(new_data)

new_data_scaled = pd.DataFrame(
    new_data_scaled,
    columns=["avg_income", "house_age", "num_rooms"]
)

prediction = model.predict(new_data_scaled)

print(f"\nPredicted House Price:  ₹{prediction[0][0]:,.2f}")

# Save Model-

joblib.dump(model, "houses_model.joblib")
joblib.dump(scaler, "scalar.joblib")