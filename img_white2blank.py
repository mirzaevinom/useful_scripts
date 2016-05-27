# -*- coding: utf-8 -*-
"""
Created on Wed May 25 10:30:11 2016

@author: Inom Mirzaev

Takes an image as an input. 
Gets rid of unnecessary background white space.
Saves it in an output file
Run the script as
    img_white2blank.py -i <inputfile> -o <outputfile>
"""

from PIL import Image


import sys, getopt


inputfile = ''
outputfile = ''
try:
    opts, args = getopt.getopt(sys.argv[1:] ,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'img_white2blank.py -i <inputfile> -o <outputfile>'
    sys.exit(2)    

for opt, arg in opts:
    if opt == '-h':
        print "Takes an image as an input."
        print "Gets rid of unnecessary background white space."
        print "Saves it in an output file"
        print "instructions:"
        print '    img_white2blank.py -i <inputfile> -o <outputfile>'
        sys.exit()
    elif opt in ("-i", "--ifile"):

        if arg[-4:]=='.png':
            inputfile = arg
        else:
            print 'Input file should end with ".png"'
            sys.exit()
    elif opt in ("-o", "--ofile"):
     
        if arg[-4:]=='.png':
            outputfile = arg
        else:
            print 'Output file should end with ".png"'
            sys.exit()
            
img = Image.open( inputfile )
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata( newData )
img.save( outputfile, "PNG")
