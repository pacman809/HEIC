from PIL import Image
from pillow_heif import register_heif_opener
import sys
import ctypes

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

register_heif_opener()
try:
	image = Image.open(sys.argv[1])
	#print(image)
except:
	print("Invalid Input")
#image.show(f'OutPutHEIC.png', quality=100)
image.show()

