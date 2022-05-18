# Problem Statement - Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

# Empty list to store the numbers gotten
number_list = []

# Between range of 100 and 401 (so as to include 400)
for number in range(100, 401):

    # If number[0], number[1], number[2] are even
    if (
        int(str(number)[:1]) % 2 == 0
        and int(str(number)[1:2]) % 2 == 0
        and int(str(number)[2:]) % 2 == 0
    ):

        # Add to a list but turn back to string before appending so as to be able to use "join" later on
        number_list.append(str(number))

print(",".join(number_list))
print(len(number_list))
