# 🏠 House Price Prediction using Multiple Linear Regression

A Machine Learning project that predicts house prices using Multiple Linear Regression. The project stores house data in a MySQL database, reads it using Pandas, preprocesses the data, trains a regression model, evaluates its performance, and predicts house prices based on user input.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- PyMySQL
- MySQL Workbench
- Joblib

## Features

- Read data from a local MySQL database
- Perform feature scaling using StandardScaler
- Train a Multiple Linear Regression model
- Evaluate the model using R² Score and Mean Absolute Error (MAE)
- Predict house prices based on user input
- Save the trained model and scaler using Joblib

## Project Structure

```
House-Price-Prediction/
│
├── house_price_prediction.py
├── database.sql
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
```

## Database

Database Name:

```
house_db
```

Table Name:

```
houses
```

Columns:

- avg_income
- house_age
- num_rooms
- price

## Database

![Database](screenshots/database.png)

## Program Output

![Output](screenshots/output.png)


## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/House-Price-Prediction.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Open `database.sql` in MySQL Workbench and execute it.

Run the project:

```bash
python house_price_prediction.py
```

## Sample Output

```
Enter Average Income: 900
Enter House Age: 9
Enter Number of Rooms: 5

Predicted House Price: ₹23,450.72
```

## Author

Harsh Mishra
