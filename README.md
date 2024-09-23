# Square Pointer and QR Code Reveal - Python Turtle Application

- [Türkçe Bölüm](#turkce-bolum)
- [English Section](#english-section)

<h1 align="center" style="font-size: 62px;" id="turkce-bolum">TÜRKÇE</h1>

Bu Python projesi, Turtle grafik kütüphanesini kullanarak ekranda kare şeklinde bir işaretçi oluşturur ve hareket ettirir. Ayrıca, engeller, yükleme alanları çizer ve QR kodlarını ekranda gösterir.

## Özellikler

- **Izgara Çizimi**: 1920x1080 çözünürlüğünde bir ızgara sistemi oluşturur.
- **Kare İşaretçi**: Turtle şeklinde bir kare işaretçi oluşturur ve belirlenen koordinatlara hareket ettirir.
- **Engel Çizimi**: Belirli bir konumda dikdörtgen engeller çizer.
- **Yükleme Alanı**: Yükleme alanı için belirlenen bölgelerde dikdörtgenler oluşturur.
- **QR Kod Oluşturma**: Verilen URL veya metin verisinden bir QR kod oluşturur ve ekranda gösterir.
- **Resim Gösterimi**: Belirlenen konumda boyutlandırılmış bir resim gösterir.

## Gereksinimler

Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install pillow qrcode[pil] python-turtle
```

## Kullanım

### Izgara Çizimi:
```python
draw_grid(step=100, line_color="gray", line_thickness=2)
```
Ekranda belirlenen adımlarla gri renkte bir ızgara çizer.

### İşaretçiyi Hareket Ettirme:
```python
move(300, 0)
```
Kare işaretçiyi verilen x ve y koordinatlarına göre hareket ettirir.

### Engel Çizme:
```python
draw_barrier(width=100, height=50, color="blue")
```
Mavi renkli bir dikdörtgen engel çizer.

### Yükleme Alanı Çizme:
```python
draw_load_area(width=50, height=50, color=(1, 0.84, 0))
```
Belirlenen boyutlarda yükleme alanı oluşturur.

### QR Kod Oluşturma:
```python
create_qr_code(data="https://www.example.com", file_path="qrcode.png")
```
Belirlenen URL veya metin verisinden QR kodu oluşturur ve kaydeder.

### Resim Gösterme:
```python
draw_image(input_image_path="engel.png", new_width=50, new_height=50)
```
Belirlenen resim dosyasını ekrana 60x60 piksel boyutunda yerleştirir.


## Örnek Kullanım:
```python
# Izgara çizme
draw_grid(step=100, line_color="gray", line_thickness=2)

# İşaretçiyi hareket ettirme ve engel çizimi
move(300, 0)
draw_barrier(width=100, height=50, color="blue")

# QR kod oluşturma ve gösterme
create_qr_code(data="https://www.example.com", file_path="qrcode.png")
draw_image(file_path="qrcode.png")

# Yükleme alanı çizimi
draw_load_area(width=50, height=50, color=(1, 0.84, 0))
```



<h1 align="center" style="font-size: 62px;" id="english-section">ENGLISH</h1>


This Python project creates and moves a square-shaped marker on the screen using the Turtle graphics library. It also draws obstacles, loading areas, and displays QR codes on the screen.

## Features

- **Grid Drawing**: Creates a grid system with a resolution of 1920x1080.
- **Square Marker**: Creates a Turtle-shaped square marker and moves it to specified coordinates.
- **Obstacle Drawing**: Draws rectangular obstacles at a specified location.
- **Loading Area**: Creates rectangles in specified areas for the loading area.
- **QR Code Generation**: Creates a QR code from the given URL or text data and displays it on the screen.
- **Image Display**: Displays a scaled image at a specified location.

## Requirements

The following libraries must be installed to run the project:

```bash
pip install pillow qrcode[pil] python-turtle
```

## Usage

### Grid Drawing:
```python
draw_grid(step=100, line_color="gray", line_thickness=2)
```
Draws a gray grid on the screen with the specified steps.

### Moving the Pointer:
```python
move(300, 0)
```
Moves the square pointer according to the given x and y coordinates.

### Drawing an Obstacle:
```python
draw_barrier(width=100, height=50, color="blue")
```
Draws a blue rectangular obstacle.

### Drawing Loading Area:
```python
draw_load_area(width=50, height=50, color=(1, 0.84, 0))
```
Creates a loading area with the specified dimensions.

### Creating QR Code:
```python
create_qr_code(data="https://www.example.com", file_path="qrcode.png")
```
Creates and saves a QR code from the specified URL or text data.

### Displaying Images:
```python
draw_image(input_image_path="engel.png", new_width=50, new_height=50)
```
Places the specified image file on the screen with a size of 60x60 pixels.

## Example Usage:
```python
# Draw grid
draw_grid(step=100, line_color="gray", line_thickness=2)

# Move the pointer and draw barriers
move(300, 0)
draw_barrier(width=100, height=50, color="blue")

# Create and display QR code
create_qr_code(data="https://www.example.com", file_path="qrcode.png")
draw_image(file_path="qrcode.png")

# Draw loading area
draw_load_area(width=50, height=50, color=(1, 0.84, 0))
```
