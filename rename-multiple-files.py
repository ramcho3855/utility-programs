#author@ramavatar
#python program to rename files in a directory using os.rename

import os


def rename(directory):
	counter = 501
	
	for filename in os.listdir(directory):
		src = directory + filename
		dstName = str(counter) + ".jpg"
		dst = directory + dstName
		
		os.rename(src, dst)
		counter += 1


#Driver code
if __name__ == '__main__':
	directory = "./../../Desktop/temporary/"			#directory of files to be renamed
	rename(directory)
