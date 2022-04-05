# print('사용자 정보를 입력하세요')
# userName = input('이름 : ')
# userPn = input('연락처 : ')
# userMail = input('메일 : ')
# userJob = input('직업 : ')

# print('---------------') #이거 없으니까 실행 안된다 이거 필수!!
# print(userName)
# print(userPn)
# print(userMail)
# print(userJob)
# print('----------------')

# sales = int(input('1분기 매출 : '))
# purchase = int(input('1분기 매입 : '))
# total = sales - purchase

# #print('1분기 매출 : '+ sales +'원')
# #print('1분기 매입 : '+ purchase + '원')
# print('수익 : ' , total , '원')

# inputData = int(input('숫자를 입력하세요'))

# if inputData%2==0: 
#   print(inputData,'짝수입니다')
# else :
#        print(inputData,'홀수입니다')


# score = int(input('점수를 입력해주세요'))
# if score>=80:
#     print('축하합니다 합격입니다')
# else : print('다음 기회에')    


# score = int(input('점수를 입력하세요'))

# if score>=60:
#     pass
# else : 
#     pass

# temp = int(input('기계 온도를 입력해주세요'))
# if temp>=40:
#     print('팬 가동')
# else : print('팬 중지')

# score = int(input('점수를 입력해주세요'))

# if score>= 90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>=60:
#     print('D')
# else :
#     print('F')

print('Good morning. Nice to meet you.')
print('Where are you from?')
print('Please choice a number.')
countryNumber=int(input('1.Korea 2.USA 3.China'))

if countryNumber ==1:
    print('주문하시겠어요?')
elif countryNumber ==2:
    print('May I take your order?')
else :
    print ('你想吃什么?')