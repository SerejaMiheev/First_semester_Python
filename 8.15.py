'''8.15. Дан символьный файл f, содержащий сведения о сотрудниках учреждения, записанные по следующему образцу:
фамилия_имя_отчество, фамилия_имя_отчество, ... Записать эти сведения в файле g, используя образцы:
а) имя_отчество_фамилия, имя_отчество_фамилия,...;
б) фамилия_и.о., фамилия_и.о.,...'''


import re


def ln(f):
	if len(f) == 0:
		f = ' '
	return f
	
def tx(n):
	txt = '.txt'
	a = len(n)
	if n[a-4:a] not in txt:
		b = n + txt
	else:
		b = n
	return b

def nfile(f1,f2):
	global c
	if f1 == f2:
		f3=f2+str(c)
		c += 1
	else:
		f3=f2
	return f3

def file2(x,y):
	f1=open(x,mode='r')
	f2=open(y,mode='w')
	for line in f1:
		a=p.findall(line)
		for i in range(len(a)//3):
			d=a[i+1]+'_'+a[i+2]+'_'+a[i]
		f2.writelines(d+'\n')
	f1.close()
	f2.close()

def file3(z,s):
	f1=open(z,mode='r')
	f2=open(s,mode='w')
	for line in f1:
		a=p.findall(line)
		for i in range(len(a)//3):
			d=a[i]+'_'+a[i+1][0:1]+'.'+a[i+2][0:1]
		f2.writelines(d+'\n')
	f1.close()
	f2.close()
	
def readf(r):
	f1=open(r,mode='r')
	for line in f1:
		print(line)
	f1.close()
	
c = 1 

p = re.compile(r'[а-яё]+[^_|\n]', re.S | re.I)

nf1 = input('Введите название первого файла: ')
nf1 = ln(nf1)
nf2 = input('Введите название второго файла: ')
nf2 = ln(nf2)
nf3 = input('Введите название третьего файла: ')
nf3 = ln(nf3)

nf2 = nfile(nf1,nf2)
nf3 = nfile(nf2,nf3)
nf3 = nfile(nf1,nf3)

nf1 = tx(nf1)
nf2 = tx(nf2)
nf3 = tx(nf3)

k = int(input('Сколько будет сотрудников?: '))
print('Введите сведения о сотрудниках учреждения, по следующему образцу:')
print('фамилия_имя_отчество, фамилия_имя_отчество, ...(без запятой)')
f1=open(nf1,mode='w')
for i in range(k):
	fio = input('Введите фио: ')
	f1.write(fio+'\n')
f1.close()

file2(nf1,nf2)
file3(nf1,nf3)
print('=====================')
print('Первый файл:')
readf(nf1)
print('=====================')
print('Второй файл:')
readf(nf2)
print('=====================')
print('Третий файл:')
readf(nf3)
print('=====================')

input()