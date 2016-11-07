class Solution(object):

    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapper = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}


        if num in mapper:
            return mapper[num]

        neg = False
        if num < 0:
            neg = True
            num *= -1
            new_num = 0

            if num < 15:
                new_num = 15 - num

            else:
                while num > 0:
                    last = num % 10
                    last = 15 - last
                    new_num = new_num * 10 + last
                    num /= 10

            new_num += 1
            num = new_num

        print num
        hexa = ''
  
        while num != 0:
            remainder = num % 16
            num = (num - remainder)/16
            hexa += mapper[remainder]

        if neg:
            for i in range(len(hexa), 8):
                hexa += 'f'
        
        return hexa[::-1]
        

if __name__ == "__main__":
    import sys
    print Solution().toHex(int(sys.argv[1]))