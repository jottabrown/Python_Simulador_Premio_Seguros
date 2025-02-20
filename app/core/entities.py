#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

from typing import Optional

class CarInsurance:
    def __init__(self, make: str, model: str, year: int, value: float,
                 deductible_percentage: float, broker_fee: float,
                 registration_location: Optional[str] = None):
        self.make = make
        self.model = model
        self.year = year
        self.value = value
        self.deductible_percentage = deductible_percentage
        self.broker_fee = broker_fee
        self.registration_location = registration_location

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"