rate = 10.00
totalHours = 45
regularHours = 40
overTimeHours = totalHours - regularHours
pay = (rate * regularHours) + ((rate * 1.5) * overTimeHours)
print 'For working', totalHours, 'hours, I should be paid', pay
