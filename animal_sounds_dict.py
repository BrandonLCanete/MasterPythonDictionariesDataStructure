# Animal one sound
animal_one_sound = {
    "animal_name" : "Dog",
    "animal_sound" : "Bark"
}
# Animal two sound
animal_two_sound = {
    "animal_name" : "Cat",
    "animal_sound" : "Meow"
}
# Animal three sound 
animal_three_sound = {
    "animal_name" : "Cow",
    "animal_sound" : "Moo"
}
# Animal four sound
animal_four_sound = {
    "animal_name" : "Duck",
    "animal_sound" : "Quack"
}
# Animal five sound
animal_five_sound = {
    "animal_name" : "Sheep",
    "animal_sound" : "Baa"
}
# Animal six sound
animal_six_sound = {
    "animal_name" : "Pig",
    "animal_sound" : "Oink"
}
# Animal seven sound
animal_seven_sound = {
    "animal_name" : "Horse",
    "animal_sound" : "Neigh"
}
# Animal eight sound
animal_eight_sound = {
    "animal_name" : "Lion",
    "animal_sound" : "Roar"
}

# Animal sounds dictionaries
animals_sounds = [animal_one_sound,animal_two_sound,animal_three_sound,animal_four_sound,animal_five_sound,animal_six_sound,animal_seven_sound,animal_eight_sound]

# Loop to get the data dictionaries
for animals in animals_sounds:
    # Print the entire dictionaries
    print(f"Animal Name: {animals.get('animal_name')}, Animal Sound: {animals.get('animal_sound')}")

# Access the sound of the 4th animal
fourth = animals_sounds[3]['animal_sound']
# Print the sound of the 4th animal
print(f"The sound of the fourth animal is : {fourth}")

# Update the sound of the 7th animal
seventh = animals_sounds[6]['animal_sound'] = "A Neigh"
# Print the updated sound of 7th animal
print(f"The updated sound of 7th animal is : {seventh}")

# Delete the 5th animal from the dictionary
del animals_sounds[4]
# Print the animal sound dictionaries
print(f"The updated animals after the fifth animal deleted are : {animals_sounds}")

# Get the last key-value pair
last = animals_sounds[6]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")
