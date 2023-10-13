import question_d

print('Celsius\t Fahrenheit')
C=0
while C <= 20:
    F = question_d.get_fahrenheit(C)
    print(C,'\t',F)
    C += 1
    