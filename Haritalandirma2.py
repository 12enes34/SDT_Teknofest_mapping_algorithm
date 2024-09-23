import turtle

import os
import time
from PIL import Image
import qrcode
# Ekran oluşturma
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Ekranı tam ekran yapar

screen.bgcolor("white")  # Arka plan rengini beyaz yapma
screen.title("Kare Şeklinde İşaretçi")

last_location       = [0,0]

QrCodeLocation      = []
BarrierLocation     = []
LoadAreaLocation    = []

# Kare şeklinde bir işaretçi oluşturma
t = turtle.Turtle()
t.penup()
t.goto(last_location[0],last_location[1])
t.pendown()


t.shape("square")  # Turtle'ın şeklini kare olarak ayarla
t.shapesize(2.5, 2.5)  # Turtle'ın boyutunu 50x50 piksel olarak ayarla (varsayılan boyut 20x20 pikseldir)
t.color("black")  # İşaretçinin rengini siyah yap
# Hareket fonksiyonunu tanımlama
def move(x,y):
       
    """Turtle'ı verilen x ve y kadar hareket ettirir."""
    #t.penup()  # Çizim yapmadan önce kalemi kaldır
    last_location[1] += y
    t.goto(last_location)  # Verilen koordin
     
    last_location[0] += x
    t.goto(last_location)

def draw_barrier(width=100, height=50, color="blue"):
    """Belirli bir konumda içi boyalı bir dikdörtgen çizer."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(last_location)

    BarrierLocation.append(([last_location[0],last_location[1]])) 


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

def draw_load_area(width=50, height=50, color="yellow"):
    """Belirli bir konumda içi boyalı bir dikdörtgen çizer."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(last_location)

    LoadAreaLocation.append(([last_location[0],last_location[1]])) 


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


def create_qr_code(data, file_path):
    # QR kod objesi oluştur
    qr = qrcode.QRCode(
        version=1,  # Versiyon numarası (1-40 arası)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
        box_size=1,  # Her bir kutucuğun boyutu
        border=4,  # Kenar boşluğu
    )
    
    # Veriyi ekle
    qr.add_data(data)
    qr.make(fit=True)
    
    # QR kodu bir image objesi olarak oluştur
    img = qr.make_image(fill='black', back_color='white')
    
    # Dosyaya kaydet
    img.save(file_path)

    
    
# Kullanım örneği
data = "https://www.example.com"
file_path = "C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/qrcode.png"
#create_qr_code(data, file_path)

t3 = turtle.Turtle()
# t3.hideturtle()
t3.penup()
t3.goto(last_location)


def draw_image(input_image_path):
    output_image_path = input_image_path.rsplit('.', 1)[0] + '.gif'

    # Resmi aç ve GIF olarak kaydet
    image = Image.open(input_image_path)
    image.save(output_image_path, "GIF")

    # Dosyanın gerçekten oluşturulduğunu kontrol edin
    if not os.path.exists(output_image_path):
        raise FileNotFoundError(f"Converted file not found: {output_image_path}")
    

    # Tam dosya yolunu kullanarak GIF resmini turtle kütüphanesine tanıt
    absolute_path = os.path.abspath(output_image_path)
    screen.addshape(absolute_path)
    QrCodeLocation.append((absolute_path,[last_location[0],last_location[1]])) # tekrar da sikinti olammais icin ekleniyor
    # Turtle nesnesini oluştur

    # planiim her qr in konumunu kaydet ve her yeni qr cagrildiginda tum qr lari tekrar ekrana ciz
    
    # Animasyonu kapat
    screen.tracer(0)

    for i in QrCodeLocation:
        
        t3.shape(i[0])
        t3.goto(i[1])
        t3.stamp()
        
    screen.update()
    screen.tracer(1)



# verılen yer degıstırmeye gore yol alıyor




move(0,400)

move(300,0)

#yuk alma alanina gidis

move(0,-300)
create_qr_code(data, file_path)
draw_image(file_path)
move(0,-100)

#draw_load_area()
draw_image('C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/Haritalandirma/engel.png')

move(0,-100)
create_qr_code(data, file_path)
draw_image(file_path)
move(0,-300)

move(-300,0)

move(0, 400)

move(0,400)

move(300,0)



move(300,0)



move(0,-300)

create_qr_code(data, file_path)
draw_image(file_path)

move(0,-100)

draw_barrier()

move(0,-100)

create_qr_code(data, file_path)
draw_image(file_path)

move(0,-300)

move(-300,0)

move(-300,0)

move(0,400)



#move(x,y)





#qr eklenecek engel yerine ve ciahz yerine resim konacak

move(0,400)

move(-300,0)

#yuk alma alanina gidis

move(0,-400)

draw_load_area()

move(0,-400)

move(300,0)

move(0, 400)

move(0,400)

move(-300,0)



move(-300,0)

move(0,-400)

draw_barrier()

move(0,-400)

move(300,0)

move(300,0)

move(0,400)