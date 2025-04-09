import pandas as pd
import joblib
import logging

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Load the trained models
try:
    risk_model = joblib.load("app/models/risk_model.joblib")
    loan_model = joblib.load("app/models/loan_model.joblib")
    logging.info("Models loaded successfully")
except Exception as e:
    logging.error("Failed to load models: %s", e)
    raise

def predict_risk(data):
    """
    Predict the risk category for the given input data.
    Expects a pandas DataFrame with the correct column names.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input to predict_risk must be a pandas DataFrame")

    # Log the DataFrame columns for debugging
    logging.info("DataFrame columns in predict_risk: %s", data.columns.tolist())

    # Make prediction
    try:
        prediction = risk_model.predict(data)[0]  # Assuming single prediction
        logging.info("Risk prediction: %s", prediction)
        return prediction  # e.g., "Low", "Medium", "High"
    except Exception as e:
        logging.error("Error during risk prediction: %s", e)
        raise

def predict_loan(data):
    """
    Predict the loan approval status for the given input data.
    Expects a pandas DataFrame with the correct column names.
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input to predict_loan must be a pandas DataFrame")

    # Log the DataFrame columns for debugging
    logging.info("DataFrame columns in predict_loan: %s", data.columns.tolist())

    # Make prediction
    try:
        prediction = loan_model.predict(data)[0]  # Assuming single prediction
        logging.info("Loan prediction: %s", prediction)
        return prediction  # 1 for Approved, 0 for Rejected
    except Exception as e:
        logging.error("Error during loan prediction: %s", e)
        raise