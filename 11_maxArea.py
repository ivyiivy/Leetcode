class Solution:
    def maxArea(self, height) :
        maxarea = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            maxarea = max(maxarea,(j - i) * min(height[i], height[j]))
            if (height[i] <= height[j]):
                i += 1
            else:
                j -= 1
        return maxarea

solution=Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
