# 파이썬에서 입력을 받는 함수가 있습니다~~ 구글링해서 찾아보세요!

print('문제 1. 전화번호 받기')

print('조건 1. 저장할 때는 공백 문자 없이')
print('조건 2. -, ., , 등이 들어올 때 전부 제외 하고 숫자만 저장!')

print('문제 2. 영어 이름 받기')
print('choi juwon 을 입력 받으면,')
print('first name : Choi, last name: Juwon 이 출력되게 만들기')

print('1.')
phone_num = input("전화번호를 입력하세요 :")
phone_num = phone_num.replace('-','').replace('.','').replace(',','').replace(' ','')
print(phone_num)

print('2.')
name = input("영문 이름을 입력해주세요:")
name = name.title().split()
print("first name : ",name[0],", last name: ",name[1])