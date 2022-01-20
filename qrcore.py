import qrcode
import cv2

def qrcodemake(string):
    img = qrcode.make(string)
    return img

def qrcodesave(img):
    img.save("qrcode.jpg")

def qrcodedecoder(string):
    newimg = cv2.QRCodeDetector()
    new, points, _ = newimg.detectAndDecode(cv2.imread(string))
    return new

print("You want to code or decode? ")
choice = str(input("Code <- -> Decode ")).lower()
if(choice=="code"):
    string = str(input("Insert link you want to turn into QRCode "))
    img = qrcodemake(string)
    qrcodesave(img)
else:
    string = str(input("Enter the Path of the QRCode you want to decode "))
    print(qrcodedecoder(string))

