from PIL import Image
from ctypes import windll as WDLL
from os.path import abspath as Path
from PIL.ImageFilter import GaussianBlur as Blur

def Main():
    print("Drag n Drop the image file here and press Enter", end = ' ')
    File = input()
    Desktop = Image.open(repr(File)[1:len(repr(File)) - 1])
    Desktop.save('WallPaper.png')
    Desktop.save('Login.png')
    Login = Image.open('Login.png')
    Login = Login.filter(Blur(Percent(3, list(Login.size)))).save('Login.png')
    WDLL.user32.SystemParametersInfoW(0x14, 0, Path('WallPaper.png'), 3)
    print("Desktop changed suu=ccessfully")
    input()
    pass

def Percent(Percentage = float(), Dimensions = []):
    print(Dimensions[0])
    Size = min(Dimensions)
    Pixels = int((Percentage * Size) / 100)
    return Pixels

Main()
