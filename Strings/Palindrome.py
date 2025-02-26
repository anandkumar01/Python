def is_palindrome(s):
    n = len(s)
    if not n:
        return ""
    i, j = 0, n-1
    while i<j:
        if s[i] != s[j]:
            return False
        else:
            i+=1
            j-=1
    return True
s = "anagana"
if is_palindrome(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")