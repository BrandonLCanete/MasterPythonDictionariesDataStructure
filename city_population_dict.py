# City one population
city_one_population = {
    "city_name" : "Manila",
    "city_population" : 1600000
}
# City two population 
city_two_population = {
    "city_name" : "Caloocan",
    "city_population" : 1500000
}
# City three population
city_three_population = {
    "city_name" : "Quezon",
    "city_population" : 2761720
}
# City four population
city_four_population = {
    "city_name" : "Davao",
    "city_population" : 1212504
}
# City five population
city_five_population = {
    "city_name" : "Cebu",
    "city_population" : 798634
}
# City six population
city_six_population = {
    "city_name" : "Taguig",
    "city_population" : 644473
}
# City seven population
city_seven_population = {
    "city_name" : "Pasig",
    "city_population" : 617301
}
# City eight population
city_eight_population = {
    "city_name" : "Makati",
    "city_population" : 510383
}
# City nine population
city_nine_population = {
    "city_name" : "General Santos",
    "city_population" : 679588
}
# City ten population
city_ten_population = {
    "city_name" : "Legazpi",
    "city_population" : 179481
}

# City populations dictionaries
city_populations = [city_one_population,city_two_population,city_three_population,city_four_population,city_five_population,city_six_population,city_seven_population,city_eight_population,city_nine_population,city_ten_population]

# Loop to get the data dictionaries
for cities in city_populations:
    # Print the entire dictionaries
    print(f"City Name: {cities.get('city_name')}, City Population: {cities.get('city_population')}")

# Access the population of the 6th city
sixth = city_populations[5]['city_population']
# Print the population of the 6th city
print(f"The population of sixth city is : {sixth}")

# Update the population of the 3rd city
third = city_populations[2]['city_population'] = 2800000
# Print the updated population of 3rd city
print(f"The updated population of third city is : {third}")

# Delete the 9th city from the dictionary
del city_populations[8]
# Print the city populations dictionaries
print(f"The updated cities after nineth city deleted are : {city_populations}")

# Get the last key-value pair
last = city_populations[8]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")