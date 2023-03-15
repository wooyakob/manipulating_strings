my_string = "My string is: " + "The quick brown fox jumps over the lazy dog"

# Print my string
print("\n\n")
print(my_string[:])
print("\n\n")

# Negative Indices. Last letter.
print("The last letter of my string is: " , my_string[-1])
print("\n\n")

# String Length
print("The length of my string is: " , len(my_string))
print("\n\n")

# Negative Indices. First letter.
print("The first letter of my string is: " , my_string[-43])
print("\n\n")

# Spell my name using negative indices
print("You can spell my name using negative indices! Here, check this out: ")
print("\n\n")
print(my_string[-23])
print(my_string[-7])
print(my_string[-36])
print(my_string[-2])
print(my_string[-33])
print("\n\n")

# Test out an index
print(my_string[-1:-42])


# What Lessons Did You Learn?
print("Wow, I learned that spaces inside of a string are counted in calculating the which letter is associated with the negative indices!")
print("Wow, I don't think you can create an index of two negative indices, even though -43 is associated with the first letter, and -1 the last letter")