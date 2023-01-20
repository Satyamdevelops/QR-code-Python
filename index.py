import qrcode

img = qrcode.make("https://twitter.com/satyamdevelops")
img.save("SatyamDevelops.jpg")