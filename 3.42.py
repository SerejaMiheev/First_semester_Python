'''3.42. Даны два целочисленных списка, содержащих одинаковое количество чисел. Написать программу, которая печатает «Да»,
 если эти списки состоят из одинаковых элементов, и «Нет» - в противном случае.'''


one = []
two = []
a = int(input('Введите количество элементов первого и второго списка: '))
if a <= 0:
	print('Вы ввели некорректное количество элементов')
	input()
	exit()
else:
	three = [0] * a 
	print('Введите элементы первого списка, после каждого элемента нажмите \'Enter\'')
	for i in range(a):
		one.append(input())
	print('Введите элементы второго списка, после каждого элемента нажмите \'Enter\'')
	for i in range(a):
		two.append(input()) 
for i in range(a):
	if (one[i] in two) == True:
		b = two.index(one[i])
		if three[b] == 0:
			del three[b]
			three.insert(b,1)
		elif three[b] == 1:
			for j in range(b,a):
				if two[j] == one[i]:
					if three[j] == 0:
						del three[j]
						three.insert(j,1)
						break	
if all(three) == True:
	print('Да, списки состоят из одинаковых элементов')
else:
	print('Нет, списки не состоят из одинаковых элементов')
input()
