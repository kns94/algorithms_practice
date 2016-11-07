'''
Adding Number to a LinkedList
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if not digits:
            return None

        if len(digits) == 1:
            if digits[0] != 9:
                digits[0] += 1
                return digits
            else:
                digits[0] = 0
                digits.append(1)
                return digits[::-1]

        rev = digits[::-1]

        carry = 1

        for i in range(0, len(rev)):
            sm = rev[i] + carry
            if sm < 10:
                rev[i] = sm
                carry = 0
                break
            else:
                carry = 1
                digit = sm % 10
                rev[i] = digit

        if carry == 1:
            rev.append(1)

        return rev[::-1]

print(Solution().plusOne([9]))