# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    time complexity: O(n^2)
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ""
    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True
        ans = s[i]
    max_len = 1
    # fill the table in bottom-up fashion
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            # palindrome condition
            if s[start] == s[end]:
                # if it's a two character string or if the remaining string is a palindrome too
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if end - start + 1 > max_len:
                        max_len = end - start + 1
                        ans = s[start:end + 1]
    return ans

# test run
s = "babad"
print(longestPalindrome(s))

# test run
s = "cbbd"
print(longestPalindrome(s))

# test run
s = "thisisnotapalindrome"
print(longestPalindrome(s))
