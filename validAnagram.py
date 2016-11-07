import sys

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == t:
            return True

        if len(s) != len(t):
            return False

        one = map(str, s)
        two = map(str, t)

        s_count = {k:one.count(k) for k in set(one)}
        #for o in one:
        #    if o not in s_count:
        #        s_count[o] = 0
        #    else:
        #        s_count[o] += 1

        #t_count = {}
        t_count = {k:two.count(k) for k in set(two)}
        #for t in two:
        #    if t not in t_count:
        #        t_count[t] = 0
        #    else:
        #        t_count[t] += 1

        for k, v in s_count.iteritems():
            if k not in t_count:
                return False

            if s_count[k] != t_count[k]:
                return False

        return True

        #shared_items = set(s_count.items()) & set(t_count.items())
        #if len(shared_items) == len(s_count.keys()):
        #    return True
        #else:
        #    return False

if __name__ == '__main__':
    ana = Solution()
    print ana.isAnagram(sys.argv[1], sys.argv[2])