from PIL import Image
import os
import sys

#git image file you want to use
dir = os.getcwd()
img = Image.open(dir+'/'+ sys.argv[1])

#Help
if "-h" in str(sys.argv):
    print("You asked for help with -h, for threshold use -t <value>, for iteration -i <value>")
    exit()
elif "-t" in str(sys.argv):
    thresh = int(sys.argv[3])
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    r.save(dir + '/bg_const_bw_' + str(thresh) + '.png')
    exit()

elif "-i" in str(sys.argv):
    for i in range(0, 255, int(sys.argv[3])): #for multiple iteration
        thresh = i
        fn = lambda x : 255 if x > thresh else 0
        r = img.convert('L').point(fn, mode='1')
        r.save(dir + '/bg_const_bw_' + str(i) + '.png')

else:
    exit()