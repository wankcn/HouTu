text = [4, 9]
content = text.copy()
text.append(13)
content.append([5, 10])
print(content)
print("hello" + ' ' + "Python")
##############
text = "Tomorrow"
print(text.find("m", 3))

text = "one three"
print(text.find("e", 3, 8))

# num = input("aaa:")
# print(type(num))


str = " https://www.imooc.com/"
print(str.find("im", 14))

print("#################################")
print(6.0 == int('6'))
print("imooc".upper() == 'IMOOC')
print("imooc ".rstrip() != 'imooc')
print(" imooc ".strip() == 'Imooc')

print(set([1, 2, 3]))
print(set((1, 2, 3)))
# print(set(1, 2, 3))
print("#################################")
num = 6.0
print(type(num))



num1 = input("shuru :")
num2 = input("shuru :")
sum1 =num1+num2
print(sum1)