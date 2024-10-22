# Programming one language 
programming_one_language = {
    "programming_name" : "Java",
    "programming_creator" : "James Gosling"
}
# Programming two language
programming_two_language = {
    "programming_name" : "C#",
    "programming_creator" : "Anders Hejlsberg"
}
# Programming three language
programming_three_language = {
    "programming_name" : "PHP",
    "programming_creator" : "Rasmus Lerdorf"
}
# Programming four language
programming_four_language = {
    "programming_name" : "Javascript",
    "programming_creator" : "Brendan Eich"
}
# Programming five language
programming_five_language = {
    "programming_name" : "C",
    "programming_creator" : "Dennis MacAlistair Ritchie"
}
# Programming six language
programming_six_language = {
    "programming_name" : "C++",
    "programming_creator" : "Bjarne Stroustrup"
}
# Programming seven language
programming_seven_language = {
    "programming_name" : "Python",
    "programming_creator" : "Guido van Rossum"
}

# Programming languages dictionaries
programming_languages = [programming_one_language,programming_two_language,programming_three_language,programming_four_language,programming_five_language,programming_six_language,programming_seven_language]

# Loop to get the data dictionaries
for programmings in programming_languages:
    # Print the entire dictionaries
    print(f"Programming Name: {programmings.get('programming_name')}, Programming Creator: {programmings.get('programming_creator')}")

# Access the developer of the 4th programming language
fourth = programming_languages[3]['programming_creator']
# Print the developer of the 4th programming language
print(f"The developer or creator of the fourth programming language is : {fourth}")

# Update the developer of the 6th programming language
sixth = programming_languages[5]['programming_creator'] = "Danish Developer Bjarne Stroustrup"
# Print the updated developer or creator of 6th programming language
print(f"The updated developer or creator of sixth programming language is : {sixth}")

# Delete the 2nd programming language from the dictionary
del programming_languages[1]
# Print the programming languages dictionaries
print(f"The updated programming languages after second programming language deleted are : {programming_languages}")

# Get the last key-value pair in the dictionary
last = programming_languages[5]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")