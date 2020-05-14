#import numpy as np
import os
import math

cls = lambda: os.system('cls')
def intro():
    print('...................................................')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('                   โปรแกรม คำนวณพีทาโกรัส')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('...................................................\n')

    print('   กำหนดให้                            ')
    print('                         /|        ')
    print('                        / |        ')
    print('                    a  /  | b      ')
    print('                      /   |        ')
    print('                     /____|        ')
    print('                       c          \n')
    print('   เมื่อ a^2=b^2+c^2                 \n')

def punpun_c():
    print('   ต้องการหาค่า c ')
    B = input('กรุณาป้อนค่า b  -> ')
    A = input('กรุณาป้อนค่า a  -> ')
    if A <= B:
        print("ค่า a ต้องมีค่ามากกว่า b นะ \n")
        punpun_c()
    else:
        C = math.sqrt(float(A)**2 - float(B)**2 )
        print('ค่า c ที่คำนวณได้มีค่าเท่ากับ ' + str(C))

def punpun_b():
    print('   ต้องการหาค่า b ')
    C = input('กรุณาป้อนค่า c  -> ')
    A = input('กรุณาป้อนค่า a  -> ')
    if A <= C:
        print("ค่า a ต้องมีค่ามากกว่า c นะ \n")
        punpun_b()
    else:
        B = math.sqrt(float(A)**2 - float(C)**2 )
        print('ค่า b ที่คำนวณได้มีค่าเท่ากับ ' + str(B))


def punpun_a():
    print('   ต้องการหาค่า a ')
    B = input('กรุณาป้อนค่า  b ->  ')
    C = input('กรุณาป้อนค่า  c ->  ')
    A = math.sqrt(float(B)**2 + float(C)**2)
    print('ค่า a ที่คำนวณได้มีค่าเท่ากับ  ' + str(A))

def main():
    print('ต้องการหาค่า a, b หรือ c')
    cba = input('->  ')
    if cba == 'a' :
        #print('\n\n')
        punpun_a()
    elif cba == 'b' :
        print('\n\n')
        punpun_b()
    elif cba == 'c' :
        #print('\n\n')
        punpun_c()
    else :
        #print('\n\n')
        cls()
        intro()
        print('แกกดอะไรของแก ...... !!!')
        main()

if __name__ == '__main__':
    intro()
    main()
