if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    students.sort(key = lambda x: (x[1],x[0]))
    second_lowest_grade = next(x for x in students if x[1] > students[0][1])[1]
    print('\n'.join([x[0] for x in students if x[1] == second_lowest_grade]))
