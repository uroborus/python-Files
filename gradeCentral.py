#Grade Central simple app Udemy Python course

from statistics import mean as m

admins = {'Python':'Pass123@'}

studentDict = {'Jeff':[78,88,93],
               'Alex[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Ading grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student Does not exist.')

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in studentDict:
        print('removing student ')
        del studentDict[nameToRemove]

def studentAVG():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent, 'has an average grade of:', avgGrade)

def main():
 print("""
 Welcome to Grade Central

 Choose an Option
 [1] - Enter Grades
 [2] - Remove Student
 [3] - Student Average Grades
 [4] - Exit
 """)
 action = input('What would you like to do today? (Enter a Number) ')

if action == '1':
    enterGrades()
elif action == '2':
    removeStudent()
elif action == '3':
    studentAVG()
elif action == '4':
    exit()
else:
    print ('no valid choice was given, try again')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] = passw:
        print('Welcome,',login)
        while True:
            main()
        else:
            print('Invalid Password')
else:
    print('Invalid Username.')

while True"
    main()
