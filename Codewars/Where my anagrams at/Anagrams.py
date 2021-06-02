def anagrams(word, words):
    # Use list comprehension with if condition to find anagram
    # sorted() will arrange a string
    return [eachWord for eachWord in words if sorted(word) == sorted(eachWord)]