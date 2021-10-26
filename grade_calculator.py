def grade(scores):
    average = sum(scores) /3
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'E'

def getHighest(data):
    highest = 0
    for i in range(len(data)):
        if sum(data[i][1:])>sum(data[highest][1:]):
            highest = i
    return highest



def summary(data):
    for record in data:
        print(record[0], grade(record[1:]))
    print('==Summary==')
    print('Number of students:',len(data))
    highest =  getHighest(data)
    print('The student with highest percent is',data[highest][0])
    percent = sum(data[highest][1:])/5
    print('The percent is {:.2f}%'.format(percent))
    As =0
    total= 0
    for record in data:
        if(grade(record[1:]))=='A':
            As+=1
        total += sum(record[1:])
    print('Number of A students is',As,'.')
    average = total/(5*len(data))
    print('The average is {:.1f}'.format(average))



def main():
    file = input('Enter the data file name > ')
    data = []

    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip().split(',')
            row = [int(score.strip()) for score in line[1:]]
            row.insert(0, line[0])
            data.append(row)

    summary(data)



main()
