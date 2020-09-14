"""2.18. Сформировать и вывести на экран все возможные переносы данного слова. Перенос почти всегда будет выполняться правильно, если пользоваться такими правилами:
а) две идущие подряд гласные можно разделить, если первой из них предшествует согласная, а за второй идет хотя бы одна буква (буква й при этом рассматривается с предшествующей гласной как единое целое);
б) две идущие подряд согласные можно разделить, если первой из них предшествует гласная, а в той части слова, которая идет за второй согласной, имеется хотя бы одна гласная (буквы ь,ъ при этом рассматриваются как единое целое с предшествующей согласной);
в) если правила, указанные в пунктах (а) и (б) применить невозможно, то следует попытаться разбить слово так, чтобы первая часть содержала более чем одну букву и оканчивалась на гласную, а вторая содержала хотя бы одну гласную."""


word = input('Введите слово: ')
sogl = 'бвгджзклмнпрстфхцчщшБВГДЖЗКЛМНПРСТФХЦЧШЩ'
gl = 'аоиеёэыуюяАОИЕЁЭЫУЮЯ'
zn = 'ьЬъЪ'
q = 'Йй'
l = len(word)
cf = 0
ct = 0
b = False
s = 0
nword = ''
for i in range(l):
	if len(word[:i]) > 0:
		for j in word[i+1:]:
			if j in gl:
				cf += 1
		if i+3 <= l:
			if (word[i+1] in sogl) and (word[i+2] in sogl):
				s = 1
			if (word[i] in gl) and (word[i+1] in q) and (word[i+2] in gl):
				if (word[i-1] in sogl) and (len(word[i+2:]) > 0):
					if ct == 0:
						nword = word[0:i+2] + '-' + word[i+2:]
					else:
						nword = nword[0:i+2+ct] + '-' + word[i+2:]
					ct += 1
					b = True
			if (word[i] in sogl) and (word[i+1] in zn) and (word[i+2] in sogl):
				if (word[i-1] in gl) and (cf >= 1):
					if ct == 0:
						nword = word[0:i+2] + '-' + word[i+2:]
					else:
						nword = nword[0:i+2+ct] + '-' + word[i+2:]
					ct += 1
					b = True
		if i+2 <= l:
			if (word[i] in gl) and (word[i+1] in gl):
				if (word[i-1] in sogl) and (len(word[i+2:]) > 0):
					if ct == 0:
						nword = word[0:i+1] + '-' + word[i+1:]
					else:
						nword = nword[0:i+1+ct] + '-' + word[i+1:]
					ct += 1
					b = True
			if (word[i] in sogl) and (word[i+1] in sogl):
				if (word[i-1] in gl) and (cf >= 1):
					if ct == 0:
						nword = word[0:i+1] + '-' + word[i+1:]
					else:
						nword = nword[0:i+1+ct] + '-' + word[i+1:]
					ct += 1
					b = True
		if b == False and (len(word[i+1:])>1):
			if (word[i] in gl) and (cf >= 1) and (s == 0):
				if ct == 0:
					nword = word[0:i+1] + '-' + word[i+1:]
				else:
					nword = nword[0:i+1+ct] + '-' + word[i+1:]
				ct +=1
		cf = 0
		b = False
		s = 0
print(nword)
input()