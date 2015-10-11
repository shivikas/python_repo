#Exercise 6.5
from __builtin__ import True

s = raw_input('Enter a string')
print s

w = raw_input('Enter Second string for comparison:')
print w

for i,x in enumerate(s):
    print i,x

for i in s:
    print i

y = -1    
while y >= -len(s):
    print s[y]
    y -=1
    

#d = (s == w)
#print d

def cmpString(u,v):
    if len(u) == len(v):
        i =0
        while i < len(u):
            if u[i] == v[i]:
                i +=1
            else:
                print 'Unequal string'
                return False
        
        return True
    else:
        return False
    

def palindrome(u):
    k = 0
    while k < len(u)/2:
        if u[k] == u[-(k+1)]:
            k +=1
        else:
            return False
    return True
            
    
def makePalindrome(u):
    print u
    y = -1
    str = ""
    while y >= -len(u):
        str += u[y]
        y -=1
    print str
    return u + str
    
        
d = cmpString(s.lower(),w.lower())
print d 
if palindrome(s) == True:
    print '{0} string is a palindrome'.format(s)
else:
    print '{0} string is not a palindrome'.format(s)

print makePalindrome(s)
