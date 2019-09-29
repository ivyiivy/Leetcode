#  List 一定要考虑越界问题！！
# 可以用str.strip函数去掉左边的空格


class Solution:
    def myAtoi(self, str: str) -> int:
        if str == '':
            return 0
        i = 0
        while str[i] == ' ':
            i += 1
            if i >= len(str):
                return 0

        str = str[i:]

        num = 0
        i = 0

        if str[i] == '-' or str[i] == '+':
            j = i
            i += 1
            if i >= len(str):
                return 0
            while '9' >= str[i] >= '0':
                num = num * 10 + int(str[i])
                i += 1
                if i >= len(str):
                    break

            if str[j] == '-':
                num = num * -1
        elif '9' >= str[i] >= '0':
            while '9' >= str[i] >= '0':
                num = num * 10 + int(str[i])
                i += 1
                if i >= len(str):
                    break
        else:
            return 0
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num


solution = Solution()
print(solution.myAtoi('+'))
