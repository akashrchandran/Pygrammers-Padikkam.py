import os
import qrcode

qr = qrcode.QRCode()
os.makedirs('qrcodes', exist_ok=True)
print("QR Code Generator", end="\n\n")
print("Enter any data and it will generate QR corresponding to that data!")
data = input("Enter any data: ")
qr.add_data(data)
file_name = f"qrcodes/{data[:5]}.png"
img = qr.make_image()
img.save(file_name)
print("Generated QR code:")
qr.print_ascii()
print("QR code saved at: ", os.path.abspath(file_name))