#Assign sQuote the value of "Vernon Davis"
sQuote = str("Vernon Davis")

#Assign sQuote2 the value of "Vernon Davis"
sQuote = str("Vernon Davis")

# Extract each character out of the string one at a time using a while:
iPosition = 0
while iPosition < len(sQuote):
    sCharacter = sQuote[iPosition]
    print(sCharacter)
    iPosition += 1

# Extract each character out of the string one at a time using a for:
for sCharacter in sQuote:
    print (sCharacter)

# Extract every other character out of the string one at a time using a for:
for iPosition in range(0, len(sQuote), 2):
    sCharacter = sQuote[iPosition]
    print(sCharacter)

#Assign my dad's full name to 3 different variables:
sFirst = "George"
sMiddle = "Clement"
sLast = "Lamb"

#George Clement Lamb
#0123456789012345678
# Concantenation:
sFullName = sFirst + " " + sMiddle + " " + sLast
print (sFullName)

#Slicing also known as substrin, extrating or parsing:
sSlice = sFullName[0:6]
print(sSlice)

sSlice = sFullName[:8]
print(sSlice)

sSlice = sFullName[8:]
print(sSlice)

sSlice = sFullName[0:19:2]
print(sSlice)

sSlice = sFullName[-6:]
print(sSlice)

#using Pything's string functions:
print(len(sFullName))




