class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        if len(nums) == 0:
            return 0

        f, s, t = None, None, None

        for num in nums:
            if num > t:
                if num > s:
                    if num > f:
                        t = s
                        s = f 
                        f = num
                    else:
                        if num != f:
                            t = s
                            s = num 
                else:
                    if num != s:
                        t = num 

        print f,s,t

        if t or t == 0:
            return t
        else:
            return f 

print Solution().thirdMax([2,2,3,1,5,5,5,6])
