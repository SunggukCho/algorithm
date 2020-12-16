word = input()

def palindrome(word):
    if len(word) < 2:
        return 1
    if word[0] != word[-1]:
        return 0
    return palindrome(word[1:-1])

result = palindrome(word)
print(result)