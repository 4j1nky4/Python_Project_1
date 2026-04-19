import qrcode

data = input("Enter the text or URL to encode in the QR code: ")

filename = input("Enter the filename to save the QR code (without extension): ") + ".png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(filename)
print(f"QR code generated and saved as {filename}")