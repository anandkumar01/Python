# Longest substring without repeating characters

def longest_unique_characters(s):
    if not s:
        return ""
    visited = set()
    res = ""
    max_len = 0
    start = 0
    max_start = 0
    for end in range(len(s)):

        while s[end] in visited:
            visited.remove(s[start])
            start += 1
        visited.add(s[end])

        # Update max_len and max_start if longer unique substring found
        if (end - start + 1) > max_len:
            max_len = end - start + 1
            max_start = start
    return s[max_start : max_start + max_len]


s = "shstarhra"
print(longest_unique_characters(s))
