# for i in range(1,100,1):
#     if i<=9:
#         if i%3==0:
#             print(i,'짝!',end='')
#         else : 
#             print(i, end='')
#     else:
#         print(i, end='')

#         firstNum=i//10
#         secondNum=i%10

#         if firstNum %3 ==0:
#             print('짝!', end='')

#         if secondNum%3 == 0 and secondNum!=0:
#             print('짝!', end='')
# print()

adminPw= 'habitac'
count=1

while True:
    if count>5:
        print('로그인 실패!! 횟수 초과!')
        break
    
    inputPw = input('관리자 암호를 입력하세요')

    if inputPw!=adminPw:
        print('암호를 다시 확인하세요!')
        count+=1
    elif inputPw ==adminPw:
        print('로그인 되었습니다')
        break
