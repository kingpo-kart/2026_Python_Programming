a = "hello, python"
#len() 함수: 객체의 길이를 반환하는 파이썬 내장 함수
print(len(a)) #문자열의 길이 반환
print(len([1, 2, 3, 4, 5])) #리스트의 길이 반환

#대소문자를 변환해주는 문자열 메소드
print(a. upper()) #모든 문자를 대문자로 변환
print(a. lower()) #모든 문자를 소문자로 변환
print(a. capitalize()) #첫 글자만 대문자로 변환
print(a. title()) #각 단어의 첫 글자만 대문자로 변환

#문자열의 공백문자 or 특정 문자를 제거해주는 문자열 메소드
a = "\t   python  \t"
print("[" + a + "]") 
print("[" + a.strip() + "]") #문자열의 양쪽 공백 제거
print("[" + a.lstrip() + "]") #문자열의 왼쪽 공백 제거
print("[" + a.rstrip() + "]") #문자열의 오른쪽 공백 제거

a = "***python***"
print(a.strip("*")) #문자열의 양쪽 특정 문자 제거
print(a.lstrip("*")) #문자열의 왼쪽 특정 문자 제거
print(a.rstrip("*")) #문자열의 오른쪽 특정 문자 제거

s = "Python is fun. I love Python."

#부분 문자열이 처음 등장하는 위치(인덱스)를 반환하는 문자열 메소드
print(s.find("Python")) #0
print(s.index("Python")) #0

print(s.find("Java")) #-1
#print(s.index("Java")) #ValueError: substring not found

#부분 문자열이 몇 번 등장하는지 반환하는 문자열 메소드
print(s.count("o")) #2

#문자열 포함 여부를 알려주는 연산자 (멤버십 연산자)
print("Python" in s) #True
print("Java" in s) #False
print("Python" not in s) #False
print("Java" not in s) #True

#특정 prefix(접두사)로 시작하는지 여부를 알려주는 문자열 메소드
print(s.startswith("Python")) #True

#이전 문자열을 새로운 문자열로 치환하는 문자열 메소드
#문제) replace는 원본 문자열을 바꿀까요? 새로운 문자열을 반환할까요? 답) 새로운 문자열을 반환합니다.
print(s.replace("Python", "C")) #C is fun. I love C.
print(s.replace("Python", "C", 1)) #C is fun. I love Python.

#판별 문자열 메소드 (isXXX())
print("123".isdigit()) #True
print("abc".isalpha()) #True
print("123abc".isalnum()) #True
print(" \t \n".isspace()) #True
print("hello".islower()) #True
print("HELLO".isupper()) #True
print("".isnumeric()) #한자

#구분자를 기준으로 문자열을 나누어 리스트로 반환하는 문자열 메소드
s = "apple, banana, kiwi"
fruits = s.split(", ") #구분자: ", "
print(fruits) #['apple', 'banana', 'kiwi']

#Iterable(반복가능) 객체를 구분자를 기준으로 문자열로 합쳐주는 문자열 메소드
print(", ".join(fruits)) #apple, banana, kiwi

s = "  hello world  "
result = s.strip().upper()
print(result)

email = "abcd@dimigo.hs.kr"
print("@dimigo.hs.kr" in email)

sentence = ""