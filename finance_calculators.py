# Financial Calculator Capstone Project

import math
# The below code show's the two avalible finance calculator options
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("\n")
calculation_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

calculation_choice = calculation_choice.lower()

# investment is chosen at initial input
if calculation_choice == "investment":
    deposit_1 = float(input("Please enter the amount you'll be depositing £"))
    interest_rate_1 = float(input("Please enter the interest rate (No need to included %. e.g 10): "))
    years_investing_1 = float(input("Please enter the number of years you plan on investing: "))
    interest_1 = (input("Please confirm if you'll like 'simple' or 'compound' interest caluctated? "))
    interest_1 = interest_1.lower()
# if simple interest is chosen
    if interest_1 == "simple":
        simple_interest = deposit_1*(1+(interest_rate_1/100)*years_investing_1)
        simple_interest_2_deciamls = ("%.2f" % simple_interest)
        print(f"Your total amount once interest is applied will be: £{simple_interest_2_deciamls}")
 # if compound interest is chosen
    elif interest_1 == "compound":
        compound_interest = deposit_1 * math.pow((1+(interest_rate_1/100)),years_investing_1)
        compound_interest_2_deciamls = ("%.2f" % compound_interest)
        print(f"Your total amount once interest is applied will be: £{compound_interest_2_deciamls}")

# bond is chosen at initial input
elif calculation_choice == "bond":
    house_value = float(input("Please confirm the value of the house: "))
    interest_rate_2 = float(input("Please enter the interest rate (No need to included %. e.g 10): "))
    time_taken_to_repay = float(input("Please confirm the number of months you plan to take to repay the bond: "))
    interest_rate_2_monthly = float((interest_rate_2/100)/12)    
    bond_repayment = (interest_rate_2_monthly * house_value) / (1-(1 + interest_rate_2_monthly) **(-time_taken_to_repay))
    bond_repayment_2_deciamls = ("%.2f" % bond_repayment)
    print(f"Your monthly bond repayment will be £{bond_repayment_2_deciamls}")
# error message shown if invalid entry is entered at the initial input
else:
    print("Oops you have not entered a valid calculation choice, please try again.")

