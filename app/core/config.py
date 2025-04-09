from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODEL_DIR: str = "app/models/"
    RISK_MODEL_PATH: str = f"{MODEL_DIR}risk_model.joblib"
    LOAN_MODEL_PATH: str = f"{MODEL_DIR}loan_model.joblib"
    API_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"  # Optional: load from .env file if used

settings = Settings()