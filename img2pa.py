from PIL import Image
import os
import sys

dir = os.getcwd()
img = Image.open(dir+'/'+ sys.argv[1])

for i in range(0, 251, 25): #for multiple iteration
    thresh = i
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    r.save(dir + '/bg_const_bw_' + str(i) + '.png')