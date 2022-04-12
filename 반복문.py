# for num in range(2,10,2):
# #     print('num : ',num)

# num = int(input('메일 발송 횟수를 입력하세요.'))

# for num in range (1,num+1,1):
#     print('메일이 발송되었습니다')



# for num in range (1,10,1):
#     print('num = ',num)
#     if num%3==0:
#         print('3의 배수!')

# for num in range(1,10,1):
#     print(5, end = '')
#     print('*',end='')
#     print(num, end='')
#     print('=',end='')
#     print(5*num)

# for i in range(1,11):
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# num = 1
# while num <5:
#     print(num)
# #     num+=1

# num =1
# while num<31:
#     if num%2==0:
#         print('짝수 : ',num)
#     else :
#         print('홀수 : ',num)
#     num+=1


# num =1
# while num<=9:
#     print('3*',end='')
#     print(num,end='')
#     print(' = ', end='')
#     print(3*num)
#     num+=1

# sum = 0

# for num in range(0,11):
#     sum+=num
# print('sum: ',sum)

# sum=0
# num=0

# while num<11:
#     sum+=num
#     num+=1

# print('sum : ',sum)


# nowTem = 30.0
# targetTem = float(input('희망온도를 말해주세요'))

# for i in range(1000):
#     nowTem -=0.1
#     print('현재 온도 : ',format(nowTem, '.2f'))

#     if nowTem<=targetTem:
#         break
# print('냉방 기능 종료!')

# for c in 'hello':
#     print(c)

# for num  in range(50):
#     if num%7==0:
#         print('num : ',num)

# num = 1
# minNum =0

# while num<=100:
#     if num%3==0 and num%8==0:
#         print('공배수 : ',num)
#         if minNum==0: minNum=num
#     num+=1
# print('최소공배수 : ',minNum)


# currentTemp = 30.0
# targetTemp = float(input('희망온도를 말해주세요'))

# for i in range(1000):
#     currentTemp-=0.1
#     print('현재온도 : ', format(currentTemp,'.2f'))
#     if currentTemp<=targetTemp:
#         break;
# print('냉방 기능 종료!')

# num = 1
# sum = 0

# while num<11:
#     sum+=num
#     if sum>30:
#         print('num : ',num)
#         break
#     num+=1

# for num in range(1,6):
#     print(num)
# else :
#     print('반복이 끝났습니다!')

#for i in range(5):
    #pass

# from unittest import result


# num=1
# maxSize = 150

# while True:
#     result = ((num*2)*(num*3))/2
#     if result > maxSize : break
#     print('삼각형의 넓이 : ',result)
#     num+=1

# for num1 in range(1,6):
#     for num2 in range(num1):
#         print('*', end='')
#     print()

# for n1 in range (1,10,1):
#     for n2 in range (2,10,1):
#         print(n2, end='')
#         print('x',end='')
#         print(n1,end='')
#         print('=',end='')
#         print(n2*n1, '\t', end='')
#     print()


# from cgitb import lookup


# loopCnt = 6

# for n1 in range(loopCnt):
#     for n2 in range(loopCnt-n1-1):
#         print('', end='')

#     for n3 in range((n1+1)*2-1):
#         print('*', end='')
#     print()
