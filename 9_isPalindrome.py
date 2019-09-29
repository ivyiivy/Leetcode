class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            y = 0
            x1 = x
            while x / 10:
                y = y * 10 + x % 10
                x = x // 10
            return x1==y
            # if x1 == y:
            #     return True
            # else:
            #     return False


solution = Solution()
print(solution.isPalindrome(-121))
