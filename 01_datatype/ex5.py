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