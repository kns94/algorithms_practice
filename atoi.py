import sys

class Solution(object):

    def isNumeric(self, ch):

        if ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9':
            return True
        else:
            return False

    def myAtoi(self, str):

        if len(str) == 0:
            return 0

        """
        :type str: str
        :rtype: int
        """
        
        str = str.lstrip()
        number = ''

        if not self.isNumeric(str[0]):
            if len(str) > 1:
                if not self.isNumeric(str[1]):
                    return 0
                else:
                    if str[0] == '+' or str[0] == '-':
                        number += str[0]
                    else:
                        return 0
                else:
                    for i in range(1, len(str)):
                        if not self.isNumeric(str[i]):
                            break
                        number += str[i]        

        else:
            for ch in str:
                if not self.isNumeric(ch):
                    break
                number += ch

        if number == '':
            return 0

        if int(number) > 2147483647:
            return 2147483647

        if int(number) < -2147483648:
            return -2147483648

        return int(number)


if __name__ == "__main__":
    solver = Solution()
    print solver.myAtoi(sys.argv[1])