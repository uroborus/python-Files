mustGet = 'paper plates'
mustAlsoGet = 'chocolate candy bars'


def separateRuns():
    print '###############'
    print   #blank line

def getGroceries(item1, item2, item3, item4): #uses one parameter variable
    print item1 #prints the contents of item1 var
    print item2
    print item3
    print item4
    #print #blank line
    separateRuns()

getGroceries('eggs','soap','lettuce','cat food')
getGroceries('beer','milk','soda','peas')
getGroceries(mustGet, mustAlsoGet, 'lettuce', 'cat food')
