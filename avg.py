def calculateAverage(param1, param2, param3, param4):
    total = param1 + param2 + param3 + param4
    #divide by floating point value to ensure we get the proper potentially fractional answer
    average = total / 4.0
    #print 'Average value is:', average
    return average # hand answer back to caller

average1 = calculateAverage(2, 3, 4, 5)
average2 = calculateAverage(-3, 5.2, 15, 1000.8)
average3 = calculateAverage(1.4, -2.5, 14.3, 200.5)
print 'The three averages are:', average1, average2, average3
