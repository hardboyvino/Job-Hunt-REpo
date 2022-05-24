# Problem Statement - Write a Python program to count the number of strings where, the string length is 2 or more and the first and last character are same, from a given list of strings.

sample_list = ["abc", "xyz", "aba", "1221"]

count = 0

for word in sample_list:
    # If the length of the word is 2 or more and the first and last chars are the same
    if len(word) >= 2 and word[0] == word[-1]:
        # Then add to counter
        count += 1

print(count)
