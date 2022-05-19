# Problem Statement - Write a Python program to get the Fibonacci series between 0 to 50

# The fibonachi has to start with a list containing the 1st 2 elements of the sequence before starting
# fibo = [0, 1]

# for number in range(2, 50):
#     # If the addition of the 2 previous numbers is less than 50 then append the number, else means we have gone too far
#     if ((fibo[number - 1]) + (fibo[number - 2])) < 50:
#         fibo.append(fibo[number - 1] + fibo[number - 2])
#     else:
#         break

# print(fibo)

x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x + y
