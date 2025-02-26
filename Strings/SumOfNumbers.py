def sum_of_numbers(s):
    sum = 0
    temp = ""
    for ch in s:
        if ch.isdigit():
            temp += ch
        else:
            if temp:
                sum += int(temp)
                temp = ""
    if temp:
        sum += int(temp)
    return sum


s = "ank13jh9t2d02"
print(sum_of_numbers(s))
