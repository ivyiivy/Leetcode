class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def center(s, left, right):
            L = left
            R = right
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1

            return R - L - 1

        maxlen = 0
        start = 0
        end = 0
        if len(s) == 0:
            return ""

        for i in range(len(s)):
            len1 = center(s, i, i)
            len2 = center(s, i, i + 1)
            maxlen = max(len1, len2)
            if maxlen > (end - start + 1):
                start = i - (maxlen - 1) // 2
                end = i + maxlen // 2
        print(s[start:end + 1])

solution=Solution()
solution.longestPalindrome("dfsfkjsdgfdskljg")


