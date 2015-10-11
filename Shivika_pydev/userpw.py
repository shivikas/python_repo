import re
import datetime

def isLeapyear(year):
    if (year % 4 == 0 and year % 100 != 0):
        print '{0} is a leap year'.format(year)
        return True
    elif (year % 100 == 0 and year % 400 == 0):
        print '{0} is a leap year'.format(year)
        return True
    else:
        print '{0} is a not a leap year'.format(year)
        return False
 
def checkDateformat(date):
    dateIscorrect = re.match('[0-3][0-9]\/[0-1][0-9]\/[1-2][0-9]{3}',date)
    print dateIscorrect
    return dateIscorrect

def checkDatevalid(date):
    list_str = date.split('/')    
    print list_str
    print 'Date Entered is:', int(list_str[0])
    print 'Month Entered is:', int(list_str[1])
    print 'Year entered is:', int(list_str[2])

    if (list_str[0] == 00 or list_str[1] == 00):
        print 'Date or Month can not be 00. Enter valid Value'
        return False

    if (int(list_str[0]) >= 1 or int(list_str[0]) <= 31):
        if (int(list_str[1]) >= 1 or int(list_str[1]) <= 12):
            if (int(list_str[2]) <= 2100):
                if (int(list_str[0]) == 29 and int(list_str[1]) == 2):
                    if not isLeapyear(int(list_str[2])):
                        print 'date {0} can only be possible in leap year. And {1} is not a leap year'.format(list_str[0], list_str[2])
                        return False
                    
                else:
                    return True

    else:
        return False
        

dateInput = raw_input('Enter date if DD/MM/YYYY format: ').strip()
print dateInput

if (checkDateformat(dateInput)):
    print 'Date entered in correct format'
    if (checkDatevalid(dateInput)):
        print 'Entered Date is Valid'
    else:
        print 'Entered Date is Invalid. Try again!'

else:
    print 'Date is entered in wrong format. Try again!'
    
