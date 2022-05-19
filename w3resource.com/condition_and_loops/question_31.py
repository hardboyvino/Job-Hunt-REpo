# Problem Statement - Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

age = int(input("Input a dog's age in human years: ").strip())

if age < 0:
    print("Please try again!")

elif age <= 2:
    print(f"The dog's age in dog's years is {age * 10.5:.0f}")

elif age > 2:
    print(f"The dog's age in dog's years is {((2 * 10.5) + ((age - 2) * 4)):.0f}")
