from PIL import Image
import os
import sys

import argparse


def Main():
    #arg Parser ----------------------------
    parser=argparse.ArgumentParser(description="Turns each pixel of the image to black or white - depending on the chosen threshold")

    parser.add_argument('filename', type=str, help='Enter file name, including exstension')

    group=parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--threshold', type=int, help='Enter threshold value : between 0(full white) and 255(full black)')
    group.add_argument('-i', '--iteration', type=int, help='Enter iteration value : images will be created for each i iteration')

    args: Namespace = parser.parse_args()

    #Image file you want to use -----------
    dir = os.getcwd()
    img = Image.open(dir+'/'+ args.filename)
    fullname = dir + '/' + args.filename.split(".")[0]

    #Picture manipulation
    if args.threshold is not None:
        bwimg(int(args.threshold), fullname, img)
    else:
        for i in range(0, 255, args.iteration):
            bwimg(i, fullname, img)


def bwimg(threshold, full_path, picture):
    fn = lambda x : 255 if x > threshold else 0
    r = picture.convert('L').point(fn, mode='1')
    r.save(full_path + '_' + str(threshold) + '.png')

if __name__ == '__main__':
    Main()