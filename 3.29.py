'''3.29. В заданном списке определить максимальное количество подряд идущих положительных элементов, не прерываемых ни нулями,
 ни отрицательными элементами.'''


arr = []
k = 0
kmax = 0
a = int(input('Введите количество элементов списка: '))
if a <= 0:
	print('Вы ввели некорректное количество элементов')
	input()
	exit()
else:
	print('Введите элементы списка (числа), после каждого элемента нажмите \'Enter\'')
	for i in range(a):
		arr.append(float(input()))
for i in range(a):
	if arr[i] > 0:
		k += 1
	if (arr[i] <=0) or (i == a-1):
		if k > kmax:
			kmax = k
			k = 0 
print('Максимальное количество подряд идущих положительных элементов: '+ str(kmax) )
input()