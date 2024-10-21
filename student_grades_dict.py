# Student one grade
student_one_grade = {
    "student_name" : "Angeline",
    "student_grade" : 90
}
# Student two grade
student_two_grade = {
    "student_name" : "Arthur",
    "student_grade" : 95
}
# Student three grade
student_three_grade = {
    "student_name" : "Joey",
    "student_grade" : 93
}
# Student four grade
student_four_grade = {
    "student_name" : "Marky",
    "student_grade" : 85
}
# Student five grade
student_five_grade = {
    "student_name" : "Juan",
    "student_grade" : 80
}

# Students grades dictionaries
student_grades = [student_one_grade,student_two_grade,student_three_grade,student_four_grade,student_five_grade]

# Loop to get the data dictionaries
for grades in student_grades:
    # Print the entire dictionaries
    print(f"Student Name: {grades.get('student_name')}, Student Grade: {grades.get('student_grade')}")

# Print the grade of the 3rd student
print(f"The third student grade is : {student_grades[2]['student_grade']}")

# Update the grade of the 2nd student
second_student_grade_update = student_grades[1]['student_grade'] = 100
# Print the updated grade of 2nd student
print(f"The updated grade of second student is : {second_student_grade_update}")

# Delete the entry of the 5th student
del student_grades[4]
# Print the student dictionaries 
print(f"The updated students after student five deleted are : {student_grades}")

# Get the last key-value pair
last = student_grades[3]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")