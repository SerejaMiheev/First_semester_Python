'''9.6. Построить ромб по стороне a и острому углу R (в градусах).'''

from PIL import Image, ImageDraw, ImageFont
import math

txt = 'Михеев Т-108'
font_file = r"C:\WINDOWS\Fonts\arial.ttf"
font = ImageFont.truetype(font_file, size=24)
e = 0
print("Размер изображения 800x600")
x = int(input("Введите начальную точку, по оси X: ")) 
y = int(input("Введите начальную точку, по оси Y: "))
a = int(input("Введите длину стороны а: "))
R = float(input("Введите острый угол (в градусах): "))
Rad = math.radians(R)
print(Rad)
cosx = math.cos(Rad)
print(cosx)
ac = a*cosx
print(ac)
bc = a**2-ac**2
print(bc)
bc = math.sqrt(bc)
print(bc)

img = Image.new("RGB",(800,600),"white")
draw = ImageDraw.Draw(img)
#draw.line((x,y,x+a,y), fill="blue")
draw.line((x,y,x+ac,y+bc), fill="blue")
#draw.line((x+ac,y+bc,x+a+ac,y+bc), fill="blue")
#draw.line((x+a,y,x+a+ac,y+bc), fill="blue")
while True:
	if x+e != x+a:
		e += 1 
		draw.line((x+e,y,x+ac+e,y+bc), fill="blue")
	else:
		break
draw.text((x+ac+50,y+bc+50),txt,font=font,fill="blue")
img.save("mypaint.jpg")
img.show()
input()
