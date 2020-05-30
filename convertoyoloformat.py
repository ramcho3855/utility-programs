from PIL import Image
import os
import shutil
import glob

dst = "training/"


def savetxt(filePath,dst):
	w= 1920
	h= 1080

	#filePath  = '/home/ramavatar/Desktop/UFPR-ALPR/UFPR-ALPR dataset/training/track0002/track0002[01].txt'
	f = open(filePath,'r')

	temp = f.readline()
	vline = f.readline().rstrip('\n')
	vline = vline.split(' ')
	cline = f.readline().rstrip('\n')
	cline = cline.split(' ')


	xmin = int(vline[1],10)
	ymin = int(vline[2],10)
	xmax = xmin + int(vline[3],10)
	ymax = ymin + int(vline[4],10)

	b = (xmin,xmax,ymin,ymax)
	bb = convert((w,h), b)
	if cline[1] == 'car':
		classCount = 0
	else:
		classCount = 1
	lineToWrite = str(classCount) + ' ' + str(bb[0]) + ' ' + str(bb[1]) + ' ' + str(bb[2]) + ' ' + str(bb[3])
	w = open(dst,'w')
	w.writelines(lineToWrite)
	w.close()


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    return (x,y,w,h)
    
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if item.endswith(".txt"):
        	savetxt(s,d)
        elif item.endswith(".png"):
        	shutil.copy2(s, d)



for __ in range(1,10):
	src = "/home/ramavatar/Desktop/UFPR-ALPR/UFPR-ALPR dataset/training/track000" + str(__) + "/"
	copytree(src,dst)
		

for __ in range(10,61):
	src = "/home/ramavatar/Desktop/UFPR-ALPR/UFPR-ALPR dataset/training/track00" + str(__) + "/"
	copytree(src,dst)



