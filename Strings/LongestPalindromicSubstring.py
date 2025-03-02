def longest_palindromic_string(s):
    if not s:
        return ""
    res = ""

    # method to find longest palindrome around the center
    def check_palindrome(s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    for i in range(len(s)):
        even = check_palindrome(s, i, i + 1)
        odd = check_palindrome(s, i, i)

        if len(odd) > len(res):
            res = odd
        if len(even) > len(res):
            res = even
    return res


s = "manageganktok"
print(longest_palindromic_string(s))
