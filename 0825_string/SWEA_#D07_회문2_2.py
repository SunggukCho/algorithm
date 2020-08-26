import sys
sys.stdin = open('palindrome2.txt', 'r')

def palindrome(char):
    char = char
    char_rev = char[::-1]
    if char == char_rev:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, 10+1):
    N = int(input())
    arr = [str(input()) for _ in range(100)]
    M = 100

    result = []
    for i in range(M):
        for j in range(M):
