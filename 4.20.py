'''4.19*. Из первой сотни натуральных чисел найти все простые с помощью решета Эратосфена. 
Для представления решета используйте множество!'''

s = set()
n = 100
p = 0
for i in range(1,n+1):
	s.add(i)
for i in range(2,n+1):
	if i <= n:
		p = i**2
		for j in range(3,n+1):
			if p <= n:
				s.discard(p)
				p +=i
s.remove(1)
print(s)
input()
