import os
import shutil

src = "track"

count =  91

dst = "test/"


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

for __ in range(91,100):
	src = "track00" + str(__) + "/"
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		shutil.copy2(s,d)
		

for __ in range(100,151):
	src = "track0" + str(__) + "/"
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		shutil.copy2(s,d)
