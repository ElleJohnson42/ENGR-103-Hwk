####################################################################### 
# Program Filename: Assignment2Code.py
# Author:  Alexandrea Elle Johnson
# Date: 4/21/2025
# Description: Calculatates maximum wind power and actual power based off of user input
# Input: Radius, Wind Speed, Operating Efficiency, pi, Air Density
# Output: Area, Maximum Power, Actual Power
####################################################################### 


Pi = float(3.14159265358979323846233832)
AirDensity_p = float(1.2)


def Area_Calculation(Radius:float, Pi:float):
    # Solve for area using the formula A=pi*r^2 and the radius input given by the user for r
    Area = Pi * Radius * Radius
    Rounded_area = round (Area, 2) # rounds to two(2) decimal points
    
    # Print area to the print window saying it is in m^2
    print("Your area is", Rounded_area, "meters squared.")
    return float(Area)


def Max_Power_Calculation(AirDensity_p:float, Area:float, WindSpeed:float):
    # Solving maximum power using: Pmax=0.5*p*A*v^3 with Pmax=0.5*density_of_air*Area*Air_speed_cubed
    MaxPow_J = 0.5 * AirDensity_p * Area * WindSpeed * WindSpeed * WindSpeed
    MaxPow_kW = MaxPow_J / 1000 #conversion from J to kW
    Rounded_MaxPow_kW = round(MaxPow_kW, 2) # rounds to two(2) decimal points
    
    # Print the rounded maximum power to the print window saying it is in kW
    print("Your maximum power is", Rounded_MaxPow_kW, "kW.")
    return float(MaxPow_kW)


def Actual_Power_Calculation(MaxPow_kW:float, OperatingEfficiencyDecimal:float):
    # Multiply the maximum power by the decimal version of the operating efficiency to find actual power
    ActPow_kW = MaxPow_kW * OperatingEfficiencyDecimal
    Rounded_ActPow_kW = round(ActPow_kW, 2) # rounds to two(2) decimal points
    
    # Print the rounded actual power to the print window saying it is in kW
    print("Your actual power is", Rounded_ActPow_kW, "kW.")
    return float(ActPow_kW)


def main():
    Radius = abs(float(input("What is the radius of your wind turbine in meters?")))
    print("Thank you the computer has interpreted your input as:", Radius, "meters")
    
    WindSpeed = abs(float(input("What is the wind speed of air around your wind turbine in meters per second?")))
    print("Thank you the computer has interpreted your input as:", WindSpeed, "meters per second")
    
    OperatingEfficiency = abs(float(input("What is the operating efficiency of your wind turbine as a percentage?")))
    print("Thank you the computer has interpreted your input as:", OperatingEfficiency, "percent")
    
    # Convert the operating efficiency to a decimal by dividing by 100
    OperatingEfficiencyDecimal=OperatingEfficiency/100
    print("For calculation purposes the program has turned your percentage into the decimal:",OperatingEfficiencyDecimal )
    
    Area = Area_Calculation(Radius, Pi)
    
    MaxPow_kW = Max_Power_Calculation(AirDensity_p, Area, WindSpeed)
    
    ActPow_kW = Actual_Power_Calculation(MaxPow_kW, OperatingEfficiencyDecimal)
 
    
if __name__ == "__main__": #good formating for main call
    main() #calling the main function so it runs all the code
