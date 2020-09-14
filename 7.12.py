'''7.12. В сводке об экспортируемых товарах указывается: наименование товара, страна, импортирующая товар, объем поставляемой партии в штуках. Напечатайте списки стран, в которые экспортируется данный товар, и общий объем его экспорта.'''


d = {}
list = []
st = []
p = []



x = int(input('Введите кол-во различных видов товара: '))
if x >= 1:
	for i in range(x):
		Name = input('Введите название товара: ')
		z = int(input('Сколько стран импортируют данный товар?: '))
		if z >= 1:
			for ii in range(z):
				State = input('В какую страну экспортируется данный товар?:')
				list.append(State)
				Piece = int(input('Введите объем партии в штуках: '))
				if Piece <= 0:
					input('''Для выхода нажмите 'Enter' ''')
					exit()
				list.append(Piece)
		else:
			input('''Для выхода нажмите 'Enter' ''')
			exit()
		d[Name]=list
		list = []
		print()
else:
	input('''Для выхода нажмите 'Enter' ''')
	exit()
print('=====================')
print('Список товаров:')
for key in d:
	print('{0}'.format(key),sep='/n')
print('=====================')
Name2 = input('Введите наименование товара: ')
if d.get(Name2) != None:
	value=d.get(Name2)
	for i in range(len(value)):
		if i%2==0:
			st.append(value[i])
		else:
			p.append(value[i])
	for i in range(len(st)):
		print('В {0} экспортируется {1} шт товара'.format(st[i],p[i]),sep='/n')
else:
	print('Такого товара нет')
input('''Для выхода нажмите 'Enter' ''')
