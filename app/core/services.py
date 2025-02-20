#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

from .entities import CarInsurance
from .value_objects import Rate

class PremiumCalculator:
    def __init__(self, car: CarInsurance):
        self.car = car

    def calculate_rate(self) -> Rate:
        age_rate = (2025 - self.car.year) * 0.005  # 0.5% por ano de idade
        value_rate = (self.car.value // 10000) * 0.005  # 0.5% para cada 10.000 dólares
        total_rate = age_rate + value_rate
        return Rate(total_rate)

    def calculate_premium(self, rate: Rate) -> float:
        base_premium = self.car.value * rate.value
        deductible_value = base_premium * self.car.deductible_percentage
        return base_premium - deductible_value + self.car.broker_fee