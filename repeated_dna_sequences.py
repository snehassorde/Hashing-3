# Time Complexity : O(n*10)
# Space Complexity : O(n)
#Approach 1: using two sets
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        allSubs = set()
        result = set()
        n = len(s)
        for i in range(n-9):
            sub = s[i:i+10]
            if sub in allSubs:
                result.add(sub)
            else:
                allSubs.add(sub)
        
        return result

#Approach 2: Rolling hash
# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        allSubs = set()
        result = set()
        n = len(s)
        maps = {}
        maps['A'] = 1
        maps['C'] = 2
        maps['G'] = 3
        maps['T'] = 4

        hashVal = 0
        kl = int(pow(4, 9))

        for i in range(0, n):
            if(i>=10):
                #out
                out = s[i-10]
                hashVal -= kl * maps[out]
            #in
            inc = s[i]
            hashVal = hashVal*4 + maps[inc]
            if hashVal in allSubs:
                result.add(s[i-9:i+1])
            else:
                allSubs.add(hashVal)
    
        return result