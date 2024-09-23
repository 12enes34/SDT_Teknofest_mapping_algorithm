import turtle
import qrcode
import time
from PIL import Image

# Ekran oluşturma
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Ekranı tam ekran yapar

screen.bgcolor("white")  # Arka plan rengini beyaz yapma
screen.title("Kare Şeklinde İşaretçi")

last_location=[0,0]

# Kare şeklinde bir işaretçi oluşturma
t = turtle.Turtle()
t.penup()
t.goto(last_location)
t.pendown()

t.shape("square")  # Turtle'ın şeklini kare olarak ayarla
t.shapesize(2.5, 2.5)  # Turtle'ın boyutunu 50x50 piksel olarak ayarla (varsayılan boyut 20x20 pikseldir)
t.color("black")  # İşaretçinin rengini siyah yap


def move(x,y):
    """Turtle'ı verilen x ve y kadar hareket ettirir."""
    #t.penup()  # Çizim yapmadan önce kalemi kaldır
    last_location[1] += y
    t.goto(last_location)  # Verilen koordin
     
    last_location[0] += x
    t.goto(last_location)



def draw_filled_rectangle(width, height, color="black"):
    """Belirli bir konumda içi boyalı bir dikdörtgen çizer."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(last_location)

    t.pendown()
    t.begin_fill()
    t.fillcolor(color)

    

    t.forward(width/2)
    t.left(90)
    t.forward(-height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(-height)
    t.left(90)
    t.forward(width/2)
        
    t.end_fill()




move(0,400)

move(300,0)

#yuk alma alanina gidis

move(0,-300)
move(0,-100)

draw_filled_rectangle(55,55,'yellow')

move(0,-100)
move(0,-300)

move(-300,0)

move(0, 400)


