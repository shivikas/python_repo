#!usr/bin/env python

import string
import keyword

alphas = string.letters+'_'
nums = string.digits

myInput = raw_input('enter the Identifier to test:')

print myInput

if len(myInput) >= 1:
    
    if myInput[0] not in alphas:
        print 'invalid ID. First symbol should be alphabet'
    else:
        for otherchar in myInput[1:]:
            if otherchar not in alphas+nums:
                print 'Invalid other character.Must be alphanumeric'
                break
        else:
            print 'okay as an identifier'
                
if myInput not in keyword.kwlist:
    print 'OK'
else:
    print 'Error: Identifier is a Keyword'