class Solution(object):

    def checkArithmetic(self, arr):
        '''
        Checking if the particular array is an arithmetic progression or not
        '''

        #print arr

        diff = arr[1] - arr[0]                     

        for i in range(1, len(arr) - 1):                
            current_diff = arr[i + 1] - arr[i]
            if current_diff != diff:
                return False
        return True

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        count = 0
        
        for i in range(len(A) - 2):
            if self.checkArithmetic(A[i:i+3]):
                count += 1
                j = i + 4

                while self.checkArithmetic(A[i:j]) == True and j <= len(A):
                    count += 1
                    j += 1

        return count

print Solution().numberOfArithmeticSlices([1,2,3,4,5,6])

