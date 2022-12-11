from PIL import Image
import os
import sys

#git image file you want to use
dir = os.getcwd()
img = Image.open(dir+'/'+ sys.argv[1])
fullname = dir + '/' + sys.argv[1].split(".")[0]

def bwimg(threshold, full_path):
    fn = lambda x : 255 if x > threshold else 0
    r = img.convert('L').point(fn, mode='1')
    basewidth = int(sys.argv[5])
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    s = r.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    s.save(full_path + '_' + str(threshold) + '.png')

#Help
if "-h" in str(sys.argv):
    print("You asked for help with -h, for threshold use -t <value>, for iteration -i <value>")
    print(fullname)
    exit()

#Create 1 b&w image with 1 threshold
elif "-t" in str(sys.argv):
    bwimg(int(sys.argv[3]), fullname)
    exit()

#Create multiple images with iterations as thresholds
elif "-i" in str(sys.argv):
    for i in range(0, 255, int(sys.argv[3])): #for multiple iteration
        bwimg(i, fullname)
    exit()

else:
    exit()

