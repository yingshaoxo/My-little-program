class FenwickTree(object):
    def __init__(self, n):
        self.sum_array = [0] * (n + 1)
        self.n = n
 
    def lowbit(self, x):
        return x & -x
 
    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
 
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res
 
 
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        sum_array = [upper, lower - 1]
        total = 0
        for num in nums:
            total += num
            sum_array += [total, total + lower - 1, total + upper]
 
        index = {}
        for i, x in enumerate(sorted(set(sum_array))):
            index[x] = i + 1
 
        tree = FenwickTree(len(index))
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            tree.add(index[total], 1)
            total -= nums[i]
            ans += tree.sum(index[upper + total]) - tree.sum(index[lower + total - 1])
        return ans

example = Solution()
result = example.countRangeSum([-2, 5, -1], -2, 2)
print(result)
