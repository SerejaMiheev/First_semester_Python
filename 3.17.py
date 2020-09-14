'''3.17. Напишите программу, объединяющую первую «половину» элементов первого списка со второй «половиной» элементов второго списка. '''


one = []
two = []
a = int(input('Введите количество элементов первого списка: '))
if a > 0:
	print('Введите элементы списка')
else:
	print('Вы ввели недопустимое значение')
	input()
	exit()
for i in range(a):
	one.append(input())
b = int(input('Введите количество элементов второго списка: '))
if b > 0:
	print('Введите элементы списка')
else:
	print('Вы ввели недопустимое значение')
	input()
	exit()
for i in range(b):
	two.append(input())
if (a%2 == 0) and (b%2 == 0):
	one[len(one)//2:] = two[len(two)//2:]
	print('Результат '+str(one))
elif(a == 1) and (b == 1):
	r = one[:] + two[:]
	print('Результат' +str(r))
else:
	print('''Количество элементов одного или несколько списков нечётное:
		Введите '1', если хотете округлить в большую сторону.
		Введите '2', если хотите округлить в меньшую сторону.''')
	x = input('Введите число, соответствующее ответу: ')
	if x == '1':
		if (a%2 == 0) and (b%2 != 0):
			one[len(one)//2:] = two[len(two)//2:]
			print('Результат '+str(one))
		elif (a%2 != 0) and (b%2 == 0):
			one[1+len(one)//2:] = two[len(two)//2:]
			print('Результат '+str(one))
		elif (a%2 != 0) and (b%2 != 0):
			one[1+len(one)//2:] = two[len(two)//2:]
			print('Результат '+str(one))
	if x == '2':
		if (a%2 == 0) and (b%2 != 0):
			one[len(one)//2:] = two[1+len(two)//2:]
			print('Результат '+str(one))
		elif (a%2 != 0) and (b%2 == 0):
			one[len(one)//2:] = two[len(two)//2:]
			print('Результат '+str(one))
		elif (a%2 != 0) and (b%2 != 0):
			one[len(one)//2:] = two[1+len(two)//2:]
			print('Результат '+str(one))
	else:
		print('Вы не ввели нужное число')
input()