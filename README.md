# Kare Şeklinde İşaretçi ve QR Kod Gösterimi - Python Turtle Uygulaması

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





