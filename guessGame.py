class Solution(object):


    def __init__(self):
        self.already = []

    '''
    def guess(self, n):
        number = 5

        if n == number:
            return 0

        if n < number:
            return 1

        if n > number:
            return -1
    '''

    def guesstimates(self, start, end):

        #if start == end:
        #    return p[start]

        #if p[start:end] == 1:
        #    return p[start]

        #print '\n\n'
        #print start, end
        if start == end:
            return start

        estimate = (start + end)/2

        if estimate in self.already:
            estimate += 1

        self.already.append(estimate)

        #g = self.guess(estimate)
        g = guess(estimate)
        #print estimate, g

        if g == 0:
            return estimate 

        if g == -1:
            return self.guesstimates(start, estimate)

        if g == 1:
            return self.guesstimates(estimate, end)

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.guesstimates(1, n)


print Solution().guessNumber(5)