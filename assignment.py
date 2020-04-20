'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*

과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. input.py 문제 2개 풀기 (4월 20일까지)

과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''
print('1.')
for i in range(10):
    print('*' * (10 - i))

print('2.')
for i in range(1, 10):
    print('2', 'X', i, '=', i*2 )

print('3.')
num = 0
total = 0
while num < 999:
    num += 3
    total += num
print(total)

num = 0
total = 0
while num < 1001:
    num += 1
    if (num % 3) != 0: continue
    total += num
print(total)

print('4.')
total = 0
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
for i in mutsa_scores:
    total += i
print(total / 6)