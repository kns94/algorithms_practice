# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class expressionParse:
        
    def turnSimple(self, string):
        """
        Convert string to simple format i.e removing the first bracket
        """

        #print string
    
        if len(string) == 0:
            return ''
           
        count = 1

        #Remove opening bracket and closing, if found
        if string[0] == '(' and string[-1] == ')':
            i = 1
            while i < len(string):
                if string[i] == ')' and count == 1 and i != len(string) - 1:
                    arr = map(str, string)
                    del arr[i]
                    del arr[0]
                    string = "".join(arr)
                    break
                elif string[i] == '(':
                    count += 1
                elif string[i] == ')':
                    count -= 1
                    if i == len(string) - 1:
                        #return '(' + self.turnSimple(string[1 : -1]) + ')'
                        return self.turnSimple(string[1 : -1])
                    #pass 

                i += 1
        
        #print '-' + string

        l = 0
        r = len(string) - 1

        while string[l] != '(' and l < r:
            l += 1


        while string[r] != ')' and r > l:
            r -= 1

        if l == r:
            return string

        left_string = string[: l]
        right_string = string[r + 1:]

       
        if l == 0 and r == len(string) - 1:
            return self.turnSimple(string[l: r + 1])
        elif l != 0 and r == len(string) - 1: 
            return left_string + '(' +  self.turnSimple(string[l + 1: r]) + ')' + right_string
        elif l == 0 and r != len(string) - 1:
            return self.turnSimple(string[l + 1: r]) + right_string
        elif l != 0 and r != len(string) - 1:
            return left_string + '(' +  self.turnSimple(string[l + 1: r]) + ')' + right_string
    

        #return left_string + self.turnSimple(string[l + 1: r]) + right_string
            
    def reverse(self, string):
        """
        Reverse the string and reverse the curve brackets
        """
        string = string[: : -1]
        new = ''
        
        for i in range(len(string)):
            #If opening bracket found, replace it with closing one
            if string[i] == '(':
                new  += ')'  
            #If closing bracket found, replace with opening bracket
            elif string[i] == ')':
                new += '('
            #Copy elements otherwise
            else:
                new += string[i]

        return new
                       
    def processString(self, line):
        """
        Function to process input string
        """

        #print line  

        #Splitting input line by /
        tokens = line.strip().split('/')
        #Input string is the first half before /
        string = tokens[0]
        #Removing white spaces
        string = "".join(string.split())
        #Operations to perform
        operation = tokens[1]
                              
        #If no operations to perform, return string as is
        if len(operation) == 0:
            return str(string)
        
        #If length of string is 1, return as is
        if len(string) == 1:
            return str(string)
       
        #performing operations one by one
        output = string
        for opr in operation:
            if opr == 'S':
                #If operation is Simple
                output = self.turnSimple(output)
                #print output
                       
            if opr == 'R':
                #If operation is reverse
                output = self.reverse(output)
                #print output

        return output

#Input is parsed via standard input
print expressionParse().processString("(AB)C(D((E)FG)H)/S")
print expressionParse().processString("((12)3)4(((5)67)8)/S") 
print expressionParse().processString("(12)3((45)6)/S") 
#(AB)C(D((E)FG)H)
#(12)3((45)6)