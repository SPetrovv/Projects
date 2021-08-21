import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)
qr.add_data('https://www.google.com')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('google.png')


#can do svg type of files so they can be resized