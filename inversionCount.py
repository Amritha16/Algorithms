# Question 2 find inversion count of array
# Input :
# N
# N elemnts of array
# Example :
# 5
# 8 4 9 2 8
# Output : 
# 5

# This can be solved using BIT or fenwick trees

class Fenwick:

    def __init__(self):
        fenwick = []
        nums = []
    
    def updateHelper(self, index, ele):
        while(index < len(self.fenwick)):
            self.fenwick[index] += ele
            index += index & -(index)
    
    def sum(self, i):
        ans = 0
        while(i > 0):
            ans += self.fenwick[i]
            i -= i & -(i)
        return ans

    def convert(self, nums):
        temp = [0 for _ in range(len(nums))]
        d = {n: i for i, n in enumerate(nums)}
        counter = 1
        for ele in sorted(d.keys()):
            temp[d[ele]] = counter
            counter += 1
        return temp

    def inversion(self, nums):
        self.nums = self.convert(nums)
        self.fenwick = [0 for _ in range(len(nums) + 1)]
        inv = 0
        for i in range(len(self.nums) - 1, -1, -1):
            inv += self.sum(self.nums[i] - 1)
            self.updateHelper(self.nums[i], 1)
        return inv

f = Fenwick()
print(f.inversion([8, 4, 2, 1]))


