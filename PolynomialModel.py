import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Function to load and preprocess COVID-19 data
def load_covid_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Drop rows with missing values
    df = df.dropna()

    return df

# Function to train a logistic regression classifier and make predictions
def train_logistic_regression(data):
    # Features: Province/State, Country/Region, Lat, Long, Confirmed, Active
    X = data[['Lat', 'Long', 'Confirmed', 'Active']]
    # Target variable: 'Deaths' or 'Recovered'
    y = data['Deaths'].astype(bool)  # Convert 'Deaths' to binary (True/False)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the data
    scaler = StandardScaler()
    X_train_poly = scaler.fit_transform(X_train)
    X_test_poly = scaler.transform(X_test)

    # Create a logistic regression model and fit it to the training data
    model = LogisticRegression(max_iter=1000)  # Increase max_iter to avoid convergence warning
    model.fit(X_train_poly, y_train)

    # Make predictions on the test data
    predictions = model.predict(X_test_poly)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy:.2f}')
    print(classification_report(y_test, predictions))

# Main function
def main():
    file_path = 'covid_19_clean_complete.csv'  # Replace with the actual path to your dataset
    covid_data = load_covid_data(file_path)

    # Train a logistic regression classifier
    train_logistic_regression(covid_data)

if _name_ == "_main_":
    main()
