x = 5
hak = 0
devam = 'e'


result = 5<x<10
print(result)

result = 5<=x<10
print(result)

# and 
result= (x>4) and (x<10)
print(result)

result = (hak>0) and (devam== 'e')
print(result)

result = (x >0) and (x%2 == 0) # Her ikisinde doğru olmalıki True sonuç versin.
print(result) # x simiz sıfırda büyük ama modu 2 olduğu için false sonuç verdi.


# or
result = (x >0) or (x%2 == 0) # Her ikisinden biri doğru olmalıki True sonuç versin.
print(result) # Herhangi biri doğru(x 5 olduğu için sıfırdan büyük) olduğu için True sonucunu verdi


# not
result = (x > 0) 
print(result)

result = not(x > 0) 
print(result)


# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2 ==0)
print(result) 



