import qrcode
from PIL import Image

link = "https://fuvstudentcouncil.github.io/yearbook2025/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color=None).convert("RGBA")

datas = img.getdata()
new_data = []
for item in datas:
    if item[:3] == (255, 255, 255):
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)
img.putdata(new_data)

img.save("qr_transparent.png")

