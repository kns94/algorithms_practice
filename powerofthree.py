import sys

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n == 0:
            return False
        
        if n == 1:
            return True
            
        if n < 0:
            return False
        

        if (math.log10(n)/math.log10(3)).is_integer():
            return True
        return False

        #largest = pow(3,20)

        #if largest % n == 0:
        #    return True
        
        #return False

        
if __name__ == "__main__":
    print Solution().isPowerOfThree(int(sys.argv[1]))