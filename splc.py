"""
    A Equivalent Sound Pressure Level Calculator

    Abbreviations:
    - SPL = Sound Pressure Level
    - ESPL = Equivalent Sound Pressure Level
"""

import math

spl = []    # Initialize the list for the SPLs values
pressures_levels = [] # Initialize the list for the pressures levels

print('ESPL Calculator')
quantity = int(input('Number of Sound Pressure Levels that you will input: '))

for element in range(0, quantity):
    # Get the values for the number of SPLs that the user will input
    # After getting the values it appends to the list
    inputed_SPL = int(input('SPL('+ str(element+1)+ '): '))
    spl.append(inputed_SPL)

for value in spl:
    # Converts the SPL into pressure level
    # After the conversion process it appends to the list
    spl_to_pressure_level = 10**(value/10)
    pressures_levels.append(spl_to_pressure_level)

pressures_levels_sum= sum(list(pressures_levels)) # Sums all the values stored in the list
ESPL = 10*math.log10(pressures_levels_sum) # Calculates the ESPL using the sum done before

print('The equivalent SPL: ' + str(ESPL) + ' dB') # Prints the ESPL value
