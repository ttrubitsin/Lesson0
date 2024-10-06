# 1st program
print(9**0.5*5)

# 2nd program
print(9.99>9.98,1000!=1000.1)

# 3rd program
print(2*2+2)
print(2*(2+2))
print(2*2+2 == 2*(2+2))

#4th program
convert_type = float('123.456') #присвоил переменой convet_type преобразованное исходное значение в тип данных float
print(convert_type) # проверил преобразованое  значение
print(type(convert_type)) # проверил тип преобразованного значения
step_float = convert_type*10 # сместил значение после точки в целую часть
print(step_float) # проверил результат смещения
convert_int = int(step_float) #преобразовал в целое число
print(convert_int) #проверил результат преобразования в целое число
result = convert_int%10 # применил операцию остатка от деления для нахождения результа
print(result) # проверл результат.