'''6.12.  Написать регулярное выражение, определяющее является ли данная строчка валидным E-mail адресом. Примеры правильных выражений:
user@example.com, root@localhost. Примеры неправильных выражений: bug@@@com.ru, @val.ru, Just Text2.'''


import re
mail = input("Введите e-mail: ")
p = re.compile (r"^([a-z0-9_.+-]+)@(([a-z0-9]+\.?)+[a-z]{2,6})$", re.S | re.I)
print("E-mail является валидным" if p.search(mail) else "E-mail не является валидным")
input()