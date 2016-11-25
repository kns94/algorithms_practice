class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True 

        opposite = {'}': '{', ']': '[', ')': '(', '[': -1, '{': -1, '(': -1}

        stack = []
        top = None

        for i in range(len(s)):
            if not top:
                top = s[i]
                stack.append(s[i])
            else:
                if opposite[s[i]] == top:
                    stack.pop()
                    if len(stack) != 0:
                        top = stack.pop()
                        stack.append(top)
                    else:
                        top = None
                else:
                    stack.append(s[i])
                    top = s[i]

        if len(stack) == 0:
            return True
        else:
            return False

print Solution().isValid('([])')