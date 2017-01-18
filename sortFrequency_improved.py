class Solution(object):

    def prepareDict(self, arr):

        current = arr[0]
        current_count = 1
        wc = {}

        for i in range(1, len(arr)):
            #print arr[i], current, current_count
            if arr[i] != current:
                wc.setdefault(current_count, [])
                wc[current_count].append(current)

                current = arr[i]
                current_count = 1
            else:
                current_count += 1

        wc.setdefault(current_count, [])
        wc[current_count].append(current)

        return wc

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0:
            return ''

        sorted_string = sorted(s)
        wc = self.prepareDict(sorted_string)
        
        sorted_count = sorted(wc.items(), key = lambda x : (x[0]), reverse = True)
        output = ''
        for item in sorted_count:
            for chars in item[1]:
                output += chars*item[0]

        return output

print Solution().frequencySort('tree')

