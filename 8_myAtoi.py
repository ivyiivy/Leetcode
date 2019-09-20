#  List 一定要考虑越界问题！！


class Solution:
    def myAtoi(self, str: str) -> int:
        if str =='':
            return 0
        i = 0
        while str[i] == ' ':
            i += 1
            if i >= len(str):
                return 0

        str1 = str[i:]

        num = 0
        i = 0

        if str1[i] == '-' or str1[i] == '+':
            j = i
            i += 1
            while '9' >= str1[i] >= '0':
                num = num * 10 + int(str1[i])
                i += 1
                if i >= len(str1):
                    break

            if str1[j] == '-':
                num = num * -1
        elif '9' >= str1[i] >= '0':
            while '9' >= str1[i] >= '0':
                num = num * 10 + int(str1[i])
                i += 1
                if i >= len(str1):
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
print(solution.myAtoi('-91283472332'))

