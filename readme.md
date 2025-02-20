# Car Insurance Premium Simulator

## Description

The **Car Insurance Premium Simulator** is a backend service designed to calculate car insurance premiums based on various factors, such as car age, value, deductible percentage, and a broker's fee. The service is implemented using **FastAPI**, adhering to **Domain-Driven Design (DDD)**, **S.O.L.I.D. principles**, and **Clean Architecture**. 

This project ensures users receive accurate and configurable insurance premium calculations, making it easy to adjust rates or configurations without modifying the code.

## Core Features

1. **Dynamic Rate Calculation**
   - For each year since the car was produced, the rate increases by 0.5%.
   - For each $10,000 of the car’s value, an additional 0.5% is added to the rate.
   
2. **Premium Calculation**
   - **Base Premium** = Car value * Applied rate.
   - **Deductible Discount** = Base premium * Deductible percentage.
   - **Final Premium** = Base Premium - Deductible Discount + Broker’s Fee.

3. **Policy Limit Calculation**
   - **Base Policy Limit** = Car value * Coverage percentage (default 100%).
   - **Deductible Value** = Base policy limit * Deductible percentage.
   - **Final Policy Limit** = Base policy limit - Deductible value.

4. **(Optional) GIS Adjustment**
   - If a registration location is provided, the rate can be adjusted based on geographic risk factors.
   - The rate variation can be between -2% and +2%, depending on the location’s risk level.

## Input Interface

The service expects the following input for the car details:

- **make** (string): e.g., `"Toyota"`
- **model** (string): e.g., `"Corolla"`
- **year** (integer): e.g., `2012`
- **value** (float): e.g., `100000.0`
- **deductible_percentage** (float): e.g., `0.10` (for 10%)
- **broker_fee** (float): e.g., `50.0`
- **registration_location** (optional, string): e.g., `"New York"`

## Output Interface

The output will return the following details:

- **make**, **model**, **year**, **value**, **deductible_percentage**, **broker_fee** (echoed from input)
- **applied_rate** (final calculated rate after adjustments)
- **policy_limit** (final policy limit after deductible application)
- **calculated_premium** (final premium after deductible and broker fee adjustments)
- **deductible_value** (monetary value calculated from the original policy limit and deductible percentage)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jottabrown/Python_Simulador_Premio_Seguros.git

2. Navigate to the project directory:

   cd car-insurance-premium-simulator

3. Create a virtual environment:
   python -m venv venv

4. Activate the virtual environment:
   .\venv\Scripts\Activate

5. Install the dependencies:
   pip install -r requirements.txt

## Running Tests
To run the tests, execute the following: pytest

##Running the Service
To run the service locally:
1. python main.py
2. python run.py

## Author

Jean Alves
Position: Systems Analyst | Software Engineer | Machine Learning Engineer
Email: jeancleber.alves@hotmail.com
LinkedIn: Jean Alves
