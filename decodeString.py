class Solution(object):

    #3[a]2[bc]
    def bracketAnalyze(self, s, i, num):

        output = ''
        if s[i] == ']':
            pass

        return output

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        output = ''
        num = ''
        alpha = ''
        i = 0

        while i < len(s):
            if s[i] != '[':
                if s[i].isdigit():
                    num += s[i]
                else:
                    output += s[i]
            else:
                i += 1
                while s[i] != ']':
                   alpha += s[i] 
                   i += 1

                num = int(num)
                while num > 0:
                    output += alpha
                    num -= 1
                num = ''
                alpha = ''

            i += 1

        return output


if __name__ == "__main__":
    solver = Solution()
    print solver.decodeString("2[abc]3[cd]ef")