#!/usr/bin/python3

"""Calculates user's monthly and potential future savings"""

# Retrieve user's financial details
monthly_income = int(input('Enter your monthly income:'))
total_monthly_expenses = int(input('Enter your total monthly expenses:'))

# User monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Annual interest rate - 5%
interest_rate = 0.05
annual_saving = monthly_savings * 12

# Projected annual savings in 1 year
projected_annual_savings = annual_saving + annual_saving * interest_rate

# Print user's monthly savings and annual savings inclusive of interest
print(f'Your monthly savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest, '
    f'is: ${projected_annual_savings:.0f}'
)
