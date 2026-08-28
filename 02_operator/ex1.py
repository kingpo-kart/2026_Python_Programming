# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  #나머지
print(a // b) #몫
print(a ** b) 

# 복합 대입 연산자
a += 4
print(a)

a -= 10
print(a)

# 증감 연산자
#a++ 
a += 1

# 비교 연산자
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble") #False
print(1 < 2 < 3) # 1 < 2 and 2 < 3
print(1 < 3 < 2) 

# 논리 연산자 (and, or, not)
print(True and True)
print(True or False)
print(not True)

# Short-circuit 테스트
a = 10
b = 0

#print(a / b)
if a > 0 or a / b:
    print("yes")
else:
    print("no")

#비트 연산자
a = 5 # 0000 0101
b = 3 # 0000 0011
print(a & b) # 0000 0001
print(a | b) # 0000 0111
print(a ^ b) # 0000 0110
print(a << b)# 5 -> 10 -> 20 -> 40
print(40 >> 3)#5
print(~a) # 1111 1010 -> -6

# 멤버십 연산자
print( "a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a > b ? a : b;
max = a if a > b else b

print("짝수" if a % 2 == 0 else "홀수")

score = 85
#90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 70점 미만이면 D
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(grade)