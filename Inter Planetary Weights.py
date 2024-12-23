#1. The constants for the planets' surface gravity factors
    # Weight = Earth Weight * Surface Gravity Factor
    # sName = String/Variable
    # Float * Float = Float
    # Float * Int = Float
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

#2. Prompt user for the person's name and Earth weight
    # n is for numbers
    # s is for strings
sName = input("What is your name: ")
nEarthWeight = float(input("What is your weight: "))

#3. Calculate weights on the different planets:

#For example if you weigh 100 pounds on earth on Mars you would be:
    # Mars Weight 38 = 100 x .38
    
nMercuryWeight = nEarthWeight * MERCURY_GRAVITY
nVenusWeight = nEarthWeight * VENUS_GRAVITY
nMoonWeight = nEarthWeight * MOON_GRAVITY
nMarsWeight = nEarthWeight * MARS_GRAVITY
nJupiterWeight = nEarthWeight * JUPITER_GRAVITY
nSaturnWeight = nEarthWeight * SATURN_GRAVITY
nUranusWeight = nEarthWeight * URANUS_GRAVITY
nNeptuneWeight = nEarthWeight * NEPTUNE_GRAVITY
nPlutoWeight = nEarthWeight * PLUTO_GRAVITY

#4. Output/print
print(f"{sName} here are your weights on our Solar System's planets:")

print(f"{'Weight on Mercury:':22}{nMercuryWeight:10.2f}")
print(f"{'Weight on Venus:':22}{nVenusWeight:10.2f}")
print(f"{'Weight on our Moon:':22}{nMoonWeight:10.2f}")
print(f"{'Weight on Mars:':22}{nMarsWeight:10.2f}")
print(f"{'Weight on Jupiter:':22}{nJupiterWeight:10.2f}")
print(f"{'Weight on Saturn:':22}{nSaturnWeight:10.2f}")
print(f"{'Weight on Uranus:':22}{nUranusWeight:10.2f}")
print(f"{'Weight on Neptune:':22}{nNeptuneWeight:10.2f}")
print(f"{'Weight on Pluto:':22}{nPlutoWeight:10.2f}")


