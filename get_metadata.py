import PIL.Image
import os
from os.path import isfile, join, exists, isdir
from PIL.ExifTags import TAGS
import fnmatch

def get_date(image):

	img = PIL.Image.open(image)

	exif_data = img._getexif()
	
	#print (exif_data)
	print (exif_data[34853])
	#return split_up(exif_data[36868])
	
def split_up(date_in):
	
	sp = date_in.split(':')
	return sp[0]+"_"+sp[1]
	
date = get_date('IMG_3351.JPG')

if not os.path.exists('dated\{}'.format(date)):
	os.makedirs('dated\{}'.format(date))