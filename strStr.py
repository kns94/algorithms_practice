class Solution(object):

    '''
    def prefixMatcher(self, string):
        length = len(string)
        mid = length/2
        j, k, ind = mid - 1, length - 1, -1
        prefix = ''
        start = False
        already = []

        while j >= 0 and k >= mid:
            if string[j] == string[k]:
                if not start:
                    start = True
                    ind = j
                prefix = string[j] + prefix
                k -= 1
            else:
                already.append(prefix)
                prefix = ''
                start = False
                ind = -1
            j -= 1

        for sub in already:
            if string[:len(sub)] == sub and len(sub) > 0:
                return sub, len(sub)
                #return sub, len(sub)

        return prefix, ind + 1
    '''

    def buildPrefixArray(self, string):

        temp = [0] * len(string)
        temp[0] = 0
        i = 1
        j = 0

        while i < len(string):
            if string[i] == string[j]:
                temp[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = temp[j - 1]
                else:
                    j = 0
                    i += 1

        return temp

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) == 0:
            return 0
            
        if len(haystack) == 0:
            return -1
        
        i, j, string_count, length = 0, 0, 0, len(needle)
        lps = self.buildPrefixArray(needle)

        while i < len(haystack):
            if haystack[i] == needle[j]:
                
                string_count += 1
                j += 1
                i += 1

                if j == len(needle):
                    return i - j

            elif i < len(haystack):
                #string_count = 0
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1

#haystack = 'abcabcdabxabcdabcdabcy'
#needle = 'abcdabcy'
haystack = "mississippi"
needle = 'issipi'
#haystack = 'abbba'
#needle = 'ba'
#haystack = "ababcaababcaabc"
#needle = "ababcaabc"
print Solution().strStr(haystack, needle)
#print Solution().prefixMatcher('ababcaab')