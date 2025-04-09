import os
from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title="Loan Risk Prediction API")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Risk Prediction API"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)