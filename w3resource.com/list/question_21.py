# Problem Statement - Write a Python program to convert a list of characters into a string.

char_list = ["a", "b", "c"] * 5

# Join all the parts of the list without any space inbetween.
# Join can be a very powerful tool on lists
new_string = "".join(char_list)

print(new_string)