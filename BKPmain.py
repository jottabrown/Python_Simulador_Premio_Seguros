#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

# Dependencies:
# - fastapi: FastAPI web framework
# - pydantic: Data validation and settings management using Python type annotations
# - pytest: Testing framework for Python
# - uvicorn: ASGI server to run FastAPI apps
# - httpx: HTTP client for asynchronous requests

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class CarInsuranceInput(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None


class CarInsuranceOutput(CarInsuranceInput):
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float


def calculate_rate(car: CarInsuranceInput) -> float:
    age_rate = (2025 - car.year) * 0.005  # 0.5% por ano de idade
    value_rate = (car.value // 10000) * 0.005  # 0.5% para cada 10.000 dólares
    return age_rate + value_rate


@app.post("/calculate", response_model=CarInsuranceOutput)
def calculate_insurance(car: CarInsuranceInput):
    applied_rate = calculate_rate(car)
    base_premium = car.value * applied_rate
    deductible_value = base_premium * car.deductible_percentage
    final_premium = base_premium - deductible_value + car.broker_fee
    policy_limit = car.value * (1 - car.deductible_percentage)

    return CarInsuranceOutput(
        **car.model_dump(),
        applied_rate=applied_rate * 100,
        policy_limit=policy_limit,
        calculated_premium=final_premium,
        deductible_value=deductible_value
    )

# OBS tem que rodar o servidor primeiro.
