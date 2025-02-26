def is_palindrome(s):
    if not s:
        return ""
    i, j = 0, len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        else:
            i+=1
            j-=1
    return True
s = "madam"
if is_palindrome(s):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")