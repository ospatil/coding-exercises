"""
Palindrome check using recursion
i/p: abbcbba, o/p: True
i/p: abba, o/p: True
i/p: geeks, o/p: False
"""


def isPalindromeRec(s, start, end):
    # initially start = 0, end = n - 1
    if start >= end:
        return True
    return s[start] == s[end] and isPalindromeRec(s, start + 1, end - 1)


def test_isPalindromeRec():
    s = "abbcbba"
    assert isPalindromeRec(s, 0, len(s) - 1) is True
    s = "abba"
    assert isPalindromeRec(s, 0, len(s) - 1) is True
    s = "geeks"
    assert isPalindromeRec(s, 0, len(s) - 1) is False
