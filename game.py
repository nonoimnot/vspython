import random
import time

sc_com = 0
sc_name = 0
i = 0

def score(sc_com,sc_name):
    print('\n********************* Score **********************')
    print('      com  = ', str(sc_com), '                   ', name, ' = ', str(sc_name))
    print('**************************************************\n')


print('****************************************************')
print('*                       เป้า ยิ้ง ฉุบ                     *')
print('****************************************************\n')
rps = ['r','p','s']
name = input('ชื่ออะไรจ๊ะหนูน้อย  ->  ')
round = input('จะเล่นกันกี่รอบดี -> ')

while i < int(round):
    print('\n\nรอบที่ ',str(i+1))
    score(sc_com,sc_name)
    choice = input('ลองเลือกอะไรซักอย่างซิ (R)ค้อน (P)กระดาษ (s)กรรไกร :  ')
    choice_com = random.choice(rps)
    time.sleep(0.25)
    print('\n')

    if choice == 'r':
        if choice_com == 'r':
            print('เค้าก็ออก ค้อน เสมอกันจ้า ')
        elif choice_com == 'p':
            print('เค้าออก กระดาษ ละตะเอง แพ้แล้วเด็กน้อย')
            sc_com += 1
        else:
            print('เค้าออก กรรไกร ชนะไปเลยจ้า ฝากไว้ก่อนนะ', name)
            sc_name += 1
    elif choice == 'p':
        if choice_com == 'r':
            print('เค้าออก ค้อน ชนะไปเลยจ้า ฝากไว้ก่อนนะ', name)
            sc_name += 1
        elif choice_com == 'p':
            print('เค้าก็ออก กระดาษ เสมอกันจ้า ')
        else:
            print('เค้าออก กรรไกร ละตะเอง แพ้แล้วเด็กน้อย')
            sc_com += 1
    elif choice == 's':
        if choice_com == 'r':
            print('เค้าออก ค้อน ละตะเอง แพ้แล้วเด็กน้อย')
            sc_com += 1
        elif choice_com == 'p':
            print('เค้าก็ออก กระดาษ ชนะไปเลยจ้า ฝากไว้ก่อนนะ ', name)
            sc_name += 1
        else:
            print('เค้าออก กรรไกร ละตะเอง เสมอกันนะ')
    else:
        print('\n แกทำอะไรของแก ')
    time.sleep(2)
    i += 1

print('\n********************** สรุปผล ************************')
score(sc_com,sc_name)
    #score(sc_com,sc_name)
    #play = input('เล่นต่อมั้ยจ๊ะ y/n -> ')

    #if play == 'y':
    #    i += 1
    #elif play == 'n':
    #    break
    #else: print('แกทำอะไรของแก อีกแล้ว ....')

