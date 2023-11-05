BLACK = '\u001b[40m'
RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

#1
for i in range(6):
    if i < 3:
        print(f'{GREEN}{"  " * 6}{YELLOW}{"  " * 8}{END}')
    else:
        print(f'{GREEN}{"  " * 6}{RED}{"  " * 8}{END}')

#2
for i in range(9):
        if i < 5:
            print(f'{WHITE}{"  " * (5-i)}{BLACK}{"  " * i}{BLACK}{"  " * (i-1)}{WHITE}{"  " * (4-i)}{END}'
                  f'{WHITE}{"  " * (3-i)}{BLACK}{"  " * (i-1)}{BLACK}{"  " * i}{WHITE}{"  " * (5-i)}{END}')
        else:
            print(f'{WHITE}{"  " * (i-3)}{BLACK}{"  " * (8-i)}{BLACK}{"  " * (7-i)}{WHITE}{"  " * (i-4)}{END}'
                  f'{WHITE}{"  " * (i-5)}{BLACK}{"  " * (7-i)}{BLACK}{"  " * (8-i)}{WHITE}{"  " * (i-3)}{END}')



#3
plot_list = [[0 for i in range(11)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i + 1

step = round(abs(result[0] - result[9]) / 9, 2)

for i in range(10):
    for j in range(11):
        if j == 0:
            plot_list[i][j] = step * (9-i) + step

for i in range(10):
    for j in range (10):
        if abs(plot_list[i][0] - result[j]) < step:
            for k in range(10):
                if k == j:
                    plot_list[i][k] = 1  

for i in range(10):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '..'
        if plot_list[i][j+1] == 1:
            line += '//'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')


#4
with open('sequence.txt') as file:
    result_4 = []
    for num_str in file:
        num = float(num_str)
        if 0 <= abs(num) <= 5:
            result_4 += [num]
print(result_4)