print("\n##### assign  #####")

apple = 1000 * 3
pear = 2000 * 5 
total = apple + pear
print (total)



print("\n##### string types #####")
a = "I love Tom’s song "
print (a)
b = ' He said " I miss my hometown" '
print (b)

c = """ Python is easy.    #  이 경우 줄바꿈을 포함한 두줄짜리 문자열이 c에 대입됨
    I like Python !!"""
print (c) 


print("\n##### assign  #####")
x = 1
print (x)      	# 결과는 1이 출력 된다.
x = x + 1    	# 이 문장은 = 기호 오른쪽의 x + 1이 먼저 계산되어 그 결과값인 2가 
                #  x라는 변수에 다시 대입된다.
print (x)      	# 이때 x의 값은 2가 출력된다.
 


print("\n##### multiple assignment  #####")
a = 2
b = 3
a = b   # 이 문장에서 a의 값은 3으로 변경됨
b = a   # 그래서 b에 a 값을 넣을 때는 기존의 2는 이미 사라지고 3이 대입됨
print (a, b)

a = 2
b = 3
temp = a   # a의 값을 temp 변수에 저장한 후
a = b       # a의 값을 3으로 변경함
b = temp   # b에는 a 가 아닌 a 값을 저장해둔 temp 값을 대입함 
print (a, b)  # 결과는 3 2로 두 값이 서로 바뀐 것을 볼 수 있음


a , b = 2 , 3	# a = 2, b = 3과 동일한 대입이 이루어짐
a , b =  b , a   # 대입 기호 오른쪽의 b와 a 값이 = 기호 왼편의 두 변수 a와 b로 대입됨
print (a, b)      # 결과는 3 2로 두 값이 서로 바뀐 것을 볼 수 있음


x,y,z,p,q = 1,2,3,4,5
x, y, z = y, z, x
p, q = p * q, p - q -1          
print (x,y,z)  # 2 3 1
print(p,q)   # 20 -2           

print("##### import  #####")
import keyword
print (keyword.kwlist)


print("##### expression #####")
p = (x + y**2)**3 + 2*(x + y**2) + (x**2 + 1)**y
a = x + y**2 
b = x**2 + 1 
p = a**3 + 2*a + b**y


print("##### data types #####")
print(type(7))                             
print(type(7.0))              
print(type("7"))    
print(type(7//3))         
print(type(7/3))          

# 추가로 한 줄을 보탭니다. 


