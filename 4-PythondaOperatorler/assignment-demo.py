x,y,z = 2,5,10

numbers = 1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

# a = int(input('1.sayı: '))
# b = int(input('2.sayı:'))

# result = (a * b) - (x+y+z)
# print(result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.
# result = y//x
# print(result)

# 3- (x,y,z) toplamının mod 3 ü nedir?
# toplam = (x+y+z)
# result = toplam%3
# print(result)

# 4- y'nin x kuvvetini hesaplayınız.
# result = y**x
# print(result)

# 5-  x, *y,z = numbers göre z'nin küpü kaçtır?

x, *y, z = numbers
print(numbers)
# print(x)
# print(y)
# print(z)
result = z ** 3
print(result)

# 6- x, *y,z = numbers işlemine göre y'nin değeri toplamı kaçtır?

numbers = 1,5,7,10,6

x,*y,z = numbers

print(y)
result =y[0]+y[1]+y[2]
print(result)


 