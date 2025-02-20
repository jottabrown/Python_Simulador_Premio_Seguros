#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

class Rate:
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("Rate cannot be negative")
        self.value = value

    def __str__(self):
        return f"{self.value * 100}%"