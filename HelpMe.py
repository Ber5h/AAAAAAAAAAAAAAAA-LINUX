import os
import math
def is_degree_two(M):
    while M!=1:
        if M%2==1:
            return False;
        M = M/2
    return True

def bin_helpme(inform_weight, i):
    s = f'{i:b}
    while len(s) < inform_weight:
        s = '0'+s;

f = open('q.txt')
s = f.read()
a = [] #список букв в строке
for i in range(len(s)): #мне нужен физический смысл каждой строчки
    new_symbol = True #проверяет, нужен ли новый символ
    for j in range(len(a)): #АААААААААА ПОМОГИТЕ Я КОДЮ В БЛОКНОТЕ
        if s[i] == a[j]: #символ строки совпадает с символом списка => новый символ не нужен
            new_symbol = False
    if new_symbol :
        a.append(s[i])
#M == len(a)
#print(a)
bin_list = []
M = len(a)
while !is_degree_two(M):
    M+=1; #доходит до 2**i
inform_weight = log(M, 2)
#у нас есть i
for i in range (inform_weight):
    bin_list.append (bin(i)[bin_helpme(inform_weight, i)])
