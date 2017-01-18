class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        wc = {}

        for num in nums:
            wc.setdefault(num, 0)
            wc[num] += 1

        return [i[0] for i in sorted(wc.items(), key = lambda x: x[1], reverse = True)[:k]]
        
if __name__ == "__main__":
    print Solution().topKFrequent([1,2,2,3,3], 2)