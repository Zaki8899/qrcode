import generate_qrcode1

img = qrcode.make("https://leetcode.com/problemset/")
img.save("leetcode_qr.png")
