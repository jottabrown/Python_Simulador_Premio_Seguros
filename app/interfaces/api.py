#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from app.core.entities import CarInsurance
from app.use_cases.calculate_premium import CalculatePremium

app = FastAPI()

# Pydantic models para validar a entrada e saída
class CarInsuranceInput(BaseModel):
    make: str
    model: str
    year: int
    value: float
    deductible_percentage: float
    broker_fee: float
    registration_location: Optional[str] = None

class CarInsuranceOutput(BaseModel):
    car: str
    applied_rate: str
    final_premium: float

@app.post("/calculate", response_model=CarInsuranceOutput)
def calculate_insurance(car_input: CarInsuranceInput):
    # Criando a entidade a partir da entrada
    car = CarInsurance(
        make=car_input.make,
        model=car_input.model,
        year=car_input.year,
        value=car_input.value,
        deductible_percentage=car_input.deductible_percentage,
        broker_fee=car_input.broker_fee,
        registration_location=car_input.registration_location
    )

    # Usando o caso de uso para calcular o prêmio
    calculate_premium = CalculatePremium(car)
    result = calculate_premium.execute()

    # Retornando os resultados
    return CarInsuranceOutput(**result)