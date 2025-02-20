#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

from app.core.services import PremiumCalculator
from app.core.entities import CarInsurance
from app.core.value_objects import Rate

class CalculatePremium:
    def __init__(self, car: CarInsurance):
        self.car = car
        self.calculator = PremiumCalculator(car)

    def execute(self):
        # Calculando a taxa
        rate = self.calculator.calculate_rate()
        
        # Calculando o prêmio
        final_premium = self.calculator.calculate_premium(rate)

        # Retornando os dados necessários
        return {
            "car": str(self.car),
            "applied_rate": str(rate),
            "final_premium": final_premium
        }