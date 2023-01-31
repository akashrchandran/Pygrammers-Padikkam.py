import os
import qrcode

os.makedirs('qrcodes', exist_ok=True)
print("QR Code Generator", end="\n\n")
print("Enter any data and it will generate QR corresponding to that data!")
data = input("Enter any data: ")
img = qrcode.make(data)
rand_file_name = f"qrcodes/{data[:5]}.png"
img.save(rand_file_name)
print("QR code saved at: ", os.path.abspath(rand_file_name))
