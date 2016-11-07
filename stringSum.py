'''
Sum of string without converting whole string to integer
'''

class Solution(object):

    def addZeros(self, string, smaller, greater):

        i = smaller
        while i < greater:
            string += '0'
            i += 1 

        return string

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        length1 = len(num1)
        length2 = len(num2)

        arr1 = [0] * 5099
        arr2 = [0] * 5099

        if length1 == 1 and length2 == 1:
            return str(int(num1) + int(num2))

        for i in range(length2 - 1, -1, -1):
            arr2[length2 - i - 1] = int(num2[i])

        for i in range(length1 - 1, -1, -1):
            arr1[length1 - i - 1] = int(num1[i])

        carry = 0
        result = ''

        for i in range(0, max(length2, length1)):
            current = arr1[i] + arr2[i] + carry

            if current >= 10:
                carry = 1
                current = current % 10
            else:
                carry = 0

            result += str(current)

        result += str(carry)
        return str(int(result [::-1]))

if __name__ == "__main__":
    import sys
    print Solution().addStrings(sys.argv[1], sys.argv[2])