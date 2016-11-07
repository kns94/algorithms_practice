import sys

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) == 0:
            return t

        hash_map = {}
        length = len(s)

        for i in range(0, length/2):
            try:
                hash_map[s[i]] += 1
            except KeyError:
                hash_map[s[i]] = 1 

            j = length - i - 1

            try:
                hash_map[s[j]] += 1
            except KeyError:
                hash_map[s[j]] = 1            

        if length % 2 != 0:
            try:
                hash_map[s[length/2]] += 1
            except KeyError:
                hash_map[s[length/2]] = 1 

        length = length + 1

        for i in range(0, length/2):
            j = length - i - 1

            if t[i] not in hash_map:
                return t[i]
            else:
                if t[j] not in hash_map:
                    return t[j]
                else:
                    if hash_map[t[i]] == 0:
                        return t[i]
                    else:
                        hash_map[t[i]] -= 1

                    if hash_map[t[j]] == 0:
                        return t[j]
                    else:
                        hash_map[t[j]] -= 1 

        print hash_map
        if length % 2 != 0:
            return t[length/2]
        #if t[length/2] not in hash_map:
        #    return t[length/2]
        #else:
        #    if 

if __name__ == "__main__":
    solver = Solution()
    a = "yjvaocttlqmhvclcuyzrufktvrobpuqmheungexdoyiaaliuafhzfwvgnkfesjiuqwudnjwlydamjytzlafwyftlmvobxhjxfqtnoqhkebsortzygdpiqrkcfoausdqxwtqmqqjzjrmnldjhzrvpyvucqsgkntddyaesdjtbpvttulqshibrktqvuevfozstukupyndvuyrwqnmqyestqgvojyoodyviteltyhcpwtydyevhytvsdspritsdheyeblesaintfcsgccxsazunelsnphalzglkbhfzwrtcimaolxzrolumunxrsejzcspwccnwmbvshtrizmvfrldefpzzwvppbpntrsvzkoxiftqhltvemlfkhfzmwqlaxaajbupilmzymcxqrkitiroztjruuiolvldcogattppctbwgldtlwznbqfcsexrnpwyxgipsprfjmpeqdojrbmez"
    b = "cyjylrpegmuahrefocwxurdyrptqtuwhlqafluetwhzfnlbseubuwmrftmldetmwcykfldtezbqczzrbwatniuylxrchoxeekloczkjanyvyvvyjttnylptptvhoxubdvdhyrmhzhykevtqubrqzfrrsydtdttrskjpztydlltlcpcntkczovrqiilsjfotbdlottptxtfaotkbmuamxtmnxcergqymzpeemdqcdvlfzufeqkexzsthnumrcupuqsnzkbjxnnxibpbjszsdhmahazqmwhlplfsdopurixasirzspsvtowsgrgfigfaapldzqvyiicyjsrwsteamucnlqpmzhqqhdosbapnvjvccovjwljgvoofqvwptfussvdurqvgipsvxyvdjibqyyiknewdnjatuwwvurclsoilgvytwzniamjqyielpgaozsmlozintyfehfekpfgqojq"
    print solver.findTheDifference(a, b)