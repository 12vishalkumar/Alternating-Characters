import math
import os
import random
import re
import sys
# Complete the 'alternatingCharacters' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
def alternatingCharacters(s):
    # Write your code here
    i = 1
    c = 0
    s = list(s)
    while(len(s) > i):
        if(s[i-1] == s[i]):
            s.pop(i-1)
            c += 1
        else:
            i += 1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
