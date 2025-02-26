# find sum of digits in a string

def sum_of_digits(s):
    sum = 0
    for ch in s:
        if ch.isdigit():
            sum += int(ch)
    return sum

s = "ank2p80wv71yp"
print(sum_of_digits(s))
