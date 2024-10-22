# Book one 
book_one = {
    "book_name" : "Clean Code",
    "book_author" : "Robert Cecil Martin"
}
# Book two
book_two = {
    "book_name" : "The Pragmatic Programmer",
    "book_author" : "Dave Thomas"
}
# Book three
book_three = {
    "book_name" : "Code Complete",
    "book_author" : "Steve McConnell"
}
# Book four
book_four = {
    "book_name" : "Refactoring",
    "book_author" : "Kent Beck"
}
# Book five
book_five = {
    "book_name" : "Design Patterns: Elements of Reusable Object-Oriented Software",
    "book_author" : "Erich Gamma"
}
# Book six
book_six = {
    "book_name" : "Introduction to Algorithms",
    "book_author" : "Ronald Rivest"
}
# Book seven
book_seven = {
    "book_name" : "Fermat's Last Theorem",
    "book_author" : "Simon Singh,"
}
# Book eight
book_eight = {
    "book_name" : "Prime Obsession",
    "book_author" : "John Derbyshire"
}
# Book nine
book_nine = {
    "book_name" : "The Man Who Loved Only Numbers",
    "book_author" : "Paul Hoffman"
}
# Book ten
book_ten = {
    "book_name" : "A Beautiful Mind",
    "book_author" : "Sylvia Nasar"
}
# Book eleven
book_eleven = {
    "book_name" : "A History of Pi",
    "book_author" : "Petr Beckmann"
}
# Book twelve
book_twelve = {
    "book_name" : "Linear algebra done right",
    "book_author" : "Sheldon Axler"
}

# Books dictionaries
books = [book_one,book_two,book_three,book_four,book_five,book_six,book_seven,book_eight,book_nine,book_ten,book_eleven,book_twelve]

# Loop to get the data dictionaries
for book in books:
    # Print the entire dictionaries
    print(f"Book Name: {book.get('book_name')}, Book Author: {book.get('book_author')}")

# Access the author of the 9th book
nineth = books[8]['book_author']
# Print the author of the 9th book
print(f"The author of the nineth book is : {nineth}")

# Update the author of the 5th book
fifth = books[4]['book_author'] = "Erich Gamma Swiss computer scientist"
# Print the updated author of the 5th book
print(f"The updated book author of the fifth book is : {fifth}")

# Delete the 3rd book from the dictionary
del books[2]
# Print the books dictionaries
print(f"The updated book after the third book deleted are : {books}")

# Get the last key-value pair in the dictionary
last = books[10]
# Print the last key-value pair in the dictionary
print(f"The last key-value pair in the dictionary after the modifications is : {last}")