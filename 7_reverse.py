class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        rx = 0
        while y / 10:
            rx = rx * 10 + y % 10
            y = y // 10

        if x < 0:
            rx = rx * -1
        if rx < -2 ** 31 or rx > 2 ** 31 - 1:
            return 0
        else:
            return rx


solution = Solution()
print(solution.reverse(123))
print(abs(2 ** 31))
