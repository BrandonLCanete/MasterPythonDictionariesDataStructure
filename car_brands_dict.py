# Car one brand
car_one_brand = {
    "car_brand" : "BMW",
    "car_country_origin" : "Germany"
}
# Car two brand
car_two_brand = {
    "car_brand" : "Audi",
    "car_country_origin" : "Germany"
}
# Car three brand
car_three_brand = {
    "car_brand" : "Mercedes-Benz",
    "car_country_origin" : "Germany"
}
# Car four brand
car_four_brand = {
    "car_brand" : "Rolls Royce",
    "car_country_origin" : "United Kingdom"
}
# Car five brand
car_five_brand = {
    "car_brand" : "Toyota",
    "car_country_origin" : "Japan"
}
# Car six brand
car_six_brand = {
    "car_brand" : "Volvo",
    "car_country_origin" : "Sweden"
}
# Car seven brand
car_seven_brand = {
    "car_brand" : "Lamborghini",
    "car_country_origin" : "Italy"
}
# Car eight brand
car_eight_brand = {
    "car_brand" : "Volkswagen",
    "car_country_origin" : "Germany"
}
# Car nine brand
car_nine_brand = {
    "car_brand" : "Ford",
    "car_country_origin" : "USA"
}
# Car ten brand
car_ten_brand = {
    "car_brand" : "Innoson",
    "car_country_origin" : "Nigeria"
}

# Car brands dictionaries
car_brands = [car_one_brand,car_two_brand,car_three_brand,car_four_brand,car_five_brand,car_six_brand,car_seven_brand,car_eight_brand,car_nine_brand,car_ten_brand]

# Loop to get the data dictionaries
for cars in car_brands:
    # Print the entire dictionaries
    print(f"Car Brand: {cars.get('car_brand')}, Car Country Origin: {cars.get('car_country_origin')}")

# Access the country of origin of the 3rd car brand
third = car_brands[2]['car_country_origin']
# Print the country of origin of the 3rd car brand
print(f"The country origin of the third car brand is : {third}")

# Update the country of origin of the 7th car brand
seven = car_brands[6]['car_country_origin'] = "Rome, Italy"
# Print the updated country of origin of the 7th car brand
print(f"The updated country of origin of the seventh car brand is : {seven}")

# Delete the 8th car brand from the dictionary
del car_brands[7]
# Print the car brands dictionaries
print(f"The updated car brands after eight car brand deleted are : {car_brands}")

# Get the last key-value pair in the dictionary
last = car_brands[8]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")