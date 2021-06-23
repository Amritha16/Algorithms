# Implementation of the fenwick tree or Binary Indexed Tree (BIT).
# Allows for updation, finding range sum query and number of inverse pairs [a[j] > a[i] where i > j]

class Fenwick:
    fenwick = []
    nums = []

    def __init__(self, nums):
        self.nums = nums
        self.fenwick = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.updateHelper(i + 1, nums[i])
    
    def updateHelper(self, index, ele):
        while(index < len(self.fenwick)):
            self.fenwick[index] += ele
            index += index & -(index)
    
    def sumHelper(self, i):
        ans = 0
        while(i > 0):
            ans += self.fenwick[i]
            i -= i & -(i)
        return ans

    def update(self, index, ele):
        self.updateHelper(index + 1, ele - self.nums[index])
        self.nums[index] = ele
    
    def sum(self, i, j):
        return self.sumHelper(j + 1) - self.sumHelper(i)


f = Fenwick([1, 3, 5])
print(f.sum(0, 2))
f.update(1, 2)
print(f.sum(0, 2))

        


    