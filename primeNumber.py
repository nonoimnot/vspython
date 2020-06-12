import os
import math
from random import randrange

i = 0
sc_right = 0
#sc_wrong = 0
primeNb = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

round = input('จะเล่นกันกี่รอบดี -> ')

while i < int(round):
    randNb = randrange(100)
    print(randNb, '  ')
    yourAns = input('คิดว่าจำนวนเฉพาะมั้ย (y/n) >> ')
    if ((randNb in primeNb) and (yourAns == 'y')) or ((randNb not in primeNb) and (yourAns == 'n')):
        print('ถูกต้อง จ้า ')
        sc_right += 1
        print('คะแนนตอนนี้ >> ',sc_right)
    else:
        print('ผิดนะจ้า ')
        print('คะแนนตอนนี้ >> ',sc_right)



    i += 1

print('\n\n คะแนนรวม >> ตอบถูก  ' ,sc_right, ' จาก ', round, ' ข้อ' )
