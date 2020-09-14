"""2.18. Сформировать и вывести на экран все возможные переносы данного слова. Перенос почти всегда будет выполняться правильно, если пользоваться такими правилами:
а) две идущие подряд гласные можно разделить, если первой из них предшествует согласная, а за второй идет хотя бы одна буква (буква й при этом рассматривается с предшествующей гласной как единое целое);
б) две идущие подряд согласные можно разделить, если первой из них предшествует гласная, а в той части слова, которая идет за второй согласной, имеется хотя бы одна гласная (буквы ь,ъ при этом рассматриваются как единое целое с предшествующей согласной);
в) если правила, указанные в пунктах (а) и (б) применить невозможно, то следует попытаться разбить слово так, чтобы первая часть содержала более чем одну букву и оканчивалась на гласную, а вторая содержала хотя бы одну гласную."""


sl = input("Введите слово: ")
sogl = 'бвгджзклмнпрстфхцчщшБВГДЖЗКЛМНПРСТФХЦЧШЩ'
gl = 'аоиеёэыуюяАОИЕЁЭЫУЮЯ'
a = True
b = True
c = 0 
e = 0
f = 0
x = ""
for i in range(len(sl)):
	try:
		sl[i+1]
	except IndexError:
		continue
	if (sl[i] in gl) and ((sl[i+1]) == 'й' or 'Й'):
		try:
			sl[i+3]
		except IndexError:
			a = False
		if ((sl[i-1]) in sogl) and (a != False):
			if (sl[i+2]) in gl:
				if c == 0:
					x = sl[0:i+2] + '-' + sl[i+2:]
				else:
					x = x[0:i+2] + '-' + sl[i+1:]
				c += 1
			a = True
	if (sl[i] in gl) and (sl[i+1] in gl):
		try:
			sl[i+2]
		except IndexError:
			a = False
		if (sl[i-1] in sogl) and (a != False):
			if c == 0:
				x = sl[0:i+1] + '-' + sl[i+1:]
			else:
				x = x[0:i+2] + '-' + sl[i+1:]
			c += 1
			a = True
	if (sl[i] in sogl) and ((sl[i+1]) == 'ъ' or 'Ъ' or 'ь' or 'Ь'):
		try:
			sl[i+3]
		except IndexError:
			a = False
		if ((sl[i-1]) in gl) and (a != False):
			if (sl[i+2]) in sogl:
				for j in range(len(sl[i+2:])):
					if sl[j] in gl:
						e += 1
						break
			if e == 1:
				if c == 0:
					x = sl[0:i+2] + '-' + sl[i+2:]
				else:
					x = x[0:i+2] + '-' + sl[i+1:]
				c += 1 
			e = 0
			a = True
	if (sl[i] in sogl) and (sl[i+1] in sogl):
		try:
			sl[i+2]
		except IndexError:
			a = False
		if (sl[i-1] in gl) and (a != False):
			for j in range(len(sl[i+1:])):
				if sl[j] in gl:
					e += 1 
					break
			if e == 1:
				if c == 0:
					x = sl[0:i+1] + '-' + sl[i+1:]
				else:
					x = x[0:i+2] + '-' + sl[i+1:]
				c += 1
			a = True
			e = 0
if c == 0: 
	for k in range(len(sl)):
		if (sl[k] in gl) and (len(a[:k]) >= 1):
			for z in range(len(sl[k+1:])):
				if sl[z] in gl:
					f += 1 
					break
			if f == 1:
				x = sl[0:k+1] + '-' + sl[k+1:]
print(x)
input()
