class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            resultant = target -x
            if resultant in hashmap:
                return [hashmap[resultant],i]
            hashmap[x] = i
        return []