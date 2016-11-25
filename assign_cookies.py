class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        """
        greed = {}

        for gluttony in g:
            try:
                greed[gluttony] += 1
            except KeyError:
                greed[gluttony] = 1

        size = {}

        for calories in s:
            try:
                size[calories] += 1
            except KeyError:
                size[calories] = 1

        """

        greed = sorted(g, reverse = True)
        size = sorted(s, reverse = True)

        s = 0
        g = 0
        children_satisfied = 0

        while s < len(size) and g < len(greed):
            if size[s] >= greed[g]:
                children_satisfied += 1
                s += 1
            g += 1

        return children_satisfied

print Solution().findContentChildren([6, 5, 3, 2, 1, 1], [5, 2])
