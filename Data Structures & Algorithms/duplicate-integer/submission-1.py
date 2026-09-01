class Solution:
    def hasDuplicate(self, nums):
        visited = set()
        
        for i in nums:
            if i in visited:
                return True

            visited.add(i)

        return False