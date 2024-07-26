# Program Description: A program for the One Stop Insurance Company that calculates insurance premiums and stores policy data.
# Author: Nicholas Power
# Dates: July 21-26, 2024

import datetime
import time
import sys

# Function to read constants from file
def read_constants(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [float(line.strip()) for line in lines]

# Function to calculate premium
def calculate_premium(NumCars, Liability, GlassCoverage, LoanerCar):
    DiscountRate = 0.25
    LiabilityCost = 130.00
    GlassCoverageCost = 86.00
    LoanerCarCost = 58.00
    
    BasePremium = 869.00
    AdditionalCarDiscount = (NumCars - 1) * BasePremium * DiscountRate
    TotalBasePremium = BasePremium + AdditionalCarDiscount
    
    ExtraCosts = 0
    if Liability == 'Y':
        ExtraCosts += LiabilityCost * NumCars
    if GlassCoverage == 'Y':
        ExtraCosts += GlassCoverageCost * NumCars
    if LoanerCar == 'Y':
        ExtraCosts += LoanerCarCost * NumCars
    
    TotalPremium = TotalBasePremium + ExtraCosts
    return TotalPremium

# Function to calculate HST
def calculate_hst(TotalPremium, HstRate):
    return TotalPremium * HstRate

# Function to calculate monthly payments
def calculate_monthly_payment(TotalCost, ProcessingFee, DownPayment=0):
    return (TotalCost + ProcessingFee - DownPayment) / 8

# Function to validate province
def validate_province(Province):
    ValidProvinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    return Province in ValidProvinces

# Function to validate phone number
def validate_phone_number(PhoneNumber):
    if len(PhoneNumber) == 10 and PhoneNumber.isdigit():
        return True
    else:
        return False

# Function to format phone number
def format_phone_number(PhoneNumber):
    return f"{PhoneNumber[:3]}-{PhoneNumber[3:6]}-{PhoneNumber[6:]}"

# Function to validate postal code
def validate_postal_code(PostalCode):
    if len(PostalCode) == 7 and PostalCode[1].isdigit() and PostalCode[4].isdigit() and PostalCode[0].isalpha() and PostalCode[2].isalpha() and PostalCode[5].isalpha() and PostalCode[3] == ' ' and PostalCode[6].isdigit():
        return True
    else:
        return False

# Function to write policy data to file
def write_policy_data(Filename, PolicyNumber, FirstName, LastName, Address, City, Province, PostalCode, PhoneNumber, NumCars, Liability, GlassCoverage, LoanerCar, PaymentMethod, DownPayment, TotalPremium):
    with open(Filename, 'a') as file:
        file.write(f"Policy Number: {PolicyNumber}\n")
        file.write(f"Customer Name: {FirstName} {LastName}\n")
        file.write(f"Address: {Address}, {City}, {Province}, {PostalCode}\n")
        file.write(f"Phone Number: {PhoneNumber}\n")
        file.write(f"Number of Cars: {NumCars}\n")
        file.write(f"Extra Liability: {Liability}\n")
        file.write(f"Glass Coverage: {GlassCoverage}\n")
        file.write(f"Loaner Car: {LoanerCar}\n")
        file.write(f"Payment Method: {PaymentMethod}\n")
        if DownPayment > 0:
            file.write(f"Down Payment: ${DownPayment:.2f}\n")
        file.write(f"Total Premium (pre-tax): ${TotalPremium:.2f}\n")
        file.write("----------------------------------------------------\n")

# Function to display a progress bar
def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

# Read constants
Constants = read_constants('Const.dat')
NextPolicyNumber, BasicPremium, DiscountRate, LiabilityCost, GlassCoverageCost, LoanerCarCost, HstRate, ProcessingFee = Constants

# Main program loop
while True:
    FirstName = input("Enter customer's first name: ").title()
    LastName = input("Enter customer's last name: ").title()
    Address = input("Enter address: ").title()
    City = input("Enter city: ").title()
    
    while True:
        Province = input("Enter province (e.g., ON): ").upper()
        if validate_province(Province):
            break
        else:
            print("Invalid province. Please enter again.")
    
    while True:
        PostalCode = input("Enter postal code (e.g., X9X 9X9): ").upper()
        if validate_postal_code(PostalCode):
            break
        else:
            print("Invalid postal code. Please enter again.")
    
    while True:
        PhoneNumber = input("Enter phone number (e.g., 9999999999): ")
        if validate_phone_number(PhoneNumber):
            PhoneNumber = format_phone_number(PhoneNumber)
            break
        else:
            print("Invalid phone number. Please enter again.")
    
    NumCars = int(input("Enter number of cars being insured: "))

    # Get and validate input for extra liability coverage
    while True:
        Liability = input("Extra liability coverage (Y/N): ").upper()
        if Liability == "Y":
            Liability = "Yes"
            break
        elif Liability == "N":
            Liability = "No"
            break
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

    # Get and validate input for glass coverage
    while True:
        GlassCoverage = input("Glass coverage (Y/N): ").upper()
        if GlassCoverage == "Y":
            GlassCoverage = "Yes"
            break
        elif GlassCoverage == "N":
            GlassCoverage = "No"
            break
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

    # Get and validate input for loaner car
    while True:
        LoanerCar = input("Loaner car (Y/N): ").upper()
        if LoanerCar == "Y":
            LoanerCar = "Yes"
            break
        elif LoanerCar == "N":
            LoanerCar = "No"
            break
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

   
    while True:
        PaymentMethod = input("Payment method - Full(F) Monthly(M) Down Pay(D): ").upper()
        if PaymentMethod in ["F", "M", "D"]:
            break
        else:
            print("Invalid payment method. Please enter again.")
    
    if PaymentMethod == "F":
        PaymentMethod = "Full"
    elif PaymentMethod == "M":
        PaymentMethod = "Monthly"
    elif PaymentMethod == "D":
        PaymentMethod = "Down Payment"
    
    DownPayment = 0
    if PaymentMethod == "Down Payment":
        DownPayment = float(input("Enter down payment amount: "))
    
    ClaimNumbers = []
    ClaimDates = []
    ClaimAmounts = []
    
    while True:
        ClaimNumber = input("Enter claim number (or 'done' to finish): ")
        if ClaimNumber.lower() == 'done':
            break
        ClaimDate = input("Enter claim date (YYYY-MM-DD): ")
        ClaimAmount = float(input("Enter claim amount: "))
        ClaimNumbers.append(ClaimNumber)
        ClaimDates.append(ClaimDate)
        ClaimAmounts.append(ClaimAmount)
    
    TotalPremium = calculate_premium(NumCars, Liability, GlassCoverage, LoanerCar)
    HST = calculate_hst(TotalPremium, HstRate)
    TotalCost = TotalPremium + HST
    
    if PaymentMethod == "Full":
        MonthlyPayment = 0
    else:
        MonthlyPayment = calculate_monthly_payment(TotalCost, ProcessingFee, DownPayment)
    
   # Print receipt
    print("\n\n")
    print("==============================================")
    print("            One Stop Insurance Co.            ")
    print("==============================================")

    print("Policy Information:")
    print("-------------------")
    print(f"Policy Number:   {int(NextPolicyNumber)}")
    print(f"Customer Name:   {FirstName} {LastName}")
    print(f"Address:         {Address}")
    print(f"                 {City}, {Province}, {PostalCode:>6}")
    print(f"Phone Number:    {PhoneNumber:>12}")
    print("----------------------------------------------")

    print("Coverage Details:")
    print("-----------------")
    print(f"Number of Cars:  {NumCars}")
    print(f"Extra Liability: {Liability}")
    print(f"Glass Coverage:  {GlassCoverage}")
    print(f"Loaner Car:      {LoanerCar}")
    print("----------------------------------------------")

    print("Payment Information:")
    print("--------------------")
    print(f"Payment Method: {PaymentMethod:<10}")
    if DownPayment > 0:
        print(f"Down Payment:                          ${DownPayment:<9.2f}")
    print("----------------------------------------------")
    print(f"Total Premium (pre-tax):              ${TotalPremium:<9.2f}")
    print(f"HST:                                   ${HST:<9.2f}")
    print(f"Total Cost:                           ${TotalCost:<9.2f}")
    if MonthlyPayment > 0:
        print(f"Monthly Payment:                       ${MonthlyPayment:<9.2f}")
    print("----------------------------------------------")

    print("Previous Claims:")
    print("----------------")
    print("Claim #         Claim Date           Amount")
    print("----------------------------------------------")
    for i in range(len(ClaimNumbers)):
        print(f"{ClaimNumbers[i]:<15} {ClaimDates[i]:<15}      ${ClaimAmounts[i]:<10.2f}")
    print("==============================================")

    
    # Write policy data to file
    total_iterations = 50

    for i in range(total_iterations + 1):
        time.sleep(0.1)  # Simulate some work
        progress_bar(i, total_iterations, prefix='Saving:', suffix='Complete', length=17)

    write_policy_data('Policies.dat', NextPolicyNumber, FirstName, LastName, Address, City, Province, PostalCode, PhoneNumber, NumCars, Liability, GlassCoverage, LoanerCar, PaymentMethod, DownPayment, TotalPremium)
    
    # Increment policy number
    NextPolicyNumber += 1
    print()
    # Check if user wants to enter another customer
    continueEntering = input("Do you want to enter another customer? (Y/N): ").upper()
    if continueEntering != 'Y':
        break

print("Thank you for using One Stop Insurance Company system!")
