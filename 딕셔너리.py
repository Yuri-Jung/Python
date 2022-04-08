

# # # # disContainer = {'이름' : '홍길동', '나이':25, '주소':'서대문구 연희로', '취미':['축구','수영','조깅'],'몸무게': 85.3}
# # # # # print(disContainer['주소'])
# # # # # print(disContainer['취미'])

# # # # disContainer['혈액형']='O'
# # # # # print(disContainer)
# # # # disContainer['몸무게']=90
# # # # disContainer['나이']=disContainer['나이']+1
# # # # # print(disContainer)

# # # # del disContainer['몸무게']
# # # # # print(disContainer)

# # # # # print(len(disContainer))

# # # # #print(disContainer.keys())
# # # # #print(disContainer.values())

# # # # for key in disContainer.keys():
# # # #     print(key, '\t:',disContainer[key])

# # # # scores={'c/c++' : 'A', 'JAVA':'B', '모바일':'C','보안':'A+', '해킹':'F', '시스템':'C+'}
# # # # print('#시나리오1')
# # # # print(scores)

# # # # print('#시나리오2')
# # # # print('JAVA: ',scores['JAVA'])
# # # # print('시스템 : ',scores['시스템'])

# # # # print('#시나리오3')
# # # # scores['파이썬']='A'
# # # # scores['OS']='A+'
# # # # print(scores)

# # # # print('#시나리오4')
# # # # scores['JAVA']='F'
# # # # scores['시스템']='A'
# # # # print(scores)

# # # # print('#시나리오5')
# # # # for key in scores.keys():
# # # #     print(key, '\t:', scores[key])
# # # 9
# # # quiz =(['3+2',5,3],['5/2의 몫',2,5],['10-2',8,3],['10*10*2',200,5],['1-(10/4의 나머지)',-1,5],['2*2*2*2',16,3],['4/2',2,3])

# # # answerCount = 0
# # # wrongAnswerCount=0
# # # totalScore = 0

# # # for item in quiz:
# # #     print('문제 : ', item[0])
# # #     answer = int(input('정답을 입력해주세요'))

# # #     if answer == item[1]:
# # #         answerCount+=1
# # #         totalScore+=item[2]
# # #     else:
# # #         wrongAnswerCount+=1
# # # print('-'*30)
# # # print('정답개수\t:', answerCount)
# # # print('오답개수\t:', wrongAnswerCount)
# # # print('Total Score \t :', totalScore)
# # # print('-'*30)


# # from unittest import result


# # quiz=(['3+2',5,3],['5/2의 몫',2,5],['10-2',8,3],['10제곱*2',200,5],['1-(10/4의 나머지)',-1,5],['2의 네제곱',16,3],['4/2',2,3])
# # correctAnswer = 0
# # wrongAnswer = 0
# # totalScore=0

# # for item in quiz:
# #     print('문제 : ',item[0])
# #     answer=int(input('정답을 입력하세요'))
# #     if answer==item[1]:
# #         correctAnswer+=1
# #         totalScore+=item[2]
# #     else :
# #         wrongAnswer+=1

# # print('-'*30)
# # print('정답개수 : ',correctAnswer)
# # print('오답개수 : ',wrongAnswer)
# # print('Total Score : ',totalScore)
# # print('-'*30)

# members={}
# flag = True

# while flag:
#     selectNum = int(input('\n1.회원가입, 2.프로그램 종료\t'))

#     if selectNum==1:
#         id=input('아이디를 입력하세요.\t')
#         pw=input('비밀번호를 입력하세요.\t')
#         members[id]=pw

#     elif selectNum==2:
#         print('-'*30)
#         print('아이디 : 비밀번호')
#         print('-'*30)

#         for key in members.keys():
#             print(key, '\t:\t', members[key])
#         print('-'*30)

#         flag =False