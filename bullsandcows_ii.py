class Solution(object):
    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        

        if len(guess) == 0:
            return ''

        already = []
        both = 0
        a = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1

        for i in range(10):
            both += min(secret.count(str(i)), guess.count(str(i)))

        b = both - a
        return "{}{}{}{}".format(a,"A",b,"B")

secret = '1122'
guess = '2211'
print Solution().getHint(secret, guess)