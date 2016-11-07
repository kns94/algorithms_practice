class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        first = {}
        
        for num in nums1:
            try:
                first[num] += 1
            except KeyError:
                first[num] = 1

        second = {}

        result = []
        for num in nums2:
            if num not in first:
                continue
            else:
                if num not in second:
                    second[num] = 1
                    result.append(num)
                elif second[num] < first[num]:
                    second[num] += 1
                    result.append(num)

        #result = []
        #for key, value in second.iteritems():
        #    while value > 0:
        #        result.append(key)
        #        value -= 1

        return result
            
if __name__ == "__main__":
    solver = Solution()
    print solver.intersect([1,2,2,1], [2,2])