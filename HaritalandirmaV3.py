import turtle
import os
from PIL import Image
import qrcode

# Ekran oluşturma
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Ekranı tam ekran yapar
screen.bgcolor("white")  # Arka plan rengini beyaz yapar
screen.title("Kare Şeklinde İşaretçi")

last_location = [-10, 0]

QrCodeLocation = []
BarrierLocation = []
LoadAreaLocation = []

# Kare şeklinde bir işaretçi oluşturma
t = turtle.Turtle()
t.penup()
t.goto(last_location[0], last_location[1])
t.pendown()

t.shape("square")  # Turtle'ın şeklini kare olarak ayarla
t.shapesize(2.5, 2.5)  # Turtle'ın boyutunu 50x50 piksel olarak ayarla (varsayılan boyut 20x20 pikseldir)
t.color("black")  # İşaretçinin rengini siyah yap
def draw_grid(step=100, line_color="gray", line_thickness=2):
    """1920x1080 çözünürlüğünde ekranı eşit karelere bölen bir ızgara çizer."""
    screen.tracer(0)
    grid_turtle = turtle.Turtle()
    grid_turtle.hideturtle()
    grid_turtle.speed(0)
    grid_turtle.color(line_color)
    grid_turtle.pensize(line_thickness)
    grid_turtle.penup()
    
    width = 1920
    height = 1080
    offset = line_thickness // 2  # Çizgi kalınlığının yarısı kadar boşluk bırakmak için

    # Yatay ve dikey çizgiler
    for x in range(-width//2, width//2, step):
        for y in range(-height//2, height//2, step):
            # Kare çizer
            grid_turtle.goto(x + offset, y + offset)
            grid_turtle.pendown()
            grid_turtle.goto(x + step - offset, y + offset)
            grid_turtle.goto(x + step - offset, y + step - offset)
            grid_turtle.goto(x + offset, y + step - offset)
            grid_turtle.goto(x + offset, y + offset)
            grid_turtle.penup()
    
    screen.tracer(1)


# Hareket fonksiyonunu tanımlama
def move(x, y):
    """Turtle'ı verilen x ve y kadar hareket ettirir."""
    t.pensize(10)
    last_location[1] += y
    t.goto(last_location)
    last_location[0] += x
    t.goto(last_location)

def draw_barrier(width=100, height=50, color="blue"):
    """Belirli bir konumda içi boyalı bir dikdörtgen çizer."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(last_location)
    BarrierLocation.append([last_location[0], last_location[1]])
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
   

def draw_load_area(width=50, height=50, color=(1, 0.84, 0)):
    """Belirli bir konumda içi boyalı bir dikdörtgen çizer."""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.pencolor(color)
    t.pensize(10)
    t.goto(last_location)
    LoadAreaLocation.append([last_location[0], last_location[1]])
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
    t.end_poly()
    #t.end_fill()

def create_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)

def draw_image(input_image_path, new_width=60, new_height=60):
    output_image_path = input_image_path.rsplit('.', 1)[0] + '.gif'
    image = Image.open(input_image_path)
    
    # Resmi yeniden boyutlandır
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_image.save(output_image_path, "GIF")
    
    if not os.path.exists(output_image_path):
        raise FileNotFoundError(f"Converted file not found: {output_image_path}")
    
    absolute_path = os.path.abspath(output_image_path)
    screen.addshape(absolute_path)
    QrCodeLocation.append((absolute_path, [last_location[0], last_location[1]]))
    screen.tracer(0)
    for i in QrCodeLocation:
        t3.shape(i[0])
        t3.goto(i[1])
        t3.stamp()
    screen.update()
    screen.tracer(1)

# Kullanım örneği
input_image_path = "C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/Haritalandirma/engel.png"
new_width = 50  # Yeni genişlik
new_height = 50  # Yeni yükseklik

t3 = turtle.Turtle()
t3.penup()
t3.goto(last_location)

#draw_image(input_image_path, new_width, new_height)

# Izgara çizme
draw_grid(step=100, line_color="gray", line_thickness=2)

# Kullanım örneği
data = "https://www.example.com"
file_path = "C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/qrcode.png"



move(0, 400)
move(300, 0)
move(0, -300)
create_qr_code(data, file_path)
draw_image(file_path)
move(0, -100)
draw_image('C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/Haritalandirma/engel.png')
move(0, -100)
create_qr_code(data, file_path)
draw_image(file_path)
move(0, -300)
move(-300, 0)
move(0, 400)
move(0, 400)
move(300, 0)
move(300, 0)
move(0, -300)
create_qr_code(data, file_path)
draw_image(file_path)

move(0, -40)
draw_load_area(100,100)
move(0, -60)

draw_image('C:/Users/enes_/OneDrive/Masaüstü/Python/SDT(SanayideDigitalTeknolojiler)2024/Haritalandirma/Box.png',80,80) #draw_barrier()
move(0, -100)
create_qr_code(data, file_path)
draw_image(file_path)
move(0, -300)
move(-300, 0)
move(-300, 0)
move(0, 400)
move(0, 400)
move(-300, 0)
move(0, -400)
draw_load_area()
move(0, -400)
move(300, 0)
move(0, 400)
move(0, 400)
move(-300, 0)
move(-300, 0)
move(0, -400)
draw_barrier()
move(0, -400)
move(300, 0)
move(300, 0)
move(0, 400)

turtle.done()
