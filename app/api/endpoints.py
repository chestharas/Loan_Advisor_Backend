from fastapi import APIRouter
from app.schemas.prediction import PredictionInput
from app.services.predict import predict_risk, predict_loan
import pandas as pd
import logging

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

router = APIRouter(prefix="/predict", tags=["predictions"])

@router.post("/risk")
def risk_prediction(input_data: PredictionInput):
    try:
        # Convert Pydantic model to dictionary
        input_dict = input_data.dict(by_alias=True)  # Use aliases to match expected column names

        # Convert to DataFrame
        df = pd.DataFrame([input_dict])

        # Log the DataFrame columns for debugging
        logging.info("DataFrame columns in risk_prediction: %s", df.columns.tolist())

        # Make prediction
        result = predict_risk(df)
        return {"risk_category": result}
    except Exception as e:
        logging.error("Error in risk_prediction: %s", e)
        return {"error": str(e)}

@router.post("/loan")
def loan_prediction(input_data: PredictionInput):
    try:
        # Convert Pydantic model to dictionary
        input_dict = input_data.dict(by_alias=True)  # Use aliases to match expected column names

        # Convert to DataFrame
        df = pd.DataFrame([input_dict])

        # Log the DataFrame columns for debugging
        logging.info("DataFrame columns in loan_prediction: %s", df.columns.tolist())

        # Make prediction
        result = predict_loan(df)
        return {"loan_status": "Approved" if result == 1 else "Rejected"}
    except Exception as e:
        logging.error("Error in loan_prediction: %s", e)
        return {"error": str(e)}

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.get("/version")
def version_check():
    return {"message": "Updated endpoints.py with aligned column names"}