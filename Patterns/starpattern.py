def pattern1(n):
    """
    *
    **
    ***
    ****
    *****
    """
    for i in range(5):
        print("*" * (i + 1))


def pattern2(n):
    """
    *****
    ****
    ***
    **
    *
    """
    for i in range(n):
        print("*" * (n - i))


def pattern3(n):
    """
        *
       **
      ***
     ****
    *****
    """
    for i in range(n):
        s = n - i - 1
        print(" " * s + "*" * (i + 1))


def pattern4(n):
    """
    *****
     ****
      ***
       **
        *
    """
    for i in range(n):
        print(i * " " + "*" * (n - i))


def pattern5(n):
    """
        *
       ***
      *****
     *******
    *********
    """
    for i in range(n):
        s = n - i - 1
        print(" " * s + "*" * (2 * i + 1))


def pattern6(n):
    """
        *
       ***
      *****
     *******
    *********
    """
    for i in range(n):
        s = i
        print(" " * s + "*" * (2 * (n - i) - 1))


n = 5
pattern6(n)
