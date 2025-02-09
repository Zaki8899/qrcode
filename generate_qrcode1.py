import qrcode as qr
img = qr.make("https://leetcode.com/problemset/")
img.save("leetcode_qr.png")