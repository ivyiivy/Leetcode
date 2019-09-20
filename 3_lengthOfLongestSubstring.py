# 暴力求解不通过
# class Solution():
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ans = 1
#         a = [0]
#         equal = False
#         for i in range(len(s)):
#             for j in range(i + 1, len(s)):
#                 for k in range(i, j):
#                     if (s[k] == s[j]):
#                         equal = True
#                 if not equal:
#                     ans += 1
#                 else:
#                     break
#             equal = False
#             a.append(ans)
#             ans = 1
#         return max(a)
#
# solution =Solution()
# a=solution.lengthOfLongestSubstring('')
# print(a)
#
#
#

# 巧妙的贪心算法

class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in c:
                i=max(i,c[s[j]])
            ans=max(ans,j-i+1)
            c[s[j]]=j+1
        return ans

solution=Solution()
print(solution.lengthOfLongestSubstring("abcdgabca"))

