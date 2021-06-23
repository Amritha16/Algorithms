# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring. 

def lcs(s1, s2):
    dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

print(lcs("abrhaa", "arah"))