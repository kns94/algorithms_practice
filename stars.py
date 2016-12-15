# Complete the function below.

import sys

def  StairCase(n):

    num_stars = 1
    spaces = n - num_stars 
    
    for i in range(n):
        for j in range(spaces): 
            sys.stdout.write(' ')

        for j in range(num_stars):
            sys.stdout.write('#')

        num_stars += 1
        spaces = n - num_stars
        print ''

StairCase(6)