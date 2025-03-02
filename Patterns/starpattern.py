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


def pattern7(n):
    """
    * * * * *
    *       *
    *       *
    *       *
    * * * * *
    """
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def pattern8(n):
    """
    * * * * *
    * *   * *
    *   *   *
    * *   * *
    * * * * *
    """
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


n = 5
pattern8(n)
