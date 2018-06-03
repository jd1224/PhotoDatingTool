import PIL.Image 
import fnmatch
import shutil
import sys
import time
import os
from os import listdir
from os.path import isfile, join, exists, isdir
from PIL.ExifTags import TAGS
'''
This program will search a given directory for all 
'''

'''
# helper for get_date to extract the year and month
# from and EXIF formatted date as YYYY MM
#
'''
def split_up(date_in):
	
	sp = date_in.split(':')
	return sp[0]+"_"+sp[1]

'''
# function to give the value of the EXIF Tag for date
# input an image name and return the date in format 
# YYYY:MM:DD HH:MM:SS
# 
'''
def get_date(image):

	img = PIL.Image.open(image)

	exif_data = img._getexif()
	
	return split_up(exif_data[36868]) 
	
'''
# function to retrieve all files from a path
# returns a list of all files with extensions
# if the directory does not exist returns an 
# general exception
'''
def get_files(path):

	file_list =  []
	if isdir(path):
		#print(True)
		for i in listdir(path):
			file_list.append(i)
		
		#print (file_list)
		return file_list
	else:
		print('failed')
		raise exception
		
	
'''
# Function to find all files with the file extensions
# in the supplied list
# returns a list of all files matching the extension
# if no matching files returns an empty list
'''
def get_photos(file_list, file_types):
	
	photo_list = []
	for i in file_list:
		for j in file_types:
			if fnmatch.fnmatch(i, '*{}'.format(j)):
				photo_list.append(i)
				
	return photo_list

def main_loop():

	#path = 'D:\\Program Files\\Notepad++\\python3\\picchecker'
	# variable to count the number of undated pictures
	bc = 0
	
	#list of common picture file types ot check for
	file_types = ['.jpg','.tif','.tiff','.wav','.dct']
	running = True
	while running:
		path_choosing = True
		fc = 0
		while path_choosing:
			path = input("enter a file path to check for pictures: ")
			if os.path.exists(path):
				os.chdir(path)
				try:
				
					file_list = get_files(path)
					#print(file_list)
					path_choosing = False
				except:
					print('You cannot access that directory.  Try using administrator mode.')
			else:
				if fc<=3:
				
					print("Enter a valid directory path")
					fc +=1
				elif fc>3:
					
					print('A valid directory looks like this: {}'.format(sys.getcwd()))
				
		photo_list = get_photos(file_list,file_types)
		
		for i in photo_list:
			try:
				
				#print (get_date(i))
				date = get_date(i)
				name = date+' '+i
				#print ('dated '+i)
				
			except:
				
				#print ('{} Undated'.format(i))
				date = 'Undated'
				name = date+i
				#print ('undated '+i)
				bc +=1
				
			finally:
				if not os.path.exists('dated folder\{}'.format(date)):
					os.makedirs('dated folder\{}'.format(date))
				shutil.copy(i,'dated folder\{}\{}'.format(date,name))
				running = False
				
				
	print ('I could not apply a date to {} photographs'.format(bc))
	input('Press Enter to Continue')
				
def typewrite(line):
	
	for i in line:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(.0001)
		
def welcome():

	typewrite('******************************************************************************\n')
	typewrite('******************************Photo Dating Tool*******************************\n')
	typewrite('*******************************CLI Tool V 1.0*********************************\n')
	typewrite('************************|--------------------------|**************************\n')
	typewrite('*********Rename Photos**|\/\/\/\/_d^^^^^^b_/\/\/\/\|**************************\n')
	typewrite("*********Based on the***|\/\/\.d''########``b./\/\/|**************************\n")
	typewrite("*********Date Contained*|/\/\/::############::/\/\/|**************************\n")
	typewrite('*********Their METATAGS*|/\/\/`p.##########.q`/\/\/|**************************\n')
	typewrite('*********For the Date***|/\/\/\`p.########.q`/\/\/\|**************************\n')
	typewrite('*********They were taken|/\/\/\/\^q......p^/\/\/\/\|**************************\n')
	typewrite('************************|--------------------------|**************Created*****\n')
	typewrite('*************************Press Enter Key to Continue***************by*joshc1224\n')
	input('******************************************************************************\n')
def about():
	os.system('cls')
	print('This utility will copy without deleting original pictures in the format of .jpg, .tif, and .tiff')
	print('to a new folder named "dated\\yyyy_mm".  It is based on the meta data provided in the photo.')
	print('If the photo does not contain metadata in the tag for date created, the photo will be labeled')
	print('"Undated". All photos will be copied to the new directory and re-named "YYYY_MM <original name>"')
	print('or "Undated <original name>".  For updates and other programs check my Github repositories at')
	print('joshc1224.  There is a GUI Version of this program located there as well.')
	input('\nPress Enter to Continue')
	
def help():
	os.system('cls')
	print('For help please check my Github repository at joshc1224 for a FAQ document. For specific question email')
	print('joshc1224@yahoo.com with a detailed description of the porblem, and screenshots if available')
	input('Press Enter to Continue')
	
def goodbye():
	os.system('cls')
	print('GOODBYE AND THANK YOU FOR USING THIS TOOL')
	print('PLEASE CHECK MY GITHUB REPOSITORY FOR OTHER')
	print('USEFUL PROGRAMS AT JOSHC1224')
	
def menu():
	
	
	typewrite('1. About this program\n')
	typewrite('2. Help \n')
	typewrite('3. Organize photographs \n')
	typewrite('4. Exit program\n')
	choice = input('Make a choice from the above menu please: ')
	
	if choice == '1':
		about()
		return True
	elif choice == '2':
		help()
		return True
	elif choice == '3':
		main_loop()
		return True
	elif choice =='4':
		return False
	else:
		print('That was not a valid choice')
		input('Press Enter to Continue')
		return True
		
if __name__=="__main__":
	running = True
	
	#welcome()
	while running:
		running = menu()
		os.system('cls')
	goodbye()
	
	
	

				
				
				
				
				
				