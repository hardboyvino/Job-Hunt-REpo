""" Problem Statement - Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010 """

# The original list of binary data
binary_data = ["0100", "0011", "1010", "1001", "1100", "1001", "1010"]

remainder_5 = []

# For each number in the data
for number in binary_data:
    # Convert it to from base 2 to base 10 and divide by 5, if there is no remainder append to remainder_5 list
    if (int(number, base=2)) % 5 == 0:
        remainder_5.append(number)

# Print the list to see the numbers in binary divisible by 5
for num in remainder_5:
    print(num)
