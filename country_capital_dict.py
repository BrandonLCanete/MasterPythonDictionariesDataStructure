# Country one capital
country_one_capital = {
    "country_name" : "Philippines",
    "country_capital" : "Manila"
} 
# Country two capital
country_two_capital = {
    "country_name" : "Canada",
    "country_capital" : "Ottawa"
}
# Country three capital
country_three_capital = {
    "country_name" : "India",
    "country_capital" : "New Delhi"
}
# Country four capital
country_four_capital = {
    "country_name" : "Japan",
    "country_capital" : "Tokyo"
}
# Country five capital
country_five_capital = {
    "country_name" : "Russia",
    "country_capital" : "Moscow"
}
# Country six capital
country_six_capital = {
    "country_name" : "Germany",
    "country_capital" : "Berlin"
}
# Country seven capital
country_seven_capital = {
    "country_name" : "France",
    "country_capital" : "Paris"
}
# Country eight capital
country_eight_capital = {
    "country_name" : "United Kingdom",
    "country_capital" : "London"
}
# Country nine capital
country_nine_capital = {
    "country_name" : "Italy",
    "country_capital" : "Rome"
}
# Country ten capital
country_ten_capital = {
    "country_name" : "Ukraine",
    "country_capital" : "Kyiv"
}
# Country eleven capital
country_eleven_capital = {
    "country_name" : "Netherlands",
    "country_capital" : "Amsterdam"
}
# Country twelve capital
country_twelve_capital = {
    "country_name" : "Greece",
    "country_capital" : "Athens"
}

# Country capitals dictionaries
country_capitals = [country_one_capital,country_two_capital,country_three_capital,country_four_capital,country_five_capital,country_six_capital,country_seven_capital,country_eight_capital,country_nine_capital,country_ten_capital,country_eleven_capital,country_twelve_capital]

# Loop to get the data dictionaries
for countries in country_capitals:
    # Print the entire dictionaries
    print(f"Country Name: {countries.get('country_name')}, Country Capital: {countries.get('country_capital')}")

# Access the capital of the 5th country
fifth = country_capitals[4]['country_capital']
# Print the capital of the 5th country
print(f"The capital of the fifth country is : {fifth}")

# Update the capital of the 8th country
eight = country_capitals[7]['country_capital'] = "London England"
# Print the updated capital of 8th country
print(f'The updated capital of eight country is : {eight}')

# Delete the 11th country from the dictionary
del country_capitals[10]
# Print the country capitals dictionaries
print(f"The updated country capitals after eleventh country deleted are : {country_capitals}")


# Get the last key-value pair
last = country_capitals[10]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")