class Solution(object):

    def calculateDigit(self, val1, val2, carry):
        total = val1 + val2 + carry
        if total == 3:
            return 1,1

        if total == 2:
            return 0,1

        if total == 1:
            return 1,0

        if total == 0:
            return 0, 0

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a) == 0 and len(b) == 0:
            return 0

        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a

        diff = len(a) - len(b)

        if diff < 0:
            diff = abs(diff)
            for i in range(diff):
                a = '0' + a 
        else:
            for i in range(diff):
                b = '0' + b

        carry = 0
        add = ''
        for i in range(len(a) - 1, -1, -1):

            total, carry = self.calculateDigit(int(a[i]), int(b[i]), carry) 
            add = str(total) + add 
            carry = int(carry)

        if carry == 0:
            return add 
        else:
            return '1'+add

print Solution().addBinary('1111', '110')