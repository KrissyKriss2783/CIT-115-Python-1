# Code Grade Analyzer
#1. Prompt for the person’s name that the Grade Analyzer is for and store in a variable.
sName = input("Name of person that we are calculating the grades for: ")

#2. Prompt the user to for a person’s 4 test scores. Only whole numbers should be accepted.
testScore1 = int(input("Test Score 1: "))
testScore2 = int(input("Test Score 2: "))
testScore3 = int(input("Test Score 3: "))
testScore4 = int(input("Test Score 4: "))

# 3. Prompt the user asking if the Lowest Grade should be determined and dropped from the calculation.
YesOrNo = input("Do you wish to drop the lowest grade Y or N? ").upper()

#4. Code a Python if statement to make sure each of the 4 test scores is not less than zero.
if testScore1 <= 0 or testScore2 <= 0 or testScore3 <= 0 or testScore4 <= 0:
    print("Test scores must be greater than 0")
    raise SystemExit()

#5. Code a Python if statement to make sure the Drop Lowest input equals Y or N. 
if YesOrNo != "Y" and YesOrNo != "N":
    print("Enter Y or N to Drop the Lowest Grade. ")
    raise SystemExit()

#6. Code a Python if/else statement using the entered Drop Lowest value. 
lowest = 0
if YesOrNo == "Y":
    if testScore1 < testScore2 and testScore1 < testScore3 and testScore1 < testScore4:
        lowest = testScore1
    elif testScore2 < testScore3 and testScore2 < testScore4:
        lowest = testScore2
    elif testScore3 < testScore4:
        lowest = testScore3
    else:
        lowest = testScore4

#7. Make sure the Average is a float data type to have a decimals in the average such as 78.5

    fAverage = (testScore1 + testScore2 + testScore3 + testScore4 - lowest) / 3
else:
    fAverage = (testScore1 + testScore2 + testScore3 + testScore4) / 4


#8. Write Python if/elif/else statements to determine the test average’s letter grade value.

sGrade = ""
if fAverage >= 97.0:
    sGrade = "A+"
elif fAverage >= 94.0:
    sGrade = "A"
elif fAverage >= 90.0:
    sGrade = "A-"
elif fAverage >= 87.0:
    sGrade = "B+"
elif fAverage >= 84.0:
    sGrade = "B"
elif fAverage >= 80.0:
    sGrade = "B-"
elif fAverage >= 77.0:
    sGrade = "C+"
elif fAverage >= 74.0:
    sGrade = "C"
elif fAverage >= 70.0:
    sGrade = "C-"
elif fAverage >= 67.0:
    sGrade = "D+"
elif fAverage >= 64.0:
    sGrade = "D"
elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"


#9. Output the Person’s Name, calculated Average and Letter Grade

print(f"{sName}'s test average is: {fAverage:.1f}") 
print(f"{sName}'s Letter Grade for the test is: {sGrade}")

