class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}

        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                already = hash_map[nums[i]]
                if i - already <= k:
                    return True
                else:
                    hash_map[nums[i]] = i 
        return False