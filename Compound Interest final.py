# name the values

PV = float(input("Enter the starting principal: "))
R = float(input("Enter the annual interest rate: "))
m = int(input("How many times per year is the interest compounded? "))
t = int(input("For how many years will the account earn interest? "))

# Future value = FV
# Int for whole number and no decimal
# Convert the interest rate
r = R / 100

#Calculate the future value using the formula given
#Formula converted from Excel
# =A3 * (1 +(A4 / 100) / A6) ^ (A6 * A5)
# =1000 * (1 + (2.5/100) ^ (12 * 2)

FV = PV * (1 + r/m) ** (m * t)


# Output the result
print(f"At the end of 2 years you will have $ {FV:,.2f} ")

