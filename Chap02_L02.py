name = input("What is your name? ")    

''' 이 부분은 여러줄 주석임
화면에 What is your name? 이 출력되고 커서가 입력을 기다린다. 
사용자가 이름을 입력하고 Enter Key를 누르면 입력된 값이 name이란 변수에 저장된다.'''

print("Hello", name) 
s = input("Enter an integer: ")  # input 함수를 통해 입력 받은 모든 값은 문자열 형태이므로
n = int(s)                       # 숫자를 입력 받아 계산하기 위해서는 입력된 문자형을 정수형으로 변경해야 함
print(n**2)  