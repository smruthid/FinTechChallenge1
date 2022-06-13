#!/usr/bin/env python
# coding: utf-8

import csv
from pathlib import Path


print("Part 1")
loan_costs = [500, 600, 200, 1000, 450]
number_of_loans = len(loan_costs)
total_loan_amt = sum(loan_costs)
average_loan = total_loan_amt/number_of_loans
print(f"There are {number_of_loans} loans.")
print(f"The total loan amount is ${total_loan_amt}.")
print(f"The average loan amount is ${average_loan}.")





print("Part 2")
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
future_val = loan.get("future_value")
months_left = loan.get("remaining_months")
print(f"The future value is ${future_val}")
print(f"There are {months_left} months remaining.")
discount_rate = 0.2
present_val = future_val/((1+(discount_rate/12))**months_left)
if present_val >= loan["loan_price"]:
    print("This is definitely worth buying")
else:
    print("Do not buy this!!!")




print("Part 3")
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
def calc_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/((1+(annual_discount_rate/12))**remaining_months)
    return present_value
present_value = calc_present_value(new_loan["future_value"], 0.2, new_loan["remaining_months"])
print(f"The present value of the loan is: {present_value}")




print("Part 4")
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)        
print(inexpensive_loans)



print("Part 5")
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")
with open(output_path, 'w', newline='') as output_file:
    csvwriter = csv.writer(output_file)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())






