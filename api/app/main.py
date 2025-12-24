from fastapi import FastAPI
from app.models.health import HealthResponse

app = FastAPI(title="NetWorth MVP API")

@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")
