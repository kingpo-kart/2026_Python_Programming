# 리스트 심화

# ===========================================================
#  리스트에서 제공하는 메소드
# ===========================================================

langs = ["c", "c++", "java", "python"]

langs.append("go")
print(langs)

langs.insert(2, "c#")
print(langs)

langs[3] = "javascript"
print(langs)

langs.remove("c++")
print(langs)


langs.pop(1)
print(langs)

langs.pop()
print(langs)

print(langs.index("python"))

langs.reverse()
print(langs)

langs.sort()
print(langs)

langs.sort(reverse=True)
print(langs)

langs.clear()
print(langs)
#                   # 끝에 추가
# print(langs)

#                # 인덱스 2에 "c#" 추가
# print(langs)

#              # 인덱스 3을 "javascript"로 변경
# print(langs)

#                  # "c++" 삭제 (첫번째 데이터만 삭제)
# print(langs)

#                         # 인덱스 1 삭제
# print(langs)

#                          # 인덱스 생략 시 마지막 항목 삭제
# print(langs)

# print()        # "python" 인덱스 찾기

#                      # 리스트 순서를 거꾸로 뒤집기
# print(langs)

#                         # 오름차순 정렬
# print(langs)

#             # 내림차순 정렬
# print(langs)

#                        # 모든 item 삭제
# print(langs)

# 리스트 복사
ori = [1, 2, 3]

result = ori.copy()
print(result)
result.append(10)   
print(ori, result)
result = ori

# 얕은 복사(shallow copy) vs 깊은 복사(deep copy)
ori = [[1, 2], [3, 4]]

result2 = ori.copy()
result2.append(100)  # 원본이 같이 바뀜

print(ori, result2)


# 깊은 복사를 하려면?
import copy

result2 = copy.deepcopy(ori)

result2[0].append(1000) # 복사본만 바뀜

print(ori, result2)


# ===========================================================
#  그 외
# ===========================================================

# 중첩리스트
nested_list = [1, ["a", ["x", "y"], "b"], 2]

print(nested_list[1][1][0])         # x 출력하기
print(nested_list[1][2])            # b 출력하기
print(nested_list[2])               # 2 출력하기

# 리스트 언패킹
num = [1,2,3,4]

print(*num)

a, b, c, d = num
print(a, b, c, d)

a, *b, c = num  #확장 언패킹
print(a, b, c) 

num2 = [5,6]
print(num + num2) #리스트 합치기

print([*num, *num2])

# zip함수: 반복 가능(iterable)한 여러 객체를 인자로 받아
# 동일한 인덱스에 있는 원소들끼리 튜플로 묶어주는 파이썬 내장 함수
subjects = ["국어", "수학", "영어", "과학"]
scores = [80, 90, 95]

print(zip(subjects, scores))

a, b, c = zip(subjects, scores) # strict = true
print(a, b, c)

for subject, score in zip(subjects, scores):
    print(f"{subject}: {score}점")

print([zip(subjects, scores)]) #[x] : x 자체를 원소 하나로 해서 리스트에 넣음
print(list(zip(subjects, scores)))

print(["python"])
print(list("python"))

# ===========================================================
#  List Comprehension
#  for문을 이용하여 각 원소에 식을 적용하여 리스트를 만드는 방법
# ===========================================================

# 1 ~ 10의 제곱수 리스트 만들기
result = []
for i in range(1, 11, 1):
    result.append(i ** 2)
print(result)

result = [x ** 2 for x in range(1, 11)]
print(result)

# 1 ~ 10 중 짝수의 제곱수로 된 리스트 만들기 (필터링 if문 추가)
result = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(result)

# 1 ~ 10 중 짝수면 "짝", 홀수면 "홀" 출력하기
result = ["짝" if x % 2 == 0 else "홀" for x in range (1, 11)]
print(result)

# 각 이름의 길이로 이루어진 리스트 만들기
names = ["pororo", "crong", "poby", "eddy"]
result = [len(names[x]) for x in range(0, len(names))]
print(result)

# 길이가 5 이상인 이름만 뽑기


# 중첩 for문도 가능



# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 60점 이상인 점수만 뽑기
scores = [85, 42, 73, 55, 90, 68, 35, 100]

result = [x for x in scores if(x >= 60)]
print(result)                       # ✅ [85, 73, 90, 68, 100] 출력


# 2️⃣ 60점 이상인 경우 "합격", 60점 미만은 "불합격"으로 처리
result = ["합격" if(x >= 60) else "불합격" for x in scores]
print(result)                       # ✅ ['합격', '불합격', '합격', '불합격', '합격', '합격', '불합격', '합격']


# 3️⃣ 1 ~ 100 중 3 또는 5의 배수의 합 구하기 (sum() 함수 이용)
result = sum(x for x in range(1, 101) if(x % 3 == 0 or x % 5 == 0))
print(result)                       # ✅ 2418 출력


# 4️⃣ n을 포함하고 있는 단어만 뽑기
words = ["apple", "banana", "kiwi", "mango"]

result = [x for x in words if("n" in x)]  
print(result)                       # ✅ ['banana', 'mango'] 출력


# 5️⃣ 세 학생의 3과목 점수표에서 과목별 평균 구하기
scores = [
    [90, 80, 70],       # 학생 1
    [100, 90, 80],      # 학생 2
    [80, 70, 60],       # 학생 3
]

std1 = scores[0]
std2 = scores[1]
std3 = scores[2]

result = [sum(score)/3 for score in zip(std1, std2, std3)]
print(list(zip(*scores)))
result = [round(sum(score) / len(score), 2) for score in zip(*scores)]
print(result)                       # ✅ [90.0, 80.0, 70.0]

#은행가 반올림
print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))