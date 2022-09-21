import os
import pyheif
from PIL import Image

files = os.listdir()

for file in files:
	
	if 'HEIC' in file:
		try:
			image = pyheif.read(file)
			image_pil = Image.frombytes(
				image.mode, 
		    	image.size, 
		    	image.data,
		    	"raw",
		    	image.mode,
		    	image.stride,
				)
			image_pil.save(file.split('.')[0], "JPEG")
		except:
			print(file + ' failed')
