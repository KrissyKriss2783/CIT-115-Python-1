# Code a Function to get a valid float input from the user
def getFloatInput(prompt):
    while True:
        try:
            # Getting the input from user
            user_input = input(prompt)
            # Converting the input into a float
            value = float(user_input)
            
            # Check if the value is positive and a non-zero
            if value <= 0:
                print("\nEnter another value Y or N:\n")
            else:
                return value
        except ValueError:
            # If the input is not a valid float, display error and prompt again
            print("\nInput a number that is greater than 0.\n")

# Code the function to calculate the median of a list of numbers and sort the list first
def getMedian(values):
    values.sort()  
    n = len(values)
    
    if n % 2 == 1:
        # If the number of entries is odd, divide the count by 2 and use that entry as the median.
        return float(values[n // 2])
    else:
        # If the number of entries is even, divide by 2, average both entries to get the new median
        med = n // 2
        return (values[med - 1] + values[med]) / 2

# Process the sales data
def main():
    sales_values = []  
    
    while True:
        # Get the sales price from the user
        fSalesPrice = getFloatInput("Enter property sales value:")
        
        # Add the sales price to the list
        sales_values.append(fSalesPrice)
        
        # Ask if the user wants to enter another value with a y or n
        while True:
            another_value = input("Enter another value Y or N: ").strip().lower()
            if another_value == 'y':
                break
            elif another_value == 'n':
                break
            else:
                print("\nEnter another value Y or N.\n")
        
        # Exit the loop if 'N' or 'n' is entered
        if another_value == 'n':
            break
    
    # Sort the list of the sales values
    sales_values.sort()
    
    # Output all the values formatted as currency with 2 decimals each value
    print()
    for value in sales_values:
        print(f"Property value: $ {value:>10,.2f}")
    
    min_value = sales_values[0]
    print(f"\nMinimum value: $ {min_value:>10,.2f}")
    
    max_value = sales_values[-1]
    print(f"Maximum value: $ {max_value:>10,.2f}")
    
    total_value = sum(sales_values)
    print(f"Total value:   $ {total_value:>10,.2f}")
    
    avg_value = total_value / len(sales_values)
    print(f"Average value: $ {avg_value:>10,.2f}")
    
    median_value = getMedian(sales_values)
    print(f"Median value:  $ {median_value:>10,.2f}")
    
    commission = total_value * 0.03
    print(f"Commission:    $ {commission:>10,.2f}")

# Run the main function
if __name__ == "__main__":
    main()
