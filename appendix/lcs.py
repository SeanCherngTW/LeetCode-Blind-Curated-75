def lcs(s1: str, s2: str) -> int:
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0 for _ in range(len_s2 + 1)] for _ in range(len_s1 + 1)]
    res = 0
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return res


print(lcs('fosh', 'fish'))
print(lcs('abcdefghijklmnopqrstuvwxyz', 'bcdghixyz'))
