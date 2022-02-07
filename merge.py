#!/usr/bin/python

import sys

#getOpt a module that helps you parse CMD options and arguments

def main(argv) :
    outputFile = sys.argv[3]

#List of files from the cmd
filenames = [sys.argv[1], sys.argv[2]]

#Open file 3 (outputfile) in write mode
with open(sys.argv[3], 'w') as outfile:
    for files in filenames:
        #Open each file in read mode
        with open(files) as infile:
            #Read each data in file 1 & file 2 and write them in file 3
            outfile.write(infile.read())
            #Add a next line to file 2 after appending
            outfile.write("\n")



    #    
    # for opt, arg in opts:
    #     if opt == '-h':
    #     print('merge.py -i <inputFile1> -ii <inputFile2> -o <outputFile>')
    #     sys.exit()
    #     with open: 
