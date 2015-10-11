
listOfNum = [45,3,67,1,55,37,98,6,16]
listOfNum.sort()
listOfNum.reverse()
print listOfNum

stringValue = ['ab','cat','bat','roadie','snapdeal', 'rise','appear', 'zebra']
stringValue.sort()
stringValue.reverse()
print stringValue

#Exercise 6.4

def getScore():
    scores = raw_input('Enter list of score seperated by comma').strip()
    print scores
    listScores = [int(s) for s in scores.split(',')]
    print listScores
    return listScores
    
def getAvg(score):
    avgScore = sum(score)/float(len(score))
    return avgScore 

def getGrade(testScore):
    for x in testScore:
        print x
        if x >= 90 and x <= 100:
            print 'The grade of student with test score {0} is A'.format(x)
    
        elif x >= 80 and x <= 89:
            print 'The grade of student with test score {0} is B'.format(x)
    
        elif x >= 70 and x <= 79:
            print 'The grade of student with test score {0} is C'.format(x)
    
        elif x >= 60 and x <= 69:
            print 'The grade of student with test score {0} is D'.format(x)
    
        elif x < 60:
            print 'The grade of student with test score {0} is F'.format(x)
    
        else:
            print 'Test score {0} entered is wrong. Must be between 0 and 100'.format(x)
            break
        
    
score_list = getScore()
print score_list
avg = getAvg(score_list)
print 'Average score of students is :', avg
getGrade(score_list)
