import qrcode
from qrcode import QRCode
s="www.kensington.com"
url=qrcode.make(s)
url.save("qr.png")
print("QR-Code generated successfully")