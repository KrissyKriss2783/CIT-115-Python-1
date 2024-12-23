# Compound Interest Program

def enterInput(prompt, isPositive=True):
    while True:
        try:
            value = float(input(prompt))
            if isPositive and value <= 0:
                print("Input must be a positive numeric value")
            elif not isPositive and value < 0:
                print("Input must be 0 or greater")
            else:
                return value
        except ValueError:
            print("Input must be a positive numeric value")

# Step 1: Get the users inputs as requested
fDeposit = enterInput("What is the Original Deposit (positive value): $")
fInterestRatePercentage = enterInput("What is the Interest Rate (positive value): ")
fNumMonths = int(enterInput("What is the Number of Months (positive value): "))
fGoal = enterInput("What is the Goal Amount (can enter 0 but not negative): $", isPositive=False)

# Step 2: Convert the interest rate percentage to a monthly interest rate with Monthly interest rate as a decimal
fMonthlyInterestRate = fInterestRatePercentage / 100 / 12  

# Step 3: Code a loop to calculate the balance for each month up to 12 months
# Initial deposit value
fBalance = fDeposit  

# Loop through 12 months
for month in range(1, 13):  
    fBalance = fDeposit * (1 + fMonthlyInterestRate) ** month
    print(f"Month: {month:2d}  Account Balance is: ${fBalance:,.2f}")

# Step 4: Code a loop to predict how many months it will take to reach the goal
# Reset the balance to the original deposit
fBalance = fDeposit  
fMonthCount = 0

while fBalance < fGoal:
    fMonthCount += 1
    fBalance = fDeposit * (1 + fMonthlyInterestRate) ** fMonthCount

# Output the results and format it with thousands separator
print(f"\nIt will take: {fMonthCount:,} months to reach the goal of ${fGoal:,.2f}.")
