class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set(nums)
        a = len(nums)
        b = len(d)
        if (a>b):
            return True
        else:
            return False