def main():
#set count of grades
    readFile()
#readFile reads text file scores.txt and print the name,grade and count of each grade
def readFile():
    name=""
    gradeA=0
    gradeB=0
    gradeC=0
    gradeD=0
    gradeF=0
    avg=0
    print('Name','Average','Grade')
    print("-"*16)
    studFile=open('C:/Users/vpn/Desktop/test/scores.txt','r')
    for line in studFile.readlines():
        val=line.split(",")
        avg=(int(val[1])+int(val[2])+int(val[3]))/3.0
        avg = round(avg, 2)
        grade=getGrade(avg)
        highest_percent = highest_in_the_room(avg)
    #count grades of each letter
        if(grade=='A'):
            gradeA=gradeA+1
        elif(grade=='B'):
            gradeB=gradeB+1
        elif(grade=='C'):
            gradeC=gradeC+1
        elif(grade=='D'):
            gradeD=gradeD+1
        elif(grade=='F'):
            gradeF=gradeF+1
        print(val[0], avg, grade)
        #print grades
    print("="*3,"summary","="*3)
    print('Number of A''s:', gradeA)
    print('Number of B''s:', gradeB)
    print('Number of C''s:', gradeC)
    print('Number of D''s:', gradeD)
    print('Number of F''s:', gradeF)
    print("the student with the highest percent is ",highest_percent)
    #Returns character grade
def getGrade(avg):
    grade=' '
#Set grade on average score
    if(avg>=90):
        grade='A'
    elif avg>=80 and avg<90:
        grade='B'
    elif avg>=70 and avg<80:
        grade='C'
    elif avg>=60 and avg<70:
        grade='D'
    else:
        grade='F'
    return grade

def highest_in_the_room(avg):
    highest_percentage = 0
    if avg > highest_percentage:
        highest_percentage = avg
        
    return highest_percentage
main()