#Problem Statement = https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    n = int(input())
    if n>1 and n<11 :
        student_marks = {}
        for name in range(n):
            name, *line = input().split()
            if len(line) < 4:
                int_line = []
                for num in line:
                    if float(num) > -1.00 and float(num) < 101.00:
                        int_line.append(float(num))
                    else:
                        raise Exception("numbers should be between 1 to 100")
                                    
            else:
                raise Exception("length of array = 3")
            scores = list(map(float, int_line))
            student_marks[name] = scores
        query_name = input()
        find_avg_of=student_marks.get(query_name)
        avg_is = sum(find_avg_of)/len(find_avg_of)
        two_decimal = "{:.2f}".format(avg_is)
        
        print(two_decimal)
        
    else:
        raise Exception("Sorry, no numbers below "+str(n)+" and above "+str(n))