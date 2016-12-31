from enum import Enum
import sys

class State(Enum):
    Before = 0
    Inside = 1
    Done   = 2

class expressionParse:

    def simplifyInternal(self, string):
        """
        Simplifying internal methods of the type (xy)z to xyz
        """

        prev = string
        current = string

        #print string

        while True:

            prev = current

            #Temperory list of indexes to remove
            remove = []
            start = False
            i = 0

            while i < len(prev):
                #Remove internal bracket
                if not start and prev[i] == '(' and prev[i + 1] != '(':
                    start = True
                    bracket_start = i
                    
                #Once we find closing bracket and if there are elements after the closing bracket - remove both brackets
                elif start and prev[i] == ')' and i != len(prev) - 1 and prev[i + 1] != ')' and prev[i + 1] != '(':
                    remove += [bracket_start, i]
                    break
                    
                i += 1

            #Convert string to array
            arr = map(str, prev)
            removals = 0                #Removals is the count of elements removed, so to shift index accordingly
            for rem in remove:
                del arr[rem - removals] #Delete index
                removals += 1
                
            current = "".join(arr)
            
            #print prev, current

            if prev == current:
                break

        return current
        
    def turnSimple(self, string):
        """
        Convert string to simple format i.e removing the first bracket
        """
           
        #Remove opening bracket, if found
        if string[0] == '(':
            string = string[1:]
        
            #Parse till closing bracket and remove it
            i = 0
            count = 1 

            while i < len(string):

                if string[i] == '(':
                    count += 1

                if string[i] == ')':
                    count -= 1

                if count == 0:
                    break 

                i += 1            
            
            #Removing brackets by slicing string
            string = string[: i] + string[i + 1: ]
            #print string
            
        #Now, simplify internal values of the type (xy)z to xyz
        string = self.simplifyInternal(string)
            
        return string

    def simplify(self, expression):
        levels = [State.Before]
        result = []

        for c in expression:
            if c == '(':
                if levels[-1] == State.Before:
                    levels[-1] = State.Inside
                else:
                    result.append(c)
                levels.append(State.Before)
            elif c == ')':
                levels.pop()
                if levels[-1] == State.Inside:
                    levels[-1] = State.Done
                else:
                    result.append(c)
            else:
                if levels[-1] == State.Before:
                    levels[-1] = State.Done
                result.append(c)

        return ''.join(result)
                
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
                output = self.simplify(output)
                #print output
                       
            if opr == 'R':
                #If operation is reverse
                output = self.reverse(output)
                #print output

        return output

#print expressionParse().processString("((AB)C)/S")

for line in sys.stdin:
    sys.stdout.write(expressionParse().processString(line))
    print ''