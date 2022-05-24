# Problem Statement - You will be given a list of 32 bit unsigned integers. Flip all the bits (1 -> 0 and 0 -> 1) and return the result as an unsigned integer.

def flipping_bits(n):
    # Convert number to base 2 that is 32 bits long
    n = f"{n:032b}"

    new_bin = []
    # Force the base-2 number to string and Use if statement to turn all the 0 to 1 and vice versa
    for i in str(n):
        if i == "0":
            i = "1"
            new_bin.append(i)
            
        else:
            i = "0"
            new_bin.append(i)
            
    # So far answers stored in list (new_bin) so turn it into 1 long string with join() method
    new_int = "".join(new_bin)

    # Turn the string back to base 2
    return int(new_int, base=2)