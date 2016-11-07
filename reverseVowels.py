import sys

class Solution(object):

    def isVowel(self, alpha):
        alpha = alpha.lower()

        if alpha == ' ':
            return False

        if alpha == 'a' or alpha == 'e' or alpha == 'o' or alpha == 'u' or alpha == 'i':
            return True
        else:
            return False

    def replace(self, a, b):
        #print a, b
        temp = a
        a = b
        b = temp
        return a, b

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 1:
            return s 

        #if len(s) == 2:
        #    if self.isVowel(s[0]) and self.isVowel(s[1]):
        #        return s[1]+s[0]

        s = " ".join(s.split())

        left_vowel = []
        right_vowel = []
        vowel_counter = 1
        length = len(s)
        temp_string = map(str, s)

        for i in range(0, length/2):
            
            #print left_vowel
            #print right_vowel
            '''
            Adding vowels from both ends and then replacing vowels on similar places
            '''
            if self.isVowel(s[i]):
                left_vowel.append([s[i],i])

            if vowel_counter <= len(left_vowel) and vowel_counter <= len(right_vowel):
                #print left_vowel
                #print right_vowel
                temp_string[left_vowel[vowel_counter - 1][1]], temp_string[right_vowel[vowel_counter - 1][1]] = self.replace(temp_string[left_vowel[vowel_counter - 1][1]], temp_string[right_vowel[vowel_counter - 1][1]])
                vowel_counter += 1

            if self.isVowel(s[length - i -1]):
                right_vowel.append([s[length - i - 1], length - i -1])

            if vowel_counter <= len(left_vowel) and vowel_counter <= len(right_vowel):
                #print left_vowel
                #print right_vowel
                temp_string[left_vowel[vowel_counter - 1][1]], temp_string[right_vowel[vowel_counter - 1][1]] = self.replace(temp_string[left_vowel[vowel_counter - 1][1]], temp_string[right_vowel[vowel_counter - 1][1]])
                vowel_counter += 1

        if length % 2 != 0:
            if self.isVowel(s[length/2]):
                left_vowel.append([temp_string[length/2], length/2])

        #print right_vowel
        #print left_vowel
        #print vowel_counter
        #print temp_string

        '''
        Now checking for imbalance - most likely that would be in the left vowel
        '''
        left_length = len(left_vowel)
        if vowel_counter <= left_length:
            while vowel_counter != left_length:
                temp_string[left_vowel[vowel_counter - 1][1]], temp_string[left_vowel[left_length - vowel_counter][1]] = self.replace(temp_string[left_vowel[left_length - vowel_counter][1]], temp_string[left_vowel[vowel_counter - 1][1]])
                vowel_counter += 1

        '''
        But if all vowels are on right side of the string
        '''
        right_length = len(right_vowel)
        if vowel_counter <= right_length:
            while vowel_counter != right_length:
                temp_string[right_vowel[vowel_counter - 1][1]], temp_string[right_vowel[right_length - vowel_counter][1]] = self.replace(temp_string[right_vowel[right_length - vowel_counter][1]], temp_string[right_vowel[vowel_counter - 1][1]])
                vowel_counter += 1

        return ''.join(temp_string)

if __name__ == "__main__":
    solver = Solution()
    #print solver.reverseVowels(sys.argv[1])
    print solver.reverseVowels("Marge\n let's \"went.\" I await news telegram.")