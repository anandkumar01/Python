def group_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_key = "".join(sorted(word))
        if sorted_key in anagrams:
            anagrams[sorted_key].append(word)
        else:
            anagrams[sorted_key] = [word]
    return list(anagrams.values())


words = ["tan", "nat", "eat", "tea", "ate", "and"]
print(group_anagrams(words))