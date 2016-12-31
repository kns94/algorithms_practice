class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        '''
        . signifies any single element
        * signifies zero or more elements of the preceeding value
        '''

        i = 0 #Pointer for string
        j = 0 #Pointer for pattern
        prev = None

        while i < len(s):

            if p[j] == '.':
                '''
                Checking for single element
                '''
                if i == len(s) - 1 and j == len(p) - 1:
                    break
                elif :

                else:
                    i += 1
                    j += 1


            """
            elif p[j] == '*':
                '''
                Zero or more instances of previous element
                '''
                if not previous:
                    return False
                else:
                    if i < len(s) - 1:
                        i += 1
                    elif s[len(s) - 1] == prev and j == len(p) - 1:
                        break
                    else:
                        return False 

                    while s[i + 1] == previous and i < len(s) - 1:
                        i += 1
                    if j < len(p):
                        j += 1
                    elif i == len(s) - 1:
                        break
                    else:
                        return False
            """
            else:
                '''
                Matching both characters
                '''
                if s[i] == p[j]:
                    previous = s[i]
                    if j < len(p) and i < len(s):
                        j += 1
                        i += 1
                    elif i == len(s) - 1 and j == len(p) - 1:
                        break
                    else:
                        return False
                else:
                    return False
        return True