# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    time complexity: O(n)
    """
    s = s.lower()
    # throw out all non-alphanumeric characters
    s = ''.join([c for c in s if c.isalnum()])
    # check if the string is a palindrome
    return s == s[::-1]
