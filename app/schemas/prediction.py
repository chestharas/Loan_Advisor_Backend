from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    Province: str
    Region_Type: str = Field(..., alias="Region Type")
    Age: int
    Gender: str
    Employment_Type: str = Field(..., alias="Employment Type")
    Annual_Income_USD: float = Field(..., alias="Annual Income (USD)")
    Credit_History: str = Field(..., alias="Credit History")
    Existing_Debt_USD: float = Field(..., alias="Existing Debt (USD)")
    Savings_Assets_USD: float = Field(..., alias="Savings/Assets (USD)")
    Loan_Type: str = Field(..., alias="Loan Type")
    Loan_Amount_USD: float = Field(..., alias="Loan Amount (USD)")
    Loan_Term_Years: int = Field(..., alias="Loan Term (Years)")
    Annual_Interest_Rate_Percent: float = Field(..., alias="Annual Interest Rate (%)")
    Collateral_USD: float = Field(..., alias="Collateral (USD)")

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "Province": "Phnom Penh",
                "Region Type": "Urban",
                "Age": 35,
                "Gender": "Male",
                "Employment Type": "Full-Time",
                "Annual Income (USD)": 12000.0,
                "Credit History": "Good",
                "Existing Debt (USD)": 5000.0,
                "Savings/Assets (USD)": 2000.0,
                "Loan Type": "Personal",
                "Loan Amount (USD)": 10000.0,
                "Loan Term (Years)": 3,
                "Annual Interest Rate (%)": 5.5,
                "Collateral (USD)": 3000.0
            }
        }