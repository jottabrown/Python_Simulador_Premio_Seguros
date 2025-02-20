#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------
class PremiumCalculator:
    def __init__(self, car):
        self.car = car

    def calculate_rate(self):
        age_rate = (2025 - self.car.year) * 0.005  # 0.5% por ano de idade
        value_rate = (self.car.value // 10000) * 0.005  # 0.5% para cada 10.000 dólares
        return age_rate + value_rate

    def calculate_base_premium(self, rate):
        return self.car.value * rate

    def calculate_final_premium(self, base_premium):
        deductible_value = base_premium * self.car.deductible_percentage
        return base_premium - deductible_value + self.car.broker_fee