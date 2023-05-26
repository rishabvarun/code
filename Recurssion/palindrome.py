def palindrome(string, start, end):
    if start >= end:
        return True
    return string[start] == string[end] and palindrome(string, start + 1, end - 1)

s = "abba"
print(palindrome(s, 0, len(s) - 1))