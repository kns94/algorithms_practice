class Solution(object):

    def wordCount(self, s):

        wc = {}
        for char in s:
            wc.setdefault(char, 0)
            wc[char] += 1
        return wc

    def modifyDict(self, wc):

        deletion = []

        for key in wc.keys():
            val = wc[key]
            wc.setdefault(val, [])
            wc[val].append(key)
            deletion.append(key)

        for key in deletion:
            del wc[key]

        return wc

    def sortVal(self, wc):

        for key in wc.keys():
            wc[key] = sorted(wc[key])

        return wc

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        wc = self.wordCount(s)
        wc = self.modifyDict(wc)
        wc = self.sortVal(wc)
        sorted_count = sorted(wc.items(), key = lambda x : (x[0]), reverse = True)

        output = ''
        for item in sorted_count:
            for chars in item[1]:
                output += chars*item[0]

        return output

print Solution().frequencySort('Aabb')

