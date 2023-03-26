def comparator(str1, str2):
    # verify arguments type
    if (isinstance(str1, str) and isinstance(str2, str)):
        # logic
        for char in str1:
            if(str2.find(char) == -1):
                return False
        return True 
    return False

# print(comparator("abc", "abcde"))
# print(comparator("abz", "abcde"))
# print(comparator("aaaaaaa", "abcde"))
# print(comparator("ab1", "abcde"))