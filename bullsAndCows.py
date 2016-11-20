class Solution(object):

    def getIndex(self, secret, ele):
        pos = []
        for i in range(len(secret)):
            if secret[i] == ele:
                pos.append(i)
        return pos
    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        

        if len(guess) == 0:
            return ''

        already = []
        a = 0
        b = 0

        for i in range(0, len(secret)):
            if secret[i] not in already:
                s_pos = self.getIndex(secret, secret[i])
                g_pos = self.getIndex(guess, secret[i])

                #print s_pos, g_pos

                common = list(set(s_pos).intersection(g_pos))
                #print common
                a += len(common)

                '''
                removing common positions from both the lists
                '''
                s_pos = list(set(s_pos).difference(set(common)))
                g_pos = list(set(g_pos).difference(set(common)))
                #print s_pos, g_pos

                if len(s_pos) <= len(g_pos):
                    b += len(s_pos)
                else:
                    b += len(g_pos) 

                already.append(secret[i])
                #print a, b 
                #print '\n\n'
                #break

        return "{}{}{}{}".format(a,"A",b,"B")

secret = '1123'
guess = '0111'
print Solution().getHint(secret, guess)