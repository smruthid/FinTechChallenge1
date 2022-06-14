#!/usr/bin/env python
# coding: utf-8

import csv
from pathlib import Path


#Fintech Challenge 1 Part 1
loan_costs = [500, 600, 200, 1000, 450]
number_of_loans = len(loan_costs)
total_loan_amt = sum(loan_costs)
average_loan = total_loan_amt/number_of_loans
print(f"There are {number_of_loans} loans.")
print(f"The total loan amount is ${total_loan_amt}.")
print(f"The average loan amount is ${average_loan}.")





#Fintech Challenge 2 Part 2
#information about the loan
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

#discount rate is the minimum expected return 
discount_rate = 0.2
present_val = future_val/((1+(discount_rate/12))**months_left)

#if present value is greater than how much loan is taken out, then buy it
if present_val >= loan["loan_price"]:
    print("This is definitely worth buying because the present value is greater than the loan cost.")
else:
    print("Do not buy this!!! This item is worth less than what you would be paying for it.")




#Fintech Challenge 1 Part 3
#information about the new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#function to calculate present value, used to get rid of repetition
def calc_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/((1+(annual_discount_rate/12))**remaining_months)
    return present_value

#calculating present value using the function
present_value = calc_present_value(new_loan["future_value"], 0.2, new_loan["remaining_months"])
print(f"The present value of the loan is: {present_value}")




#Fintech Challenge 1 Part 4
#information about multiple loans
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

#creating empty list to store loans that are less than or equal to 500
inexpensive_loans = []
#iterating through all the loans
for loan in loans:
    #checking is loan price is less than or equal to 500
    if loan["loan_price"] <= 500:
        #adding the inexpensive loans to the list
        inexpensive_loans.append(loan)        
print("List of inexpensive loans: ",inexpensive_loans)



#Fintech Challenge 1 Part 5
#the header list contains the headers that will be added to the .csv file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
#output_path is the relative path where csv is created
output_path = Path("inexpensive_loans.csv")
#opening .csv file as a file to be written to
with open(output_path, 'w', newline='') as output_file:
    csvwriter = csv.writer(output_file)
    #writing the headers to the file
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        #writing the inexpensive loans to the file
        csvwriter.writerow(loan.values())
print("Inexpensive loans written to inexpensive_loans.csv file")






