"""Generating a QR Code for your Website, Social Media Handle, Image can be done by the following code
    snippet."""

import qrcode

url = input('Enter a valid url to generate the QR Code')

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(url)
qr.make_image(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

img.save('qr_code.png')
img.show()
