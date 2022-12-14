# https://leetcode.com/problems/decode-ways/discuss/2404701/Python-Easy-Solution-(memory-beats-99)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2] != '0' and eval(s[i - 2] + s[i - 1]) < 27:
                dp[i] += dp[i - 2]
        return dp[len(s)]


if __name__ == '__main__':
    print(Solution().numDecodings('1123'))
