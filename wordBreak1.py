class Solution(object):

    def seperator(self, s, wordDict, memory):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        if s in wordDict:
            '''
            If the word itself is in dictionary, no need to split
            '''
            return s

        ln = len(s)

        if s in memory:
            '''
            Check if the string is already parsed
            '''
            return memory[s]

        for i in range(1, ln):
            prefix = s[0:i]

            if prefix in wordDict:
                suffix = s[i: ]
                sub_suffix = self.seperator(suffix, wordDict, memory)

                if sub_suffix:
                    return prefix +' ' + sub_suffix

                if sub_suffix == False:
                    memory[sub_suffix] = False
            else:
                memory[prefix] = False
            i += 1

        memory[s] = False
        return bool(None)

    def wordBreak(self,s,wordDict):
        if self.seperator(s, wordDict, {}) != False:
            return True
        else:
            return False


word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#word = "ilikesamsung"
#wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}
print Solution().wordBreak(word, wordDict)