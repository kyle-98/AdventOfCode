import math

mass_list = []

with open("input.txt", "r") as input_file:
    for line in input_file:
        mass_list.append(int(line.rstrip()))

def sum_of_fuel(mass_list):
    total_fuel = 0
    for mass in mass_list:
        fuel_requirement = math.floor(mass / 3) - 2
        temp_fuel_requirement = fuel_requirement
        temp_fuel = 0
        while temp_fuel_requirement >= 0:
            temp_fuel_requirement = math.floor(temp_fuel_requirement / 3) - 2
            if temp_fuel_requirement <= 0:
                break
            temp_fuel += temp_fuel_requirement
        total_fuel += temp_fuel + fuel_requirement     
    return total_fuel

print(sum_of_fuel(mass_list))