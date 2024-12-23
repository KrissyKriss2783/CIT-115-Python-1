#Code a function to get valid float input with error handling and validation
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive non-zero number.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Function to get the sales tax based on the state
def getSalesTax(state):
    stateTaxRates = {"CT": 0.06, "MA": 0.0625, "ME": 0.085, "NH": 0.0, "RI": 0.07, "VT": 0.06, }
    return stateTaxRates.get(state.upper(), 0.0)

# Write a function to calculate the number of gallons of paint needed and round up 
def getGallonsOfPaint(squareFeet, feetPerGallon):
    return (squareFeet + feetPerGallon - 1) // feetPerGallon  

# Function to calculate labor hours needed
def getLaborHours(laborHoursPerGallon, gallons):
    return laborHoursPerGallon * gallons

# Function to calculate the labor cost
def getLaborCost(laborHours, laborChargePerHour):
    return laborHours * laborChargePerHour

# Function to calculate the paint cost
def getPaintCost(gallons, paintPrice):
    return gallons * paintPrice

# Function to display the cost estimate and save to a file
def showCostEstimate(paintCost, laborCost, tax, totalCost, lastName):
    print(f"Paint charges: ${paintCost:,.2f}")
    print(f"Labor charges: ${laborCost:,.2f}")
    print(f"Tax: ${tax:,.2f}")
    print(f"Total cost: ${totalCost:,.2f}")
    
    # Output file created
    fileName = f"{lastName}_PaintJobOutput.txt"
    with open(fileName, "w") as file:
        file.write(f"Paint charges: ${paintCost:,.2f}\n")
        file.write(f"Labor charges: ${laborCost:,.2f}\n")
        file.write(f"Tax: ${tax:,.2f}\n")
        file.write(f"Total cost: ${totalCost:,.2f}\n")
    
    # Output 
    print(f"File: {fileName} was created.")

def main():
    # Prompt the user for inputs
    squareFeet = getFloatInput("Enter wall space in square feet: ")
    paintPrice = getFloatInput("Enter paint price per gallon: ")
    feetPerGallon = getFloatInput("Enter feet per gallon: ")
    laborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    laborChargePerHour = getFloatInput("Labor charge per hour: ")
    state = input("State job is in: ").strip()
    lastName = input("Customer Last Name: ").strip()

    # Calculations
    gallons = getGallonsOfPaint(squareFeet, feetPerGallon)
    laborHours = getLaborHours(laborHoursPerGallon, gallons)
    laborCost = getLaborCost(laborHours, laborChargePerHour)
    paintCost = getPaintCost(gallons, paintPrice)
    taxRate = getSalesTax(state)
    tax = (paintCost + laborCost) * taxRate
    totalCost = paintCost + laborCost + tax

    # Output the results
    print(f"\nGallons of paint: {gallons}")
    print(f"Hours of labor: {laborHours:.2f}")
    showCostEstimate(paintCost, laborCost, tax, totalCost, lastName)

main()
