class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        divisor = 2
        dividend = n
        reverse = 0
        bit = 31

        while dividend > 0:
            mod = dividend % divisor 
            #everse += str(mod)
            reverse += (mod * pow(2,bit))
            bit -= 1
            dividend /= divisor

        return reverse

print Solution().reverseBits(5)