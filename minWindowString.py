class Solution(object):

    def wordCount(self, word):
        wc = {}

        for w in word:
            try:
                wc[w] += 1
            except KeyError:
                wc[w] = 1
        return wc

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) == len(t):
            if self.wordCount(s) == self.wordCount(t):
                return s
            else:
                return ""

        if len(s) < len(t):
            return ""

        if len(t) == 1:
            if t in s:
                return t 
            else:
                return ""


        wc = self.wordCount(t)
        temp = wc.copy()
        is_window = False
        window = []
        window_count = 0
        min_index = [float('-inf'), float('inf')]
        window_start = 0

        i = 0
        while i < len(s):
            print window

            if not is_window:
                if s[i] in temp:
                    window_start = i

                    is_window = True
                    temp[s[i]] -= 1
                    if i not in window:
                        window.append(i) 

                    if temp[s[i]] == 0:
                        del temp[s[i]]

            if window:
                if s[i] in temp:
                    temp[s[i]] -= 1
                    if i not in window:
                        window.append(i)

                    if temp[s[i]] == 0:
                        del temp[s[i]]

            if len(temp.keys()) == 0:

                if (i - window_start) < (min_index[1] - min_index[0]):
                    min_index = [window_start, i]      
                    #print s[min_index[0]:min_index[1] + 1]          

                window_count += 1
                temp = wc.copy()    
                is_window = False
                window_start = window[window_count - 1]
                i = window[window_count - 1]

            i += 1

        if min_index[0] == float('-inf') or min_index[1] == float('inf'):
            return ""

        else:
            return s[min_index[0]: min_index[1] + 1]

print Solution().minWindow("acbbaca", "aba")