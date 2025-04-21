###############################################################################
# Program Filename: Assignment2Code.py
# Author:  Alexandrea Elle Johnson
# Date: 4/21/2025
# Description: Calculatates maximum wind power and actual power based off of 
#   user input
# Input: Radius, Wind Speed, Operating Efficiency, pi, Air Density
# Output: Area, Maximum Power, Actual Power
############################################################################### 


PI = 3.14159265358979323846233832
AIR_DENSITY = 1.2


###############################################################################
# Function: area_calculation
# Description: Blah Blah Blah
# Parameters:
#   radius:float - Blah Blah Blah
# Return values:
#   area - Blah Blah Blah
# Pre-Conditions: PI previously defined 
# Post-Conditions: None
###############################################################################
def area_calculation(radius:float):
    # Solve for area using the formula A=pi*r^2 and the radius input 
    #   given by the user for r
    area = PI * radius ** 2
    rounded_area = round(area, 2) # rounds to two(2) decimal points
    
    # Print area to the print window saying it is in m^2
    print("Your area is", rounded_area, "meters squared.")
    return area


###############################################################################
# Function: max_power_calculation
# Description: Blah Blah Blah
# Parameters: 
#   air_density:float - Blah Blah Blah
#   area:float - Blah Blah Blah
#   wind_speed:float - Blah Blah Blah
# Return values: 
#   max_pow_kw - Blah Blah Blah
# Pre-Conditions: None
# Post-Conditions: None
###############################################################################
def max_power_calculation(air_density:float, area:float, wind_speed:float):
    # Solving maximum power using: Pmax= 0.5 * p * A * v ^ 3 with 
    #   Pmax= 0.5 * density_of_air * area * air_speed_cubed
    max_pow_j = 0.5 * air_density * area * wind_speed ** 3
    max_pow_kw = max_pow_j / 1000 #conversion from J to kW
    rounded_max_pow_kw = round(max_pow_kw, 2) # rounds to two(2) decimal points
    
    # Print the rounded maximum power to the print window saying it is in kW
    print("Your maximum power is", rounded_max_pow_kw, "kW.")
    return max_pow_kw


###############################################################################
# Function: actual_power_calculation
# Description: Blah Blah Blah
# Parameters: 
#   max_pow_kw:float - Blah Blah Blah
#   operating_efficiency_decimal:float - Blah Blah Blah
# Return values: 
#   act_pow_kw - Blah Blah Blah
# Pre-Conditions: None
# Post-Conditions: None
###############################################################################
def actual_power_calculation(
        max_pow_kw:float, 
        operating_efficiency_decimal:float):
    # Multiply the maximum power by the decimal version of the operating 
    #   efficiency to find actual power
    act_pow_kw = max_pow_kw * operating_efficiency_decimal
    rounded_act_pow_kw = round(act_pow_kw, 2) # rounds to two(2) decimal points
    
    # Print the rounded actual power to the print window saying it is in kW
    print("Your actual power is", rounded_act_pow_kw, "kW.")
    return act_pow_kw

###############################################################################
# Function: get_f
# Description: Get a positive float input
# Parameters:
#   promt:str - String to output to get user to input a number
# Return values:
#   value:float - value the user input
# Pre-Conditions: None
# Post-Conditions: None
###############################################################################
def get_f(prompt:str):
    while True:
        try:
            value = abs(float(input(prompt)))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


###############################################################################
# Function: main
# Description: Blah Blah Blah
# Parameters: None
# Return values: None
# Pre-Conditions: AIR_DENSITY predefined
# Post-Conditions: None
###############################################################################
def main():
    radius = get_f("What is the radius of your wind turbine in meters? ")
    print(
        "Thank you the computer has interpreted your input as:", 
        radius, 
        "meters")
    
    wind_speed = get_f("What is the wind speed of air around your wind turbine in meters per second? ")
    print(
        "Thank you the computer has interpreted your input as:", 
        wind_speed, 
        "meters per second")
    
    operating_efficiency = get_f("What is the operating efficiency of your wind turbine as a percentage? ")
    print(
        "Thank you the computer has interpreted your input as:", 
        operating_efficiency, 
        "percent")
    
    # Convert the operating efficiency to a decimal by dividing by 100
    operating_efficiency_decimal = operating_efficiency / 100
    print(
        "For calculation purposes the program has turned your percentage into the decimal:", 
        operating_efficiency_decimal)
    
    area = area_calculation(radius)
    
    max_pow_kw = max_power_calculation(AIR_DENSITY, area, wind_speed)
    
    act_pow_kw = actual_power_calculation(max_pow_kw, 
                                          operating_efficiency_decimal)
    

if __name__ == "__main__": #good formatting for main call
    #calling the main function to run all code
    main()
