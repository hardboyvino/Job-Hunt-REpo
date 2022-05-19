# Problem Statement -  Write a Python program to convert temperatures to and from celsius, fahrenheit.
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


def main():
    temperature = input("Temp: ").strip().upper()
    temp = int(temperature[:-1])
    degrees = temperature[-1:]

    if degrees == "C":
        cel_to_fahr(temp)
    elif degrees == "F":
        fahr_to_cel(temp)
    else:
        raise ValueError


def cel_to_fahr(temp):
    fahr = ((9 * temp) / 5) + 32
    print(f"{temp}C is {fahr:.0f} in Fahrenheit")


def fahr_to_cel(temp):
    cel = (temp - 32) * 5 / 9
    print(f"{temp}F is {cel:.0f} in Celcius")


if __name__ == "__main__":
    main()
